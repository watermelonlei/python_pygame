# coding=UTF-8
import pygame
from bullet import Bullet

# author:watermelonlei
# coding=GBK
# edit in dev
class Ship():
    def __init__(self,ai_setting,screen):
        self.screen = screen
        self.ai_setting = ai_setting;
        
        self.image = pygame.image.load('planlet.bmp')
         
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        self.center = float(self.rect.centerx)
        
        
        self.moving_left  = False 
        self.moving_right = False
        self.fire_bullet  = False
        
    def add_bullet(self,bullets):
        if len(bullets) < self.ai_setting.bullet_allowed:
            new_bullet = Bullet(self.ai_setting,self.screen,self)
            bullets.add(new_bullet)
        
    def update(self,bullets):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_setting.ship_speed_factor
        self.rect.centerx = self.center
        
        if self.fire_bullet:
            self.add_bullet(bullets)
            
        
    def blitme(self):
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        self.center = self.screen_rect.centerx
	def print_ship(self):
	    print(self.rect)
