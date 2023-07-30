import pygame


pygame.init()
# pygame.mixer.init()
# background_music = pygame.mixer.Sound("sounds/8597bb02c2b2555.mp3")


# background
background = pygame.image.load("images/background_for_game.jpg")
background_x = 0  # background x position


# player positions
player_x = 100
player_y = 290
jump_x = 100
jump_y = 290

# player animation
player_anim_count = 0  # this variable will be iterate in the main.py
jump_right_anim_count = 0

# other
player_speed = 9  # this veriable for player movement
is_jump = False  # this jump watch is jump true or false
jump_count = 7


# ninja enemy
ninja_anim_count = 0
ninja_x = 800
ninja_y = 305


keys = pygame.key.get_pressed()  # this variable to track keystroke
