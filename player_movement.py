import pygame

import variables


def player_movement():
    global keys
    keys = pygame.key.get_pressed()  # this variable to track keystroke
    if keys[pygame.K_d] and variables.player_x < 270:
        variables.jump_x += variables.player_speed
    elif keys[pygame.K_a] and variables.player_x > 50:
        variables.jump_x -= variables.player_speed


def player_animation_A_D():  # Animation of the player depending
    import main   # on the pressing of the buttons
    import lists

    global keys
    keys = pygame.key.get_pressed()  # this variable to track keystroke

    if not keys[pygame.K_SPACE]:
        if keys[pygame.K_a]:  # this loop for playr's left
            main.screen.blit(
                lists.walk_left[variables.player_anim_count],
                (variables.player_x, variables.player_y)
                )
        else:
            global player_walk_right
            player_walk_right = main.screen.blit(
                lists.walk_right[variables.player_anim_count],
                (variables.player_x, variables.player_y)
            )


def player_jump():
    import main
    import lists

    pygame.init()
    global player_walk_right
    global keys
    keys = pygame.key.get_pressed()  # this variable to track keystroke
    if not variables.is_jump:
        if keys[pygame.K_SPACE]:
            variables.is_jump = True
    else:
        if variables.jump_count >= -9:
            main.screen.blit(
                lists.jump_right[variables.jump_right_anim_count],
                (variables.jump_x, variables.jump_y)
            )
            if variables.jump_count > 0:
                main.screen.blit(
                    lists.jump_right[variables.jump_right_anim_count],
                    (variables.jump_x, variables.jump_y)
                )
                variables.jump_y -= (variables.jump_count ** 2) / 2
                variables.jump_x += 10
            else:
                variables.jump_y += (variables.jump_count ** 2) / 2
                variables.jump_x += 10
                if variables.jump_y > 290:
                    variables.jump_y = 290
            variables.jump_count -= 1
        else:
            variables.is_jump = False
            variables.jump_count = 9
    variables.player_x = variables.jump_x
