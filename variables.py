import pygame
# import lists

pygame.init()
# pygame.mixer.init()
# background
background = pygame.image.load("images/background_for_game.jpg")
background_x = 0  # background x position
# background_music = pygame.mixer.Sound("sounds/8597bb02c2b2555.mp3")
player_anim_count = 0  # this variable will be iterate in the main.py


# veriables for player movement
player_speed = 9
player_x = 100  # player x position


# variables for jump
player_y = 290
is_jump = False
jump_count = 7

# ninja enemy
ninja_anim_count = 0
ninja_x = 800
ninja_y = 305

ninja_enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ninja_enemy_timer, 3000)
