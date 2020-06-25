# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define kickoff_scientist = Character("Scientist")
image bg_kickoff = im.Scale("bg_lab_kickoff.png", 1280, 720)


# The game starts here.

label start:

    scene bg_kickoff

    kickoff_scientist "Here at LAB-117, our project, PROJECT MONSTER, aims to create a fetus capable of morphing into any lifeform as we please."
    kickoff_scientist "With such creation, any lifeform beneficial to mankind may be within our grasp."
    kickoff_scientist "As it stands, our team has successfully created the monstrous fetus, a colorless blob-like fetus cultured inside our incubator pod, that we were hoping for."
    kickoff_scientist "Now, PROJECT MONSTER should be taken towards another direction and another team, so it can be tested and observed."

    menu:
        kickoff_scientist "Question now is what curious life form shall we arise from this growing fetus."

        "Project Yggdrasil":
            jump project_yggdrasil
        "Project Chef":
            jump project_chef
        "Project Cookie":
            jump project_cookie
        "Project Fetch":
            jump project_fetch
        "Project Giggles":
            jump project_giggles

    # This ends the game.

    return
