 
import pygame.font

class Scoreboard:
    def __init__(self,ai_setting,screen,stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_setting = ai_setting
        self.stats = stats
        
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        
        self.prep_score()
        
    def prep_score(self):
        rounded_score = int(round(self.stats.score,-1))
        print("score:",self.stats.score)
        score_str = "Score:" + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str,True,self.text_color,self.ai_setting.bg_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.left + 200
        self.score_rect.top = 20 
        
    def show_score(self):
        self.screen.blit(self.score_image,self.score_rect)
