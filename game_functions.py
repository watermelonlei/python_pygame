
# coding=UTF-8
import sys
import pygame
from bullet import Bullet
from pygame.sprite import Group
from alien import Alien
from random import randint
from time import sleep

def check_keydown_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True 
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        ship.fire_bullet = True
    elif event.key == pygame.K_q:
        sys.exit()

def check_keyup_event(event,ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False 
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_SPACE:
        ship.fire_bullet = False



def check_cvent(ai_setting,screen,stats,play_button,ship,aliens,bullets):
    for event in pygame.event.get():
        if event == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event,ship)
        elif event.type == pygame.KEYUP:
            check_keyup_event(event,ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_setting,screen, stats,play_button,ship,aliens,bullets,mouse_x,mouse_y)

def check_play_button(ai_setting,screen,stats,play_button,ship,aliens,bullets,mouse_x,mouse_y):
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)

    
    if button_clicked and  not stats.game_active:
        ai_setting.init_settings()
        pygame.mouse.set_visible(False)
        stats.reset_stats()
        stats.game_active = True
        aliens.empty()
        bullets.empty()
        create_fleet(ai_setting,screen,ship,aliens)
        ship.center_ship()
    else:
        print(play_button.rect,mouse_x,mouse_y)



def update_screen(ai_setting,screen,stats,sb,ship,bullets,aliens,play_button):
    screen.fill(ai_setting.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)
    sb.show_score()
    if not stats.game_active:
        play_button.draw_button()
    # 更新整个待显示的  Surface 对象到屏幕上
    pygame.display.flip() 
    
def update_bullets(ai_setting,screen,stats,sb,ship,aliens,bullets):
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collosion(ai_setting,screen,stats,sb,ship,aliens,bullets)
    
    
def check_bullet_alien_collosion(ai_setting,screen,stats,sb,ship,aliens,bullets):
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        print("collisions.values",collisions.values)
        for aliens in collisions.values():
            stats.score += ai_setting.alien_points * len(aliens)
            print("ai_setting.alien_points",ai_setting.alien_points)
            print("len(aliens)",len(aliens))
            sb.prep_score()

    if len(aliens) == 0:
        bullets.empty()
        ai_setting.increase_speed()
        create_fleet(ai_setting,screen,ship,aliens)
        
def create_fleet(ai_setting,screen,ship,aliens):
    alien = Alien(ai_setting,screen)
    number_aliens_x = get_number_aliens_x(ai_setting,alien.rect.width)
    if 0 == number_aliens_x % 2:
        number_aliens_x += 1 
    #number_rows = get_number_rows(ai_setting,ship.rect.height,alien.rect.height)
    number_rows = int((number_aliens_x + 1) / 2)
    aliens_type = randint(1,3)
    if 1 == aliens_type:
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                create_alien(ai_setting,screen,aliens,alien_number,row_number)
    elif 2 == aliens_type:
        last_row_alien_number = (2 - number_aliens_x % 2)
        every_row_reduce = int((number_aliens_x - last_row_alien_number) / number_rows)
        for row_number in range(number_rows):
            for alien_number in range(row_number * every_row_reduce,number_aliens_x - row_number * every_row_reduce):
                create_alien(ai_setting,screen,aliens,alien_number,row_number)
        
    elif 3 == aliens_type:
        alien_number = randint(0,number_aliens_x)
        directtion = 1
        for row_number in range(number_rows):
            create_alien(ai_setting,screen,aliens,alien_number,row_number)
            if alien_number >= number_aliens_x:
                directtion = -1
            elif alien_number <= 0:
                directtion = 1
            alien_number += directtion
        

        
def get_number_aliens_x(ai_setting,alien_width):
    available_space_x = ai_setting.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x 
    
def get_number_rows(ai_setting,ship_height,alien_height):
    available_space_y = (ai_setting.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows
    
def create_alien(ai_setting,screen,aliens,alien_number,row_number):
    alien = Alien(ai_setting,screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)
    
def ship_hit(ai_setting,stats,screen,ship,aliens,bullets):
    stats.ship_left -= 1
    if stats.ship_left > 0 :
        print('stats.ship_left',stats.ship_left)
        aliens.empty()
        bullets.empty()
        create_fleet(ai_setting,screen,ship,aliens)
        ship.center_ship()
        sleep(2)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)
    
    
    
def update_aliens(ai_setting,stats,screen,ship,aliens,bullets):
    check_fleet_edges(ai_setting,aliens)
    aliens.update()
    
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_setting,stats,screen,ship,aliens,bullets)
        
    check_alien_bottom(ai_setting,stats,screen,ship,aliens,bullets)
    
def check_fleet_edges(ai_setting,aliens):
    for alien in aliens:
        if (alien.check_edges()):
            change_fleet_direction(ai_setting,aliens)
            break
            
def change_fleet_direction(ai_setting,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_setting.fleet_drop_speed
    ai_setting.fleet_direction *= -1
    
    
def check_alien_bottom(ai_setting,stats,screen,ship,aliens,bullets):
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_setting,stats,screen,ship,aliens,bullets)
            break
            

    
            
