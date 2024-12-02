import pygame as pg
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        
        original_image = pg.image.load('images/alien1.bmp')
        self.original_rect = original_image.get_rect()

        desired_width = 50  # Adjust this to your preferred width
        aspect_ratio = self.original_rect.width / self.original_rect.height
        desired_height = int(desired_width / aspect_ratio)

        self.image = pg.transform.scale(original_image, (desired_width, desired_height))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        
    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left<= 0:
            return True   

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor*self.ai_settings.fleet_direction)
        self.rect.x = self.x

        
    def blitme(self):
        self.screen.blit(self.image, self.rect)
