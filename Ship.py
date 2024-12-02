import pygame as pg

class Ship():
    def __init__(self ,ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        original_image = pg.image.load('images/Ship.bmp')
        self.original_rect = original_image.get_rect()

        # Define the desired width and height for the image
        desired_width = 100  # Adjust this to your preferred width
        aspect_ratio = self.original_rect.width / self.original_rect.height
        desired_height = int(desired_width / aspect_ratio)

        # Scale the image to the desired dimensions
        self.image = pg.transform.scale(original_image, (desired_width, desired_height))

        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)
