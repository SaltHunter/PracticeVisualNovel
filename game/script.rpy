# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kazuo")

define e = Character("Eilene")

define c = Character("Carmen")

define que = Character("???")



# The game starts here.

label start:

    jump commonroute

label commonroute:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    k "*sighs* why do I need to go to school"

    k "Everyday is so monotone, even the skies are monochrome, I wish I can just disappear."

    k "But alas, as my parents have paid my school fees, i have to go to school, do the daily routine"

    scene bg hill
    with fade

    show eileen happy

    "As i look up the hill, i feel that its so high, and so hard to approach, and then"

    que "*Achoo*"

    k "hm?"

    que "Why are you here? aren't you supposed to go to school?"

    k "I'm going there, what about you?"

    


    # This ends the game.

    return
