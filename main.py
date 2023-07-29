import pygame
import variables
import functions
import player_movement
import lists


# pygame setup
pygame.init()
pygame.mixer.init()  # for sound output
screen = pygame.display.set_mode((1011, 600))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()  # to set the number of FPS
ninja_enemy_in_game = []  # type: list
running = True


# main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # pygame.quit()

    screen.blit(variables.background, (variables.background_x, 0))
    screen.blit(variables.background, (variables.background_x + 1011, 0))
    ninja_blit = screen.blit(lists.ninja_enemy[variables.ninja_anim_count],
                             (variables.ninja_x, variables.ninja_y))
    functions.background_anim()
    functions.player_anim()
    functions.test()
    player_movement.player_movement()
    player_movement.player_jump()
    functions.delete_ninja()
    # functions.rect()
    pygame.display.flip()
    clock.tick(6)  # limits FPS  to 6


pygame.quit()
