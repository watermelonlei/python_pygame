# coding=UTF-8

# update方法，适用于控制sprite对象行为的方法。 基类中该方 法没有任何实现， 这是等着我们自己去覆盖的。
# add方法，将该sprite对象增加到group中，存疑。
# remove方法。sprite对象会从group中删掉。
# kill方法，将该sprite对象从所有groups中删掉。
# groups方法，返回sprite对象所在的所有组。
# alive方法，判断sprite方法是否还在组中。

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_setting,screen):
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_setting = ai_setting
        
        # 外星人图片
        self.image = pygame.image.load('alien.bmp')
        self.rect = self.image.get_rect()
        
        # 初始位置为宽高
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        
    def blitme(self):
        #将图形渲染到Alien
        self.screen.blit(self.image,self.rect)
        
    # 重写 适用于控制sprite对象行为的方法
    # 移动外星人
    def update(self):
        self.x += (self.ai_setting.alien_speed_factor * self.ai_setting.fleet_direction)
        self.rect.x = self.x
   
   # 检验外星人是否位于屏幕边缘 就返回true
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if (self.rect.right >= screen_rect.right):
            return True
        elif (self.rect.left <= 0):
            return True
    
    
