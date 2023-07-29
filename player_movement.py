import pygame
import variables


def player_movement():
    global keys
    pygame.init()
    keys = pygame.key.get_pressed()  # this variable to track keystroke
    if keys[pygame.K_d] and variables.player_x < 270:
        variables.player_x += variables.player_speed
    elif keys[pygame.K_a] and variables.player_x > 50:
        variables.player_x -= variables.player_speed


def player_jump():
    if not variables.is_jump:
        if keys[pygame.K_SPACE]:
            variables.is_jump = True
    else:
        if variables.jump_count >= -9:
            if variables.jump_count > 0:
                variables.player_y -= (variables.jump_count ** 2) / 2
                variables.player_x += 10
                # print(variables.player_y)
            else:
                variables.player_y += (variables.jump_count ** 2) / 2
                variables.player_x += 10
                # print(variables.player_y)
                if variables.player_y > 290:
                    variables.player_y = 290
            variables.jump_count -= 1
        else:
            variables.is_jump = False
            variables.jump_count = 9
            # variables.player_y = 362
            # variables.player_y = 322
            # variables.player_y = 290

    if keys[pygame.K_SPACE]:
        print("Space was pressed")
