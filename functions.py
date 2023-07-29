import pygame
import variables
import lists


def player_anim():  # this function wil be iterate the list walk_right and so
    if variables.player_anim_count == 6:  # will be animation of player
        variables.player_anim_count = 0
    else:
        variables.player_anim_count += 1


# def rect():
#     import pygame
#     import main
#     pygame.init()
#     player_rect = lists.walk_right[0].get_rect(topleft=(
#         variables.player_x,
#         variables.player_y
#         ))
#     if main.ninja_enemy_in_game:
#         for element in main.ninja_enemy_in_game:
#             main.screen.blit(main.ninja_enemy[0], element)
#             element.x -= 10

#     def ninja_anim():
#         if variables.ninja_anim_count == 21:
#             variables.ninja_anim_count = 0
#         else:
#             variables.ninja_anim_count += 1
#         if player_rect.colliderect(element):
#             print("You lose")
#             print("Do you want to restart?")
#     ninja_anim()


def test():
    import main
    pygame.init()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # this loop for left animation of player
        main.screen.blit(lists.walk_left[variables.player_anim_count],
                         (variables.player_x, variables.player_y))
    else:  # and this loop for right animation of player
        main.screen.blit(lists.walk_right[variables.player_anim_count],
                         (variables.player_x, variables.player_y))


def delete_ninja():
    def ninja_movement():
        if variables.ninja_anim_count == 21:
            variables.ninja_anim_count = 0
        else:
            variables.ninja_anim_count += 1
        variables.ninja_x -= 10
    if variables.ninja_x >= 1011:
        # del ninja_blit
        print("Ninja was deleted")
    ninja_movement()


def background_anim():  # this function will be move the background
    variables.background_x -= 3
    if variables.background_x == -1011:
        variables.background_x = 0


def background_music():
    variables.background_music.play()
