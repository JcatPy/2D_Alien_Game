import pygame as pg
from Settings import settings
from Ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button

def game():
    pg.init()
    ai_settings = settings()
    screen  = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Alien Invasion Game")
    play_button = Button(ai_settings, screen, "Play")

    stats = GameStats(ai_settings)
    ship = Ship(ai_settings,screen)
    alien = Alien(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    gf.create_fleet(ai_settings, screen,ship,aliens)

    while True:
        gf.check_events(ai_settings, screen, stats, play_button,aliens, ship,bullets)
       
        bullets.update()
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,aliens,bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets,
 play_button)
        
game()

   
