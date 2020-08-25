﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define k = Character("Kazuo")

define e = Character("Eilene")

define c = Character("Carmen")

define que = Character("???")

define crowd = Character("Crowd")

define h = Character("Hiroto")

define f = Character("Felise")

define az = Character("Azrail?")

define s = Character("Sunyi")



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

    que "eww...disgusting."

    crowd "psst psst psst"

    "Shit, a crowd's forming. . ."

    crowd "Cringeeee bro!"

    crowd "Major chuunibyo bro"

    "Ouch, thats a harsh remark."

    crowd "Is that what they call chuunibyo? disgusting bro!"

    "I think i need to get out of trouble here instead of causing another ruckus"

    return

label commonroute2:

    show carmen frown:
        xalign 0.5
        yalign -0.05

    que "Yeah, whatever."

    que "Hmph, what a deluding idiot."
    
    show carmen frown blush:
        xalign 0.5
        yalign -0.05

    que "We'd better get to class, lest you want your sorry chuuni behind to get done in by the teacher."

    "Tch, i'll get her next time..."

    hide carmen frown

jump routecontinue

label routecontinue:

    show bg classroom
    with fade

    que "Yo! Kazuo, late as always"

    que "It's allready recess, where have you been?"

    k "ah, you again, what's your name. . ."

    show hiroto happy

    que "How rude, we've been friends for 5 years and you forgot me?"

    que "Has being late fried your brain cells or somthing? but i guess if i got to tell you."

    h "Its Hiroto, you'd do well to remember that next time we meet, incase you forget it again."

    "This is hiroto, my fellow otaku friend, he always collects figures and models and he is usually one step ahead on me at these type of things."

    k "Like the 959 other times i forgot your name? yeah, you'd do well to remember that i will forget you."

    h "Tch, that's not what im trying to tell you though, have you seen the news? there's a new gundam model coming out this week"

    k "Yeah. . . i bought the pre-orders, and they're coming in by tomorrow."

    h "No fair! you should've notified me when they are open"

    k "Yeah, i kind of did, 3 months ago, but you said you're not buying it."

    "You reap what you sow i guess..."

    h "Tch, Let's just go to the cafeteria, im getting hungry."

    k "That resolves."

    hide hiroto happy

    show bg hallway
    with fade

    que "Umph!"

    "*papers scatter*"

    que "AAAH! i have to gather these papers now!"

    k "Maybe i should"

    menu papergirl:

        "Fight":
            call Fight
            jump papergirl

        "Magic":
            jump Magic

        "Item":
            jump Item

        "Friend":
            call Friend
            jump papergirl

label Fight:

    "Ok, let's run a simulation of the fight"

    show bg hallway
    with fade

    k "ORA!"

    "As the duel between two genders, two individuals, two differing ideologies began, a raging passionate duel!"

    "Two enter the ring, only one leaves"

    que "KYAAAAAH! He's Sexually Harassing Me!"

    "Yeah... forget the duel option."

    return

label Magic:

    show bg hallway
    with fade

    "Right, let me try casting a spell"

    k "I am the bone of my sword."

    k "Steel is my body, fire is my blood."

    k "I have created over a thousand blades"

    que "Hooh, so you too are a wizard"

    que "Very well then!"

    que "Reality be bent"

    k "Unknown to death, not known to life"

    k "I have created over a thousand blades"

    k "Yet these hands will hold nothing."

    que "Synapse Linkage, 100\% synchron!"

    que "Linkage Code QX5ABCD"

    que "Linkage Code Authorized"

    que "Reality break, engage!"

    k "Unlimited! Blade Works!"

    que "Vanishment! This World!"

jump commonroute3

label Item:

    "Hmmm..."

    menu items:

        "Pencil":
            call pencil
            jump Item

        "Wallet":
            call wallet
            jump Item

        "Student ID Card":
            call idcard
            jump items

        "Return":
            jump papergirl

label pencil:
    "What is this doing here?"

    "Riight, i need it to do my homework at the cafeteria, no way i can borrow it to her"

    "Besides, i left all of my pencils in class so that's that, i couldn't lend it to her."
    return

label wallet:
    "This is my wallet, containing the money i need to buy melonpan, and a iced tea"

    "Man, i want to eat kitsune udon though, the weather's getting hot here."

    "Doubt she needs me to lend her cash, considering im running low myself."
    return

label idcard: 
    "This is my id card, nothing new here"

    "It shows my basic information."

    "My name is Kazuo Mizuhara, i am your average teenage boy, aged 17"

    "My house is on the northeast side of tokyo, i currently live in the school dorms with hiroto."

    "I am not married, and am a student to this school."

    "I get home by 9pm latest, unless am doing some schoolwork with a friend"

    "I dont smoke, i dont drink either."

    "I'm in bed by 12pm latest, and i try to get at least 7 hours of sleep every day."

    "After drinking milk and doing my stretches before going to bed i often have no problems sleeping till morning"

    "Just like a baby, i often wake up without fatigue or stress in the morning, only hatred for humankind."

    "I was told i had no issues during the last health inspection"

    "I'm trying to say that i am a person who does not like to meddle with troublesome situations like the girl i met this morning"

    "Which would cause me to lose sleep at night.."

    "Although, if someone were to challenge me to a fight, i would win..."

    "Heh! what am i even doing?!"
    return

label Friend:
    k "Hiroto, do something!"

    h "I think you should help her out, apologize to her."

    k "Tch, you're useless."
    return


label commonroute3:
    show bg battlefield1
    show felice happy

    que "Fallen Angel, Azrail Deus Ex The Fifth."

    az "State your name! duellist, and we will fight a honorable duel"

    k "I have no name, i'll let my blades do the talking"

    az "Ho! so you're approaching me, instead of running away from me, the angel of death you're approraching me"

    k "Talk less ,fight more!"

    "*CLANG!*"

    "As 2 rulers clashed with her umbrella, she extends it, prooving to be somewhat of a  large lance"

    k "What's your class, lancer?"

    az "I have no obligation to tell you! Hyah!"

    "After a series of blows, both of them were readying their ultimate attacks untill"

    show bg hallway
    with fade
    hide felice happy
    show hiroto happy

    h "I think it's about time we went back to class, we have a math test you know"

    k "Not now hiroto! i'm in battle with the great azrail, the angel of death!"

    h "and i think you two are causing a scene"

    hide hiroto happy

    crowd "Major chuunibyou bro"

    crowd "Eww cringe!"

    crowd "Hey i've seen this guy before, he's the disgusting one from this morning!"

    show felice blush

    k "Tch! we shall continue our battle later!"

    az "Fair, and by the way"

    f "My human name is Felise, Felise Arrowheart from Class 3-A, so you know where to find me for our next duel"

    k "Do remember i settle my scores"

    show felice happy

    f "I'm counting on it! and farewell!"

    f "MUAHAHAHAHAHAHA!"

    hide felice happy

    h "Let's get to class, we have a math test to do."

    k "Resolves."

    scene bg classroom
    with fade

    k "Man That math test was hard, Hiroto, i'm going to the canteen, need anything?"

    h "I'll get the usual"

    k "Ocha and melonpan, gotcha, ill be back."

    scene bg hallway
    with fade

    k "Hmm, the library looks interesting, maybe i'll stop by it, i still have time to kill after all."
   

    scene bg library
    with fade

    k "I notice a prim and proper girl sitting inside seemingly enamored by the book she is reading."

    k "I look closer and notice her prim slender figure and short smooth jet black hair, as if the personification of a Yamato Nadeshiko."

    k "The more I look the more I notice features that just seem to-"

    k "Hm...? Is.. Is that!?"

    k "STEEL BALL RUN!!!??"
  
    que "Hya!?"

    show sunyi surprised blush
    with fade

    que "W-Who??"

    k "Oh, sorry for surprising you. I was just interested in the book you were reading..." 

    que "!?"

    que "You know it!? It's one of my treasures!"

    que "The two main characters are a disgraced former executioner for a European government, and a paraplegic former horse jockey celebrity. There are several themes in the story, the first of which is the western theme demonstrated in the location of the story, 1890’s America. The main method used to run in the race is on horseback and several characters are evocative of the classic image of the American cowboy, straight down to the use of lassos and six-shooters. Another staple mode of transportation of young America is the train used by the wealthy runners of the Steel Ball Run and the President. The background and characters are very detailed, and the stylization of the characters are impressive. The characters are unique within the shonen/seinen genere at large and amongst each other."

    que "Ah!"

    que "Sorry..."

    k "Uhh..."

    que "Um, class is starting! Ex- Excuse me!"

    hide sunyi surprised blush

    k "Ah, she ran away, before i even got her name."

    scene bg classroom
    with fade

    return    


    # This ends the game.

    return

