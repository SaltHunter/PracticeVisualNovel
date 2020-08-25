﻿# The script of the game goes in this file.

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


    # These display lines of dialogue.

    k "*sighs* Why do I need to go to school..."

    k "Everyday is so monotone, even the skies are monochrome..."
    
    k "I wish I can just disappear."

    k "But alas, as my parents have paid my school fees, I have to go to school, do the daily routine"

    scene bg hill
    with fade
    

    "As I look up the hill, I feel that it's so high, and so hard to approach, and then,"

    que "*Achoo*"

    k "Hm?"

    
    show carmen frown:
        xalign 0.5
        yalign -0.05

    que "Why are you here? aren't you supposed to go to school?"

    k "I'm going there, what about you?"

   
    show carmen frown blush:
        xalign 0.5
        yalign -0.05

    que "U...Um...I, just woke up late! that's all! why are you staring at me like that?! Pervert!"

    "This, is the type of female i don't like, the school's beauty, A self-proclaimed 'Ice queen', thinking that she is some princess atop a lofty throne"

    "Who does she think she is? some kind of god? Hmph! such self-centered and egoistic ideals are what sets off wars, crumble nations and..."

    
    show carmen shout:
        xalign 0.5
        yalign -0.05
    
    que "WHO ARE YOU CALLING SELF CENTRED?!"

    "*WHAM!* *WHAM!* *WHAM!*"

    k "Damn, I let my inner monologue out again..."

    show carmen frown blush:
        xalign 0.5
        yalign -0.05

    que "Hmph! That ought to teach you next time we see each other."

    que "Hmph! I should get myself to class, thanks for wasting my time!"

    "*footstep sfx*"

    hide carmen frown blush

    k "Tch, How rude, she didn't even introduce herself, that's why I hate humanity."

    k "This world is distorted, thus gundam and I will change the world."

    menu gundam_and_i:
        "Change the world!":
            #block of code to run
            call za_warudo
            jump gundam_and_i

        "...":
            #block of code to run
            jump commonroute2

# This label and the text under for the label is actually unnecessary, but I put it here to demonstrate 
# what call does. -io
label za_warudo:

    k "Just watch. GUNDAM! COME FORTH! LET US CHANGE THE WORLD!"

    "...but nobody came. All I get is a cringing stare from the girl."

    return

label commonroute2:

    que "Yeah, whatever."

    que "Hmph, what a deluding idiot."

    scene bg classroom
    with fade

    k "Looks like I still came too school early today."
    menu:

        "Should I head to the cafeteria.":
            
         jump sunyi_scene1

         label sunyi_scene1: 

         k "I head towards the cafeteria, but on the way I pass by my school's library."

         scene bg library
         with fade

         k "I notice a prim and proper girl sitting inside seemingly enamored by the book she is reading."

         k "I look closer and notice her prim slender figure and short smooth jet black hair, as if the personification of a Yamato Nadeshiko."

         k "The more I look the more I notice features that just seem to-"

         k "Hm...? Is.. Is that!?"

         k "STEEL BALL RUN!!!??"
  
         jump sunyiroute1

         label sunyiroute1:

             a "Hya!?"

             show sunyi surprised blush
             with fade

             a "W-Who??"

             k "Oh, sorry for surprising you. I was just interested in the book you were reading..." 

             a "!?"

             a "You know it!? It's one of my treasures!"

             a "The two main characters are a disgraced former executioner for a European government, and a paraplegic former horse jockey celebrity. There are several themes in the story, the first of which is the western theme demonstrated in the location of the story, 1890’s America. The main method used to run in the race is on horseback and several characters are evocative of the classic image of the American cowboy, straight down to the use of lassos and six-shooters. Another staple mode of transportation of young America is the train used by the wealthy runners of the Steel Ball Run and the President. The background and characters are very detailed, and the stylization of the characters are impressive. The characters are unique within the shonen/seinen genere at large and amongst each other."

             a "Ah!"

             a "Sorry..."

             k "Uhh..."

             a "Um, class is starting! Ex- Excuse me!"

             hide sunyi surprised blush

             k "Ah, she ran away"

             scene bg classroom
             with fade

             return    

    # This ends the game.

    return

