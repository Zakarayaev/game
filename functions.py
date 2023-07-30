import variables
import lists


def background_anim():  # this function will be move the background
    variables.background_x -= 3
    if variables.background_x == -1000:
        variables.background_x = 0


def background_music():  # for background misic play
    variables.background_music.play()


def player_anim():  # this function wil be iterate the list walk_right and so
    if variables.player_anim_count == 6:  # will be animation of player
        variables.player_anim_count = 0
    else:
        variables.player_anim_count += 1


def player_jump_anim():  # for animayion of player jump
    if variables.jump_right_anim_count == 19:
        variables.jump_right_anim_count = 0
    else:
        variables.jump_right_anim_count += 1


def delete_ninja():  # for ninja output and delete and animation
    import main

    main.screen.blit(
        lists.ninja_enemy[variables.ninja_anim_count],
        (variables.ninja_x, variables.ninja_y))

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
