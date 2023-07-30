import pygame

import variables
import functions
import player_movement
# import lists


# pygame setup
pygame.init()
pygame.mixer.init()  # for sound output
screen = pygame.display.set_mode((1003, 600))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()  # to set the number of FPS
running = True


# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # pygame.quit()

    # background output
    screen.blit(variables.background, (variables.background_x, 0))
    screen.blit(variables.background, (variables.background_x + 1003, 0))

    # background animation
    functions.background_anim()

    # player
    functions.player_anim()
    functions.player_jump_anim()
    player_movement.player_jump()
    player_movement.player_movement()
    player_movement.test()

    # ninja
    functions.delete_ninja()

    pygame.display.flip()

    clock.tick(6)  # limits FPS  to 6


pygame.quit()
