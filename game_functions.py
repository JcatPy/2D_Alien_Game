import pygame as pg
import sys
from bullet import Bullet
from alien import Alien
from pygame import mixer
from time import sleep

mixer.init()

def check_keydown_events(event, ai_settings, screen, Ship, bullets):
     if event.key == pg.K_RIGHT:
         Ship.moving_right = True
     elif event.key == pg.K_LEFT:
         Ship.moving_left = True
     elif event.key == pg.K_SPACE:
          fire_bullet(ai_settings, screen, Ship, bullets)
          


def fire_bullet(ai_settings, screen, ship, bullets):
     if len(bullets) < ai_settings.bullets_allowed:
          new_bullet = Bullet(ai_settings, screen, ship)
          bullets.add(new_bullet)

def get_number_aliens_x(ai_settings, alien_width):
     available_space_x = ai_settings.screen_width - 2 * alien_width
     number_aliens_x = int(available_space_x / (2 * alien_width))
     return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
     available_space_y = (ai_settings.screen_height -(3 * alien_height) - ship_height)
     number_rows = int(available_space_y / (2 * alien_height))
     return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
     alien = Alien(ai_settings, screen)
     alien_width = alien.rect.width
     alien.x = alien_width + 2 * alien_width * alien_number
     alien.rect.x = alien.x
     alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
     aliens.add(alien)

def create_fleet(ai_settings, screen,ship,aliens):
     alien = Alien(ai_settings, screen)
     number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
     number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
     for row_number in range(number_rows):
          for alien_number in range(number_aliens_x):
               create_alien(ai_settings, screen, aliens, alien_number, row_number)
              
def check_keyup_events(event, Ship):
     if event.key == pg.K_RIGHT:
         Ship.moving_right = False
     elif event.key == pg.K_LEFT:
         Ship.moving_left = False
    

def check_events(ai_settings, screen, stats, play_button,aliens, ship,
 bullets):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            if event.key == pg.K_q:
                sys.exit()
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pg.MOUSEBUTTONDOWN:
             mouse_x, mouse_y = pg.mouse.get_pos()

             check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y)

def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, mouse_x, mouse_y):
     button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
     if  button_clicked and not stats.game_active:
          pg.mouse.set_visible(False)
          stats.reset_stats()
          stats.game_active = True

          aliens.empty()
          bullets.empty()

          create_fleet(ai_settings, screen, ship, aliens)
          ship.center_ship()

def update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button):
    '''screen.fill(ai_settings.bg_color)'''
    original_image = pg.image.load('images/background_image.bmp')
    original_rect = original_image.get_rect()
    desired_width = 1300  # Adjust this to your preferred width
    aspect_ratio = original_rect.width /original_rect.height
    desired_height = int(desired_width / aspect_ratio)
    background_image = pg.transform.scale(original_image, (desired_width, desired_height))
    screen.blit(background_image, (0, 0))
    ship.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
         bullet.draw_bullet()
    if not stats.game_active:
          play_button.draw_button()     
    pg.display.flip()

def update_bullets(ai_settings,screen,ship,aliens,bullets):
     for bullet in bullets.copy():
          if bullet.rect.bottom <= 0:
               bullets.remove(bullet)
     check_bullet_alien_collisions(ai_settings,screen, ship, aliens, bullets)
def check_bullet_alien_collisions(ai_settings,screen, ship, aliens, bullets):
     collisions = pg.sprite.groupcollide(bullets, aliens, True, True)
     if collisions:
          mixer.music.load("bullet_sound2.mp3")
          mixer.music.set_volume(1.5)
          mixer.music.play()

     if len(aliens) == 0:
          bullets.empty()
          create_fleet(ai_settings,screen, ship, aliens)

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
     check_fleet_edges(ai_settings,aliens)
     aliens.update()
     if pg.sprite.spritecollideany(ship, aliens):
          ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
     check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def check_fleet_edges(ai_settings, aliens):
     for alien in aliens.sprites():
          if alien.check_edges():
               change_fleet_direction(ai_settings, aliens)
               break
def change_fleet_direction(ai_settings, aliens):
     for alien in aliens.sprites():
          alien.rect.y += ai_settings.fleet_drop_speed
     ai_settings.fleet_direction *= -1

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
     if stats.ship_left > 0:
          stats.ship_left -=1
          aliens.empty()
          bullets.empty()
          create_fleet(ai_settings, screen, ship, aliens)
          ship.center_ship()
          sleep(0.5)
     else:
          stats.game_active = False
          pygame.mouse.set_visible(True)

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
     screen_rect = screen.get_rect()
     for alien in aliens.sprites():
          if alien.rect.bottom >= screen_rect.bottom:
               ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
               break






