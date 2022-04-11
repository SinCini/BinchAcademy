#k33ppr33pinpa!

# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define taka = Character("Taka", color = "#FF0000")
define rook = Character("Mr. Addock")#, color =)
define suzu = Character("Suzu", color = "#000000")
define lado = Character("Lado", color = "#FF8C00")
define blit = Character("Blit", color = "#FFFFFF")
define dino = Character("Dino", color = "#B22222")
define bomee = Character("Bomee", color = "#8A2BE2")
define jaja = Character("Blitzen", color="#00FFFF" )
#define silver = Character("Silver")
define izzy = Character("Izzy")
define me = Character("Me")
define n = Character("????")

define day = 1
# Checkers if Events happen
#default late = True
default composure = False
define seat = rook

default taka_met = False
default suzu_met = False
default lado_met = False
default blit_met = False
default dino_met = False
default bomee_met = False
default jaja_met = False

define people_met = 0

# Affection Begin
define taka_love = 0
define suzu_love = 0
define lado_love = 0
define blit_love = 0
define dino_love = 0
define bomee_love = 0
define jaja_love = 0
define silver_love = 0

# The game starts here.

label start:

    scene bg room

    "Welcome to Binch Academy, the most prestigious school in all of Eorzea.
    You were just invited under the ‘Adventurers Needed’ scholarship, a full
    ride to the very school!"

    "You have three goals you want to achieve by the end of this school year...become the fabled
    Warrior of Light, the school president, and become the Warrior of Darkness."
    
    "The Warrior of Darkness is achieved by being voted as the number one adventurer at the 
    Calamity Dance in one week."
    
    "You need to find a hot date fast to qualify, so get going!"

    scene black
    with fade

    "You were just accepted and today’s your first day of class."

    $ player_name = renpy.input("Wait a minute...Who ARE you?") 

    $ player_name = player_name.strip() or "Joey"

    scene bedroom
    with fade

    menu:
        "You..."

        "Get to class, obviously!":
            $late = False
            "It’s your first day, and you need to set a good first impression!
            You jump up, do a few good stretches, and head to school."
            jump streetDay1

        "Sleep in a little more.":
            "Sure, it’s Binch Academy. But prestige means nothing if you
            stayed up last night playing MMORPGs, and you’re super tired...
            so you set an alarm to go off 15 minutes later."

            scene bedroom
            with fade

            "Except!"
            "You slept through it!"
            "You run to school, toast in mouth and papers flying out of your
            bag."

            jump hallwayDay1

        "Skip class.":
            "Sure, it’s Binch Academy. But prestige means nothing if you stayed
            up last night playing MMORPGs, and you’re super tired. Maybe
            tomorrow they’ll consider changing what time first period starts."
            
            scene black
            with fade
            
            "Unfortunately skipping class on the first day showed that you weren't commited to the school
            and you were expelled. How are you going
            to explain this to your mom?!"
            "{b}Ending 1: YOU DROPPED OUT!.{/b}"
            return


label streetDay1:
    scene street
    with fade
    
    "On your way, you hear a wonderful voice belting out tunes like there’s
    no tomorrow. Rounding the corner you spot a red-haired Miqo’te dancing around and
    singing like a prince out of a fairy tale."
    show taka normal at right
    menu:
        "Keep walking and appreciate his voice from a distance.":
            "Just as you turn a corner, someone grabs you! You're pulled into
            a dark street."
            jump alleywayDay1

        "Compliment them.":
            me "Wow, you're amazing!"
            $taka_met = True
            $taka_love +=1

            "He stop walking and turn around to look at you. The looks
            definitely match the voice, and you feel yourself blush pink when
            they give you a confident grin."

            n "Why, thank you! I’m practicing for the part of Romeo, after
            all. May I?"

            "He holds out a hand for you to take."

    menu:
            "Take it, silly!":
                "You take his offered hand."
                $taka_love +=1
                taka "My name's Taka. Taka Ari."
                me "I'm [player_name]."
                "He walks with you to school, and you make small talk before
                you have to separate so you can stop by the office and turn
                in your invitation."
                jump hallwayDay1

            "Too much pressure! Run!":
                "You're not taking any chances with perfect strangers, so you
            book it and run past him towards school."
                $taka_love -=1

                jump hallwayDay1

label alleywayDay1:
    scene alleyway
    show izzy normal
    n "hey"
    "You scream, but thanks to their hand covering your mouth you barely make
    a noise."
    n "be quiet already i need to tell you something"
    menu:
        "Fight!":
            "You elbow them in the gut, and it's enough of a move for them to
            let go! Book it and run to class!"
            jump hallwayDay1

        "Keep screaming!":
            n "listen you need to-stop screaming-you cant become the warrior of
            darkness. thats my spot. just letting you kno"
            "They shove you back out into the street."
            scene street
            with fade
            "When you turn around, you see neither scale nor tail of the Au'ra.
            Good for you, because you're about to be late!"
            jump hallwayDay1



label hallwayDay1:
    scene hallway day
    with fade
    "You’ve finally arrived, and after turning in your invitation to show you
    accept the bell rings and you realize you have no idea how to get to class."
    "You pass a few hallways, including the elective classrooms, but it’s clear
    you’re absolutely lost when you passed the same spooky hallway three times. 
    Where do you go now?"

    menu:
        "To the map on the wall.":
            jump classroomDay1

        "Towards the elective hallways.":
            jump electivesDay1

        "Towards the spooky hallways.":
            jump spookyDay1

        "Keep walking in circles.":
            jump hallway2Day1

label hallway2Day1:
    "If you keep walking eventually you'll get there right?? As you round the corner, you
    knock right into a black-haired Miqo'te!"
    show bomee normal at right:
        zoom 0.2
    n "Oh no! I'm so sorry, are you okay?"
    "She's gorgeous."
    menu:
        "Apologize.":
            $bomee_love +=1
            me "I'm sorry, too. I'm fine. Did you get hurt?"
            "She grimaces, but shakes her head."
            n "I'll be okay."
            "She looks you up and down and her ears perk up."
            show bomee excite
            n"Are you a new student here? Oh my gosh, are you lost?!"
            menu:
                "Yeah, I am. Can you help me?":
                    $bomee_love +=1
                    bomee "Of course I'll help! It's the least I can do. My name's
                    Bomee Bell."
                    "She shows you the way to class, asking where you're from
                    and if you're excited to be a part of this school."
                    bomee "I really, really hope you like it here! I'll see you
                    around, 'kay?"
                    jump classroomDay1

                "Run away!":
                    jump runawayDay1

        "Run, she's too hot!":
            jump runawayDay1

label electivesDay1:
    scene elective
    "There are two open doors-one leads to the art room, and the other leads to the auditorium. Which do you pick?"
    menu:
        "To the art room.":
                jump artroomDay1
        "To the auditorium.":
                jump auditoriumDay1
label artroomDay1:
    "You poke your head into the art room. There's only a single student in the
    room-in front of him is a miniature Carbuncle house model. He lifts his head
    when you take a step inside."
    scene artclass
    show jaja regular
    with fade
    n "Hey. I don't recognize you. Are you new here?"
    menu:
        "Lie!":
            me "Uh...no."
            jump runawayDay1
        "Be honest.":
            me "Yeah, I am. Can you help me get to my class?"
            "He frowns, but puts down the jar of paint he was holding."
            n "I guess so. Are you a first year?"
            scene hallway
            with fade
            "You introduce yourself to him as you walk, and he takes a look at your
            schedule before nodding in approval at seeing the teacher's name."
            n "Mr. Addock's pretty chill. As long as you don't get on his bad side,
            that is."
            "You gulp and nod."
            me "Thanks for telling me."
            n "Anytime."
            menu:
                "Walk in silence the rest of the way.":
                    "He shows you the way to class, and he doesn't say anything when
                    you get there."
                    jump classroomDay1
                "Ask about the house model he was working on.":
                    $jaja_love +=1
                    me "So...what was that house you were building?"
                    n "Oh. I'm one of the school's best crafters. This is how we get
                    most companies interested in funding our school."
                    me "Companies?"
                    n "Are you smooth brained? This school's funded by the three Grand
                    Companies. They help us with school events like the Calamity
                    Dance."
                    "You two finally arrive in front of the classroom doors."
                    n "Try not to get lost again. It's a big school."
                    menu:
                        "Ask for his name.":
                            $jaja_love +=1
                            jaja "Oh. It's Jajapoki Rarapoki. You'll see it again. I'm
                            running for Warrior of Darkness. You should get going,
                            you're already super late."
                            jump classroomDay1
                        "Get to class!":
                            jump classroomDay1

label auditoriumDay1:
    "You head to the auditorium."
    n "Oh, hello."
    menu:
        "You know that voice!" if taka_love ==2:
            jump recognitionDay1

        "A student? Run!":
            "You can't get in trouble for snooping! You run and eventually find
            your way to the classroom."
            jump runawayDay1
label recognitionDay1:
    scene auditorium
    show taka normal
    menu:
        "Please help! I'm lost!":
            $taka_love +=2
            "Taka smiles and offers you his hand again."
            taka "Allow me."
            "As you walk, he speaks up again."
            taka "I thought you were new. I saw the invitation you were holding on
            our way to school. Welcome!"
            "Taka walks you all the way to your class, discussing the school
            dance-that he's also running for!-and how much fun you'll have in your first semester."
            taka "Here you are."
            taka "If you need anything else, I'll always be happy to come to your rescue."
            "He leaves you standing outside the classroom with a bright pink blush
            on your cheeks."
            jump classroomDay1
        "Uh...wrong room, sorry.":
            jump runawayDay1


label spookyDay1:
    "You decide to keep walking down the spooky hallway you earlier, if only
    because you're a little curious."
    menu:
        "Keep walking.":
            scene spooky
            with fade
            show dino normal
            n "Yo'. You're in the wrong hallway, kid."
            "There's a rugged looking Miqo'te eyeing you with what looks like a
            cigarette in her mouth. She screams of coolness, and looks a little
            surprised to see you standing in front of her."
            menu:
                "S-sorry! I'll go!":
                    jump runawayDay1
                "S-sorry! Please don't kill me!":
                    $dino_love +=1
                    n "Kill?"
                    "Her eyes go wide and then she bursts into laughter."
                    n "Haha! You're pretty funny. I like that. What are you doing
                    here, though?"
                    me "I'm [player_name]. I think I'm lost."
                    "She stares you down, looking very punk-rock and pretty and
                    scary, and then stands up, walking closer..."
                    "And past you."
                    n "Come on, kid. I'll help you out, but you  owe me one."
                    "She helps you out more than you expect, but you're mostly
                    too nervous to talk to her otherwise. She seems nice for
                    a school gangster, though."
                    n "I'll see you around again, okay? Good luck in class."
                    jump classroomDay1

        "Peek into the library to get help.":
            scene library
            
            show blitzen normal:
                        zoom 0.5
            "Instead of finding a librarian like you were expecting, there's a
            student Au'ra sitting at the computer desk, fully invested in the
            book he's reading."
            "He doesn't even notice you until you walk up to the desk and clear
            your throat."
            $blit_love +=1
            n "Oh, hey. Can I help you find something?"
            menu:
                "The way to my classroom!":
                    "He closes his book and tosses it behind him."
                    n "Sure. Are you a first year student?"
                    "That was a lot easier done than said."
                    "You make polite conversation with him as he walks you to
                    the proper wing of class, and he introduces himself as
                    Blitzen Bell."
                    $blit_love +=1
                    "When you get to the door he speaks up again."
                    blit "If you ever need any help or want some more information
                    about the school, feel free to come back to the library.
                    There's a lot to learn."
                    "Blitzen seems nice, and now you know someone who's happy
                    to help you out."
                    hide blitzen normal
                    jump classroomDay1
                "Not really.":
                    hide blitzen normal
                    jump runawayDay1


label runawayDay1:
    scene black
    "You're too scared to talk to the upperclassman, so instead you sprint away
    as fast as you can. Eventually you find the right door to your classroom."
    jump classroomDay1

label classroomDay1:
    scene classroom day
    show rook normal
    "You've finally arrived! The whole class turns to look at you when you walk in,
    including the teacher, who's wearing... a bird mask?"
    rook "Who are you."
    "It doesn't sound like a question, but you know it's not rhetorical."
    me "I'm the new transfer student, [player_name]."
    rook "Oh. Everyone, you heard them. Just take a seat where one's available."
    "You choose to sit next to..."
    hide rook normal
    menu:
        "The bespectacled girl at the front of class.":
            $seat = suzu
            $suzu_met = True
            show suzu normal at right:
                zoom 0.5
            "As soon as you sit down, the girl gives you a deadpan look over the
            top of her glasses. The expression says-"
            n "Really?"
            "No, she's actually saying it, too."
            menu:
                "Greet her":
                    $suzu_love +=2
                    me "Hi. Did I miss anything important?"
                    suzu  "..."
                    suzu "...not really."
                    "Even though she says it, however, she hands you her notebook so
                    you can take a look at the notes you've already missed."
                    "With that you hurriedly copy everything down she wrote 
                    and make note of her name at the top of the page."
                    "The rest of the class goes on without anything special happening."
                "Ignore her, she looks mean.":
                    "You turn away from her and her question to face Mr. Addock, the
                    teacher. There's no point in giving a meanie Miqo'te the
                    satisfaction of knowing they've made you nervous."
        "The Miqo'te in the back row.":
            $seat = lado
            show lado normal
            "As soon as you move to the back of the classroom, you see the Miqo'te's
            eyes jump over to you from the drawing in front of him before he goes
            back to his business."
            "As Mr. Addock keeps teaching, you watch him sketch out a familiar
            character. They're from your favorite MMORPG, Discord!"
            menu:
                "Comment on it.":
                    $lado_love += 2
                    me "I love that game."
                    "He looks every bit like a cat in water, so you offer a question
                    for conversation."
                    me "What server are you on?"
                    n "Uh...Bangers."
                    "Cool! It's a server in your region, at least."
                    n "What about you?"
                    "You two talk back and forth about Discord for the rest of class
                    to your joy, and you catch his name through seeing it on the top
                    of his paper."
                    "By the end of the day you can safely say you've found yourself
                    a new friend and potential raid partner."
                "Ignore him.":
                    "You're not really in the mood for conversation when you've
                    already showed up late to class, so you just focus on Mr. Addock's
                    teachings until the end."
label classroomPMDay1:
        scene classroom pm
        "Classes are over what do you do now? "
        menu:
            "Go home immediately":
                jump street3Day1
            "Try to invite your seatmate somewhere":
                "Hey, [seat] you wanna go somewhere after class?" 
                if (seat == suzu):
                    if(suzu_love >= 2):
                        suzu "Well you {i}are{/i} new, I {i}guess{/i} you need someone to show you around. Not that I want to or anything."
                        suzu "I've got a nice spot I can show you. Just follow me"
                        jump roofDay1
                    else:
                        suzu "ew why would I want to hang out with you? Who even {i}are{/i} you? lmao"
                        
label roofDay1:
        scene black
        "She leads you over a staircase near the back of the school and after fiddling with the door at the top
        you make it to the roof."
        scene rooftop day
        show suzu normal at left:
            zoom 0.5
        suzu "This is my favorite part of the school. " 
        suzu "We're not really allowed to go up here but I'm planning on changing that."
        suzu "Not that it concerns you I mean."
        
        "She walks towards the edge of the roof"
        menu:
            "The view is absolutely amazing from here":
                $suzu_love +=1
                suzu "well of course it is you don't have to tell me"
            "This place is kind of mid":
                suzu "..."
                
        suzu "B-BAKA!"
        "She runs away after screaming that strange word at you."
        "Guess you should head home before anyone catches you up here"
label street3Day1:
        scene street
        with fade
        "Your first day has been a success! You've talked to some interesting students,
        learned a lot in your classes, and are one step closer to becoming the Warrior of
        Darkness!"
label bedroomPMDay1:
        scene bedroom
        with fade
        "After getting done with your homework for the day you go back  "
        me "Wow."
        me "Today was amazing!"
        menu:
            "Better get some shut-eye for tomorrow":
                "Sleeping early will make it easier to wake up tomorrow"
                jump bedroomAMDay2
            "Time to knockout a few dailies out before tomorrow":
                "It wouldn't hurt to play a bit of Discord before school tomorrow. You won't stay up too late right?"
                jump bedroomAMDay2






label bedroomAMDay2:
    scene bedroom
    with fade
    "You wake up."
    "It's Tuesday. You're a little tired, but there's no time to waste!"
    menu:
        "Go to school early." if (taka_love ==2):
            "if you go early you might see that redhead again"
            jump streetDay2
        "Sleep in a little longer.":
            "It wouldn't hurt to get a few more moments of shut eye"
            jump classroomDay2

label streetDay2:
    jump classroomDay2

label classroomDay2:
    scene classroom day
    "You arrive in class and take your usual seat."
    if(seat == lado and lado_love >= 2):
        lado "Oh, hey."
        "They seems happy to see you."
        lado "You ready for today?"
        "Your eyes widen."
        me"No? What’s going on?"
        lado "It’s club sign-ups today. Mr. Addock will probably explain it."
    if(seat == suzu):
        "She doesn’t even look in your direction."
        "Greet her?"
        menu:
            "No":
                "You turn your attention to the front of the class to wait for Mr. Addock to come in."
            "Yes":
                "Good morning."
                "She hums, staring straight ahead at the board, but at last you hear her speak."
                suzu "Morning."
                "You’re happy to see she isn’t going out of her way to ignore you, at least."
                suzu "Club sign-ups are today."
                me "Eh?!"
                "She finally looks to you."
                suzu "Yeah. You didn’t know?"
                me "Who announces this stuff, anyways?!"
    "Mr. Addock enters the class just then."
    rook "So. Club sign-ups are today."
    "You’ve been waiting for this! The only thing more exciting than the school dances were the school clubs. There were so many, how were you going to decide?!"
    rook "There’s a list of clubs posted outside in the hallway. Take a look and decide after class."
    
    if (seat == suzu):
        if (suzu_love==3):
            "After class, you step into the hallway. Before you can leave, though, someone clears their throat."
            suzu "Are...are you interested in joining a club?"
            me "Oh, yeah, I hope so."
            "She looked nervous."
            suzu "Well. I’m just saying-no, I’m not asking-I’m starting up an astronomy club. We’re looking for members."
            me "Wow, that sounds like fun!"
            me "Can I join?"
        if (suzu_love==-1):
            suzu "Oh. Of course. I mean I wasn’t saying you could join or anything like that."

label end:
return


label classroomDay3:








