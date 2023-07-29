import pygame


pygame.init()
screen = pygame.display.set_mode((1011, 600))

# player lists
walk_right = [
    pygame.image.load("images/player_right/player_right1.png").convert_alpha(),
    pygame.image.load("images/player_right/player_right2.png").convert_alpha(),
    pygame.image.load("images/player_right/player_right3.png").convert_alpha(),
    pygame.image.load("images/player_right/player_right4.png").convert_alpha(),
    pygame.image.load("images/player_right/player_right5.png").convert_alpha(),
    pygame.image.load("images/player_right/player_right5.png").convert_alpha(),
    pygame.image.load("images/player_right/player_right6.png").convert_alpha()
]

walk_left = [
    pygame.image.load("images/player_left/player_left1.png").convert_alpha(),
    pygame.image.load("images/player_left/player_left2.png").convert_alpha(),
    pygame.image.load("images/player_left/player_left3.png").convert_alpha(),
    pygame.image.load("images/player_left/player_left4.png").convert_alpha(),
    pygame.image.load("images/player_left/player_left5.png").convert_alpha(),
    pygame.image.load("images/player_left/player_left5.png").convert_alpha(),
    pygame.image.load("images/player_left/player_left6.png").convert_alpha()
]

# enemy lists
ninja_enemy = [
    pygame.image.load("images/ninja/ninja1.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja2.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja3.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja4.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja5.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja6.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja7.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja8.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja9.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja10.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja11.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja12.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja13.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja14.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja15.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja16.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja17.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja18.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja19.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja20.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja21.png").convert_alpha(),
    pygame.image.load("images/ninja/ninja22.png").convert_alpha()
]
