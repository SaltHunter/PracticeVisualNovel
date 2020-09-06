# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define mg = Character("Manager")

define k = Character("Kazuo")

define e = Character("Eilene")

define c = Character("Carmen")

define que = Character("???")

define crowd = Character("Crowd")

define h = Character("Hiroto")

define f = Character("Felise")

define az = Character("Azrael?")

define s = Character("Sunyi")

define sc = Character("Student Council")

define g1 = Character("Guy 1")

define g2 = Character("Guy 2")

define gi1 = Character("Girl 1")

define gi2 = Character("Girl 2")



# The game starts here.

label start:

    jump commonroute

label commonroute:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room1
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # These display lines of dialogue.

    k "*sigh* Why do I need to go to school..."

    k "Everyday is so monotone, even the skies are monochrome..."
    
    k "I wish I can just disappear."

    k "But alas, as my parents have paid my school fees, I have to go to school, do the daily routine."

    scene bg street
    with fade
    

    "As I go down the road to school, i feel the distance covered to school will consume too much energy, 
    and then..."

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

    "This, is the type of female i don't like, the school's beauty, A self-proclaimed 'Ice queen', 
    thinking that she is some princess atop a lofty throne"

    "Who does she think she is? some kind of god? Hmph! such self-centered and egoistic ideals are what 
    sets off wars, crumbling nations and..."

    
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

    "*footstep*"

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

    que "Eww...disgusting."

    crowd "*Whisper* *Whisper*"

    "Damn, a crowd's forming..."

    crowd "Cringeeee bro!"

    crowd "Major chuunibyo bro!"

    "Ouch, that's a harsh remark."

    crowd "Is that what they call chuunibyo? Disgusting bro!"

    "I think I need to get out of here instead of causing another ruckus..."

    return

label commonroute2:

    show carmen frown:
        xalign 0.5
        yalign -0.05

    que "Yeah, whatever."

    que "(What a deluding idiot.)"
    
    show carmen frown blush:
        xalign 0.5
        yalign -0.05

    que "We'd better get to class, lest you want your sorry chuuni behind to get done in by the teacher."

    "Tch, I'll get her next time..."

    hide carmen frown

jump routecontinue

label routecontinue:

    show bg classroom
    with fade

    que "Yo! Kazuo, late as always."

    que "It's already recess, where have you been?"

    k "Ah, you again. Who are you again?"

    show hiroto frown:
        xalign 0.5
        yalign -0.05

    que "How rude. We've been friends for 5 years and you forgot me?"

    que "Has being late fried your brain cells or something?"

    h "It's Hiroto, you'd do well to remember that next time we meet, in case you forget it again."

    "This is Hiroto, my fellow otaku friend, he always collects figures and models and he is usually 
    one step ahead on me at these type of things."

    k "Like the 959 other times I forgot your name? yeah, you'd do well to remember that I will 
    forget you."

    h "Tch, that's not what I'm trying to tell you though." 
    
    h "Have you seen the news? There's a new gundam model coming out this week."

    k "Yeah, I bought the pre-orders, and they're coming in by tomorrow."

    h "No fair! you should've notified me when they are open!"

    k "Yeah, I kind of did, 3 months ago, but you said you're not buying it."

    "You reap what you sow I guess..."

    h "Tch, Let's just go to the cafeteria, I'm getting hungry."

    k "That resolves."

    hide hiroto frown

    show bg hallway
    with fade

    "As we walk down the hallway to the cafeteria, a pink-haired girl carrying an unsteady stack 
    of papers walked to us"

    "And then..."

    show felise blush closeeyed:
        xalign 0.5
        yalign -0.05

    que "Umph!"

    "The papers flew and scattered around us."

    que "AAAH! I have to gather these papers now!"

    k "Maybe I should..."

    hide felise blush closeeyed

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

    "...Run a simulation of a fight."

    show bg hallway
    with fade
    show felise blush closeeyed:
        xalign 0.5
        yalign -0.05

    k "Face my secret sword technique, which I've trained for ten years!"

    k "One strike, one strike to end it all."

    k "Tsubame Gaeshi! (Swallow Reversal)"

    "The duel between two genders, two individuals, two differing ideologies began, a raging 
    passionate duel!"

    "Two enter the ring, but only one leaves."

    show felise blush closeeyed2:
        xalign 0.5
        yalign -0.05

    que "KYAAAAAH! HE'S SEXUALLY HARASSING ME!"

    hide felise blush closeeyed2

    crowd "Eww, gross!"

    crowd "Now we have a molester in the school? aAd it's that chuuni dude? Major molester bro!"

    "Yeah... forget the duel option."

    return

label Magic:

    show bg hallway
    with fade
    #TODO have the bgm fade out when the bell rings
    play music "!ubw.mp3" fadeout 1
    show felise blush closeeyed:
        xalign 0.5
        yalign -0.05

    "...Try casting a spell on her."

    k "I am the bone of my sword."

    k "Steel is my body, fire is my blood."

    k "I have created over a thousand blades."

    show felise happy:
        xalign 0.5
        yalign -0.05

    que "Hooh, so you too, are a wizard..."

    que "Very well then!"

    que "Reality be bent!"

    hide felise happy

    "As both (supposed) mages continue their chant, the true battle begins."

    k "Unknown to death, not known to life."

    k "I have created over a thousand blades."

    k "Yet these hands will hold nothing."

    que "Synapse Linkage, 100/% synchron!"

    que "Linkage Code QX5ABCD."

    que "Linkage Code Authorized."

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

    "Riight, I need it to do my homework at the cafeteria, no way I can borrow it to her."

    "Besides, I left all of my pencils in class so that's that, I couldn't lend it to her."
    return

label wallet:
    "This is my wallet, containing the money I need to buy melonpan and an iced tea."

    "Man, I want to eat kitsune udon though, the weather's getting hot here."

    "Doubt she needs me to lend her cash, considering im running low myself."
    return

label idcard: 
    "This is my ID card, nothing new here."

    "It shows my basic information."

    "My name is Kazuo Mizuhara, I am your average teenage boy, aged 17."

    "My house is on the northeast side of Tokyo, though I currently live in the school dorms with Hiroto."

    "I am not married, and am a student to this school."

    "I get home by 9 pm latest, unless I am doing some schoolwork with a friend."

    "I don't smoke, and I don't drink either."

    "I'm in bed by 12 am latest, and I try to get at least 7 hours of sleep every day."

    "After drinking milk and doing my stretches before going to bed, I often have no problems sleeping 
    till morning"

    "Just like a baby, I often wake up without fatigue or stress in the morning, only hatred for 
    humankind."

    "I was told I had no issues during the last health inspection."

    "I'm trying to say that I am a person who does not like to meddle with troublesome situations, 
    like the girl I met this morning,"

    "Which would cause me to lose sleep at night."

    "Although, if someone were to challenge me to a fight, I would win..."

    "(What am I even doing?)"
    return

label Friend:
    show hiroto frown:
        xalign 0.5
        yalign -0.05

    k "Hiroto, do something!"

    h "I think you should help her out, apologize to her."

    hide hiroto frown

    k "Tch, you're useless."
    return


label commonroute3:
    show bg battlefield1
    show felise cat happy:
        xalign 0.5
        yalign -0.05

    que "Fallen Angel, Azrael Deus Ex The Fifth."

    az "State your name, duelist, and we will fight an honorable duel!"

    k "I have no name. I let my blades do the talking."

    az "Ho! So you're approaching me? instead of running away from me, the angel of death, you're 
    approraching me?"

    k "Talk less, fight more!"

    hide felise cat happy

    "*CLANG!*"

    # TODO: Fix this line!
    "As 2 rulers clashed with an umbrella, she extends it, proving to be somewhat to have the image 
    of a large lance"

    show felise cat happy:
        xalign 0.5
        yalign -0.05

    k "What's your class, lancer?"

    az "I have no obligation to tell you! Hyah!"

    hide felise cat happy

    "After a series of blows, both of them were readying their ultimate attack, until..."

    show bg hallway
    with fade

    #TODO Music should end here

    "*ding* *dong*"

    "The school bell rings, signifying the end of the recess."

    show hiroto happy:
        xalign 0.5
        yalign -0.05

    h "I think it's about time we went back to class, we have a math test, you know."

    k "Not now hiroto! I'm in battle with the great azrail, the angel of death!"

    h "And I think you two are causing a scene."

    hide hiroto happy

    crowd "Major chuunibyou, bro!"

    crowd "Eww, cringe!"

    crowd "Hey, I've seen this guy before, he's the disgusting one from this morning!"

    show felise blush:
        xalign 0.5
        yalign -0.05

    k "Tch! We shall continue our battle later!"

    az "Fair, and by the way,"

    show felise happy:
        xalign 0.5
        yalign -0.05

    f "My human name is Felise, Felise Arrowheart from Class 3-A, so you know where to find me 
    for our next duel."

    k "Do remember, I always settle my scores."

    show felise smile closeeyed:
        xalign 0.5
        yalign -0.05

    f "I'm counting on it! And farewell!"

    f "MUAHAHAHAHAHAHA!"

    hide felise smile closeeyed

    k "Interesting character..."

    h "Let's get to class, we have a math test to do."

    k "Resolves."

    scene bg classroom
    with fade

    k "Man, that math test was hard!" 
    
    k "Hiroto, I'm going to the canteen, need anything?"

    show hiroto happy:
        xalign 0.5
        yalign -0.05

    h "I'll get the usual."

    k "Ocha and melonpan, gotcha, anything else you need?"

    h "I've heard rumours of a major cute girl who's always in the library, they say she has thick thighs,"

    h "And a really busty physique too!"

    hide hiroto happy

    h "Yeah, I'd pass on that last one..."

    scene bg hallway
    with fade

    k "Hmm, the library looks interesting..." 
    
    k "Maybe I'll stop by there, I still have time to kill after all."

    k "Not that I'm falling for such rumors of a girl with a nice physique."
   

    scene bg library
    with fade

    "I noticed a prim and proper girl sitting inside, seemingly enamored by the book she is reading."

    "I look closer and notice her prim slender figure and short smooth jet black hair, as if she is 
    the personification of Yamato Nadeshiko."

    "The more I look, the more I notice features that just seem to-"

    k "Hm...? Is.. Is that!?"

    k "STEEL BALL RUN!!!??"
  
    que "Hya!?"

    show sunyi suprised:
        xalign 0.5
        yalign -0.05

    que "W-Who??"

    k "Oh, sorry for surprising you. I was just interested in the book you were reading..." 

    "Uwaah... she must be the girl from hiroto's rumours."

    show sunyi suprised blush:
        xalign 0.5
        yalign -0.05

    que "!?"

    que "You know it!? It's one of my treasures!"

    que "The two main characters are a disgraced former executioner for a European government, and a 
        paraplegic former horse jockey celebrity. There are several themes in the story, the first of 
        which is the western theme demonstrated in the location of the story, 1890’s America. 
        The main method used to run in the race is on horseback and several characters are evocative 
        of the classic image of the American cowboy, straight down to the use of lassos and six-shooters..."
    # Another staple mode of transportation of young America is the train used by the wealthy runners of 
    # the Steel Ball Run and the President. The background and characters are very detailed, and the 
    # stylization of the characters are impressive. The characters are unique within the shonen/seinen 
    # genre at large and amongst each other."

    que "Ah!"

    que "Sorry..."

    k "Uhh..."

    "So she's also a jojo fan?"

    "(Ding dong)"

    que "Um, class is starting! Ex- Excuse me!"

    hide sunyi surprised blush

    k "Ah, she ran away, before I even got her name."

    "Interesting character, big boobs, glasses and thick tighs, man she must be at least A+ tier, 
    I'd go back and report to hiroto."

    scene bg classroom
    with fade

    k "Urgh, English, as if today wouldn't get more boring..."

    sc "Inspection! Hand over your bags nicely and we wouldn't hurt you!"

    k "Tch, it's that girl from this morning."

    show carmen frown:
        xalign 0.5
        yalign -0.05

    que "Alright You all, stand in front of the blackboard!"

    k "How bold of you to show to the student council today when you are late."

    que "Yuck, it's that guy from this morning."

    scene bg classroom
    with fade

    "Inspection ended swiftly... with only Hiroto getting his items confiscated."

    h "Damn that carmen, confiscating my Magic: The Gathering Deck, what does she have, 
    Mystic eyes of perception EX?"

    k "Nah, that's probably the work of an enemy stand."

    c "Or maybe, if you two idiots would stop bringing illegal items to the school,
    I wouldn't confiscate them."

    show carmen shout:
        xalign 0.5
        yalign -0.05

    c "I know you, Kazuo Mizuhara, the school's number 1 problem child."

    c "And his partner in crime, Hiroto Miyamoto. Do you two have anything to say for yourselves?"

    show carmen frown:
        xalign 0.5
        yalign -0.05

    k "I didn't bring anything to school today, and this is how you talk to me?"

    c "Powerless dogs only bark, but they too grovel at the sight of real power, 
    say I have a track record"

    c "Like the one time you went on a chuuni outburst a few weeks back, 
    I still have a list of your confiscated items."

    c "And i can't wait to spread the info via the PA system"

    k "Tch."

    h "Kazuo, let it off the hook, let her off this time."

    c "I'm glad, your friend seems to have a bit more common sense than you, not that he has any anyway."

    hide carmen frown

    k "Tch, I'll get her next time..."

    scene bg classroom
    with fade

    "*Homeroom Ends*"

    show hiroto happy:
        xalign 0.5
        yalign -0.05

    h "Kazuo, let's hit the dorms!"

    k "Denied, I have to go shopping for the weekly supplies, our fridge is running out of supplies, 
    and I don't think I can ask you for supplies anyways."

    show hiroto blush:
        xalign 0.5
        yalign -0.05

    h "eeeeh, but you always ask me for help whenever we buy groceries?"

    k "I never did, all you do is spend all the money on MTG cards and shounen jump manga, remember the first day we lived together?"

    h "Tch, that was because the new core set was out, you never give me another chance."

    k "Case and point, guilty as charged."

    show hiroto blush open:
        xalign 0.5
        yalign -0.05

    h "Objection! i would like to raise my case."

    show hiroto blush:
        xalign 0.5
        yalign -0.05
    
    k "Overruled, you have been charged guilty on a few accounts."

    k "Like the one time I fell sick, and you had to buy supplies, which resulted in 
    you buying convenience store food"

    k "And forgetting to microwave it, so I had to go to the cafeteria and use their microwave."

    k "And let's not forget that one time, you blew all our supply money on the arcade, 
    and forced us both to eat rice and soy sauce for the whole week!"

    show hiroto blush open:
        xalign 0.5
        yalign -0.05

    h "Ok! I get it, man, you never let me join you on a shopping trip."

    k "Maybe later, more importantly don't you have homework to tend to?"

    h "Shit! the math homework that's due tommorow! I'll go do it now!"

    hide hiroto blush open

    k "Well, there he goes."

    k "Time to go to the shopping district before it gets late."

    k "Or before hiroto starts cooking and almost burn down the dorm, like that one time we had 
    to relocate."

    scene bg street

    "As i walk down the street, i notice a newly built shopping district along the way."

    "And can't help but notice that quite a bit of students from our school go there to hang out."

    "And after hearing a few rumors at school, about the mall in said shopping district."

    "I decide to go in."

    scene bg mall 
    with fade

    crowd "*Gossip Gossip*"

    crowd "Chatter Chatter"

    "So this is the rumored mall, it has the standard store lineup."

    "With a maid cafe, and an arcade, with the retro games i've been dying to play since i moved here."

    k "Hmmmm"

    #TODO Make Multiple flag triggers possible.

    menu mallchoice:

        "Have fun at the arcade":
            jump arcade
        
        "Go check out the grocery store":
            jump groceries

        "Relax at the maid cafe":
            jump maidcafe

label arcade:
    # $ menu_flag1 = True
    scene bg mall
    with fade

    "Lorem ipsum"

    jump commonroute4

label groceries:
    # $ menu_flag2 = True
    scene bg mall
    with fade

    "Lorem ipsum"

    jump commonroute4

label maidcafe: #this will be the test for sunyi's route bg scene(since free assets have a maid bg.)
    # $ menu_flag3 = True
    scene bg mall
    with fade

    k "K, guess I have time to spare, and cash to blow, imma check the maid cafe"

    scene bg mall
    with fade

    "So this is the rumoured cafe, Cafe MorumoTea, or Cafe MT for short."

    "Heard it was popular amongst the otaku in our school for having beautiful maids whom are energetic and serve with love."

    "It doesn't hurt to check it out."

    scene bg cafe
    with fade
    "*Door Opening Sfx*"

    show sunyi maid1:
        xalign 0.5

    que "Welcome to our..."

    show sunyi maid2:
        xalign 0.5

    que "eep!"

    "*Glass dropping sfx*"

    show sunyi maid3:
        xalign 0.5

    "As i stood there dumbfounded at the display that this maid was making, i suddenly realize"

    "Isnt she. . ."

    "That girl from the library?!"

    show sunyi maid2:
        xalign 0.5

    que "W-W-WhaleCum to our..."

    hide sunyi maid2

    que "What's with all the commotion?!"

    show mg sigh:
        xalign 1.0
    show sunyi maid3:
        xalign 0
        yalign -0.05
    que "Care to explain what's going on?"

    que "Oh, a guest?"

    que "You, serve the other guests, i'll take care of this customer."

    hide sunyi maid3
    show mg happy:
        xalign 0.5

    que "Pardon me for my employee's mistake, my name is Henry Oswald, heir to the Oswald family."

    mg "I am the manager, and head barista of this establishment, do call me Manager, or Boss if you may."

    "Maybe i'll skip out on the last one."

    mg "Oh pardon me, do you mind if i led you to my favorite seat in this cafe? i would like to have a talk with you."

    k "Sure, i do not mind."

    hide mg happy

    scene bg cafe
    with fade

    show mg happy:
        xalign 0.5

    mg "My Apologies for the sudden talk, after all the commotion my employee has caused you."

    mg "However, i would like to address the case since you seem to be in the same school as our star maid, Sunyi."

    "So that's her name, i'd best keep that in mind."

    mg "I know that part-time jobs are illegal in the school where you come from, i would like to ask you that you keep her job a secret."

    k "And what's in it for me if i do?"

    show mg sigh:
        xalign 0.5
    mg "Look here, i'm requesting you as a former alumni of the school, that you keep her working life a secret."

    mg "I built this establishment as a working enviroment to those who have circumstances, and need to work here, like her."

    mg "Most of the maids here are part-timers, like her, and they also come from your school."

    k "And why are you asking me of this request?"

    show mg happy:
        xalign 0.5
    
    mg "Because she was blushing, that only probably means she knows you."

    "I do not know how this manager reasons with his employees, but sure, you do you i guess."

    mg "I mean, look at her, now, working here full of passion."

    hide mg happy
    
    scene bg smile glasses:
        yalign -0.03

    "As i averted my gaze, i saw a beautiful, and elegant woman."

    "Working as a maid, earnestly, elegantly, and passionately"

    s "Welcome back Master, may i take your order?"

    g1 "I would like to order the morumotea special please."

    s "One, morumo special! coming right up!"

    g2 "I'd like some alone time with you after work, if you get what i mean"

    scene bg frown glasses:
        yalign -0.03

    s "I'm terribly sorry but this is currently within work hours, can we discuss this at a more appropriate time?"

    k "Isn't she in deep trouble, shouldn't we go help her?"

    mg "Nah, give her some time, she'll handle em just fine."

    scene black
    with fade

    "The scene which unfolded was nothing short of what the manager told me."

    "She just talked to the guy as if it was a part of her everyday routine, even though clearly the guy had ulterior motives in mind"

    "Nothing short of the word elegant, crossed my mind, as there she stood, like a flower in a garden of weeds, doing her duty."

    scene bg cafe

    "Looks like i got worried for nothing."

    show mg happy:
        xalign 0.5

    mg "Hey, don't look so down, It's not like she dosent have her fair share of these kinds of situations."

    "Did the worry show on my face?"

    mg "Well, it's only natural to show concern for your schoolmate for undergoing these kinds of events, here a tea, it's on me today."

    "*gulps*"

    "It's suprisingly delicious"

    k "Not bad."

    mg "Glad you like it, it's the morumotea special."

    scene bg mall

    "After relaxing and talking to the manager, i continued on to buy my groceries"

    "And a few packs from the new cardstore"

    k "hmmm...still have enough money for a few cards along the way"

    jump commonroute4

label commonroute4:
    scene bg mall
    with fade

    "Eventually, i finished my groceries"

    scene bg room
    with fade
    
    #TODO Fix Flag Script, they would appear at diffrent times supposedly.    
    
    #if menu_flag1:
     #   k "Hooh, don't come crying to me when you need extra aracade money like yesterday"
      #  f "tch..."

    #else:
     #   k "..."

    #if menu_flag2:
     #   "So she does have a dere side, instead of constantly being tsun..."

    #else:
     #   ". . ."

    #if menu_flag3:
     #   k "Ey, i saw you at the maid cafe recently"

    
    #else:
     #   k ". . ."



    return    


    # This ends the game.

    return

