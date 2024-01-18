# The game starts here.

label start:

    scene bg room

    """Welcome to Binch Academy, the most prestigious school in all of Eorzea.
    You were just invited under the ‘Adventurers Needed’ scholarship, a full
    ride to the very school! 

    The only problem is that you're a transfer student that's started a week late! Luckily you've done all the research you needed to know what you want to accomplish! 

    You have three goals you want to achieve by the end of this school year...become the fabled
    Warrior of Light, the school president, and become the Warrior of Darkness.
    
    The Warrior of Darkness is achieved by being voted as the number one adventurer at the 
    Calamity Dance in one week.
    
    You need to find a hot date fast to qualify, so get going!"""

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
    show taka normal at right:
        zoom 0.5
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
    "You’ve finally arrived, and after turning in the proof that you've been accepted into the school,
    the bell rings and you realize you have no idea how to get to class."
    
    "You pass a few hallways, including the elective classrooms, but it’s clear
    you’re absolutely lost when you passed the same spooky hallway three times. 
    Where do you go now?"

    menu:
        "To the map on the wall.":
            "You take a look at the map, and quickly figure out where your classroom was and promptly made your way over."
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
    #maybe edit it so that you fall on your butt
    show bomee normal at right:
        zoom 0.5
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
                jump craftroomDay1
        "To the auditorium.":
                jump auditoriumDay1
label craftroomDay1:
    "You poke your head into the art room. There's only a single student in the
    room-in front of him is a miniature Carbuncle house model. He lifts his head
    when you take a step inside."
    scene artclass
    show jaja normal:
        zoom 0.5
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
    show taka normal:
        zoom 0.5
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
            #maybe elaborate more on this
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
    #Remember that Dino DLC goes here. 
    "Upon reaching the end of the hall you manage to find a place that looks like a library."
label libraryDay1:
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
            about the school, feel free to come back to the library.There's a lot to learn."
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
    n "Who are you."
    "It doesn't sound like a question, but you know it's not rhetorical. You take a deep breath as you try to shake the nerves. 
    First impressions are important and you can't really afford to flop this one."
    #change this to saying how you want to be nominated as the warrior of darkness and don't you forget it.
    me "I'm the new transfer student, [player_name]. I hope to get along with all of you!"
    #Maybe insert people snickering at this remark
    n "Oh. Everyone, you heard them. Just take a seat where one's available, but do try to hurry the lesson isn't over yet."
    "You choose to sit..."
    hide rook normal
    menu:
        "Next to the bespectacled girl at the front of class.":
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
                    """In complete contrast with her, she hands you her notebook so you can take a look at the notes you've already missed.
                    
                    With that you hurriedly take out a notebook to copy everything down she wrote and make note of her name at the top of the page.
                    
                    Weird how she wrote her name in the corner of this page in the  middle of her notebook, really makes you wonder what kind of person she is. At the very least you're thankful that it's legible and easy to take in.
                    
                    She returns her attention to the front of the class and continues to take notes deligently.
                    
                    Keeping up with this lecture is taking about all you've got, but that's to be expected from a top level school. You still can't believe the fact that you made it in. Even worse for some reason you made it in the middle of the school year which would just put you behind, 
                    but that's all the more reason for you to give it your all.

                    "In the midst of all this inner struggle you can't help but to feel a looming presence over your shoulder almost like someone's watching you but every time you surveyed your surroundings the feeling disappeared."""
                    hide suzu normal
                "Ignore her, she looks mean.":
                    """You turn away from her and her question to face the teacher. There's no point in giving a meanie Miqo'te the satisfaction of knowing she made you nervous.

                    After pulling out a notebook and pen you hurriedly try to keep up with what the teacher is saying. You should really learn his name after this since you probably need to ask for the start of this lesson. 
                    Still, keeping up with this lecture is taking about everything you've got but that's to be expected from a top level school. You still can't believe the fact that you made it in, especially since you were accepted in the middle of the school year
                    which would just put you behind, but that's all the more reason for you to give it your all!

                    Sucks that you weren't able to make a friend but there's plenty of opportunities to come, and I'm sure they'll be infinitely more pleasant than this one."""
        "At the corner seat by the window.":
            "Of course! This is where the main character should sit. People will be crawling to interact with me cause it's flowing with mystical energy."
            "You confidently strut over to your seat with your head held high and set up your battle station. Unfortunately, it seems that no one paid you any mind so you decide to suck up your disappointment and focus your attention
            to the teacher. It's disorienting coming in the middle of a lecture so you try your best to keep up with what he's saying and write down what seems important."

label lunchbreakDay1:
    #
label classroomPMDay1:
        scene classroom pm
        
        "Hours past as you go from lesson to lesson, an absolute slug in which time could not go any slower. It certainly feels like a prep school with the amount of work that was packed in. Considering this was your first day of class after transferring midyear, 
        you think you did fine! All this talk about UWU and what not confused you, isn't that just some weird internet thing?"
        "Welp, classes are over what do you do now? "
        menu:
            "Go home immediately":
                "Probably a good idea to get into a routine before I try something new. I'm still having some issues finding my way home and straying from school would only make that worse."
                jump street3Day1
            "Try to invite Suzu somewhere" if suzu_met==True:
                "You're new here and the best person to show you around would be your seatmate! Maybe they'll be willing
                to show you around if you ask nicely. It wouldn't hurt to give it a try."                
                me "Hey, [seat] you wanna go somewhere after class?" 
                if (seat == suzu):
                    show suzu normal at right:
                        zoom 0.5
                    if(suzu_love == 2):
                        "She doesn't look up at you but she takes a slight pause from putting away her stuff 
                        and continues until she finishes."
                        "She clicks her tongue and starts making her way out of classroom."
                        "WELL that was ru- Before you could finish that thought she suddenly speaks up."
                        suzu "Well are you coming or not?"
                        me "eh uh"
                        suzu "Hurry up or I'll leave you behind. Someone should show you around since you're new and all. 
                        Not that I want to or anything."
                        suzu "There's a nice place though I'd doubt you'd have any way of getting there. Just follow me and don't make too much noise."
                        jump roofDay1
                    else:
                        suzu "ew why would I want to hang out with you? Who even {i}are{/i} you? lmao"
                        "Yikes guess I'll just go home. She seems really mean. I don't know if I should keep talking to her or not."
                        #yikes alright guess I'll just go home
                        jump endDay1
            "Wander around to the field" if bomee_met == True:
               "Maybe I can try to find that person"
            "Blitzen" if blit_met == True:
              "stuff"
              
        #Visit one of the other places I've been to
                        
label roofDay1:
        scene black
        #makes sure to see that no teachers are watching where you two are going
        """She places a finger on her lips as she motions you to follow. Her eyes dart back and forth as she scours the route ahead for potential peepers.
        Any time you tried to ask her a question she immediately shut you up with a shush motion.

        You finally approach what seems to be the destination as you reach a dead end with a stairwell. With confidence, she strolls up as you hesitantly follow.
        At the top, she pulls a hairpin from the sleeve of her sweater and expertly manuevers it coaxing the lock open with several satisfying clicks.

        The door swings open and you're greeted by a rush of wind cutting across your skin as the sudden flash of light blinds you. 
        In your daze you feel a tug towards the light along with a soft thud of, presumably, the door closes behind you.
        This isn't your first time on a school rooftop, but there's just something about that fact that you're up here without permission that's just so exciting."""
        scene rooftop day
        show suzu normal at left:
            zoom 0.5
            linear 1.0 xzoom -1.0 yzoom 1.0
        suzu "This is my favorite part of the school. " 
        suzu "We're not really allowed to go up here but I'm planning on getting permission in the near future."
        suzu "Not that it concerns you I mean."
        suzu "What do you think about it?"
        show suzu determined at slightright:
        with move
        menu:
            "The view is absolutely amazing from here":
                $suzu_love +=1
                #good angles as it's quite wide and better than her room due to the limited angle
                                #It's so vast
                suzu """Well of course it is you don't have to tell me.
                With it's elevation and openess you can really. You can watch the sky  

                My favorite part is how private it feels, really separates you from everyone else.
                She walks toward the edge of the roof and reaches towards the sky
                Like I said I'm planning on gaining access to the rooftops and to do that I want to start an astronomy club.
                This is the perfect place to watch the stars
                The universe is so vast, yet here we are stuck on this rock. Someday I'll explore it."""
                "She lets out something like a dry laugh."
                suzu  "Unfortunately that dream is far away so I'll just settle for reading the stars and studying astrology for now..."
                #spreads her arms out far to simulate the vastness of space
                #maybe a special cg for this
                #New blood at the school so she gets embarassed because she overshared
                show suzu shocked:
                    linear 1.0 xzoom 1.0 yzoom 1.0
                "After stating that however, she stood still for just a moment before turning around slowly."
                suzu "B-BAKA!"      
                show suzu shocked at left
                "She runs away after screaming that strange word at you."
                hide suzu
            "This place is kind of mid":
                $suzu_love-=1
                suzu "..."
                suzu "Alright, that's fine forget that I even showed you this."
                "She storms off leaving you alone."
        "Guess you should head home before anyone catches you up here"
label endDay1:
        scene street
        with fade
        "Your first day has been a success! You've talked to some interesting students,
        learned a lot in your classes, and are one step closer to becoming the Warrior of
        Darkness!"

jump bedroomAMDay2
