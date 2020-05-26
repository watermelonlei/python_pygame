# coding=UTF-8
class Setting:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (218,178,178)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3           #可以死三次
        
        self.bullet_speed_factor = 1
        self.bullet_width = 20        
        self.bullet_height = 20
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 10
        
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 2
        self.fleet_direction = 1 
       
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.init_settings()
        self.init_dynamic_settings()
        
    def init_settings(self):
        print('init_settings')
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1
        self.alien_speed_factor = 1
        self.fleet_direction = 1 
        
        
    def increase_speed(self):
        print('increase_speed')
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.speedup_scale)
        
        
    def init_dynamic_settings(self):
        self.alien_points = 50
    
