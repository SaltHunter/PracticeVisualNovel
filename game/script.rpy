# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kazuo")

define e = Character("Eilene")

define c = Character("Carmen")



# The game starts here.

label start:

    jump commonroute

label commonroute:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    k "*sighs* why do I need to go to school"

    k "Everyday is so monotone, even the skies are monochrome, I wish I can just disappear."


    # This ends the game.

    return
