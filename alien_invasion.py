# coding=UTF-8

import sys
import pygame
import game_functions as gf 
from pygame.sprite import Group
from setting  import Setting
from ship  import Ship
from alien import Alien
from game_stats import GameStats
from button  import Button
from scoreboard import Scoreboard

#  组 pygame.sprite.Group
#  sprites() 获得组
#  add()
#  copy()    副本
#  remove()  删除
#  has()     判断是否存在
#  update()  更新
#  draw()    位块显示
#  clear()   绘制背景
#  empty()   清空

def run_game():
    pygame.init()
    ai_settings = Setting()
    
    # 初始化一个准备显示的窗口或屏幕
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    
    #  Set the current window caption
    pygame.display.set_caption('Alirn Invasion')
    
    play_button = Button(ai_settings,screen,'Play')
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)
    ship = Ship(ai_settings,screen)
    # 组  
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)

    while True: 
        # 事件处理  标记ship移动方向
        gf.check_cvent(ai_settings,screen,stats,play_button,ship,aliens,bullets)
        
        
        if stats.game_active:
            
            # 移动飞船 发射子弹
            ship.update(bullets)
            
            # 子弹超出屏幕删除 子弹遇到外星人删除 子弹全部删除后再创建一组
            gf.update_bullets( ai_settings,screen,stats,sb,ship,aliens,bullets)
            
            # 外星人左右移动 并向下平移
            gf.update_aliens(ai_settings,stats,screen,ship,aliens,bullets)
            
        # 显示到屏幕
        gf.update_screen(ai_settings,screen,stats,sb,ship,bullets,aliens,play_button)

run_game()



