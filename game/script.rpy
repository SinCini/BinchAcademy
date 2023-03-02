#k33ppr33pinpa!

# The script of the game goes in this file.
# Declare characters used by this game. The color argument colorizes the
# name of the character.
#classes
define taka = Character("Taka", color = "#FF0000")
define rook = Character("Mr. Addock")#, color =)
define suzu = Character("Suzu", color = "#00FF00")
define blit = Character("Blit", color = "#FFFFFF")
define dino = Character("Dino", color = "#B22222")
define bomee = Character("Bomee", color = "#8A2BE2")
define jaja = Character("Blitzen", color="#00FFFF" )
define silver = Character("Silver")
define izzy = Character("Izzy")
define me = Character("Me")
define n = Character("????")

define day = 1
#Club stuff for now
define AstronomyClub = False
define ClubMet = False
# Checkers if Events happen
#default late = True
default composure = False
define seat = rook
#met Conditions
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

#Transform things
transform slightright:
    xalign 0.75
    yalign 1.0
transform slightleft:
    xalign 0.25
    yalign 1.0

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
                jump artroomDay1
        "To the auditorium.":
                jump auditoriumDay1
label artroomDay1:
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
            jump libraryDay1
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
    me "I'm the new transfer student, [player_name]. I hope to get along with all of you!"
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
                    "Even though she says it, however, she hands you her notebook so
                    you can take a look at the notes you've already missed."
                    "With that you hurriedly take out a notebook to copy everything down she wrote and make note of her name at the top of the page."
                    "Weird how she wrote her name in the corner of this page in the  middle of her notebook though, really makes you wonder what kind of person she is. 
                    At the very least you're thankful that it's legible and easy to take in." 
                    "She returns her attention to the front of the class and continues to take notes deligently."
                    "Keeping up with this lecture is taking about all you've got, but that's to be expected from a top level school. You still can't believe the fact that you made it in. 
                    Even worse for some reason you made it in the middle of the school year which would just put you behind, but that's all the more reason for you to give it your all."
                    "In the midst of all this inner struggle you can't help but to feel a looming presence over your shoulder almost like someone's watching you but every time you look around it disappears."
                    hide suzu normal
                "Ignore her, she looks mean.":
                    "You turn away from her and her question to face the teacher. There's no point in giving a meanie Miqo'te the
                    satisfaction of knowing they've made you nervous."
                    "After pulling out a notebook and pen you hurriedly try to keep up with what the teacher is saying. You should really learn his name after this since you probably need to ask for the start of this lesson. 
                    Still, keeping up with this lecture is taking about everything you've got but that's to be expected from a top level school. You still can't believe the fact that you made it in, especially since you were accepted in the middle of the school year
                    which would just put you behind, but that's all the more reason for you to give it your all!"
                    "Sucks that you weren't able to make a friend but there's plenty of opportunities to come, and I'm sure they'll be infinitely more pleasant than this one."
        "At the corner seat by the window.":
            "Of course! This is where the main character should sit. People will be crawling to interact with me cause it's flowing with mystical energy."
            "You confidently strut over to your seat with your head held high and set up your battle station. Unfortunately, it seems that no one paid you any mind so you decide to suck up your disappointment and focus your attention
            to the teacher. It's disorienting coming in the middle of a lecture so you try your best to keep up with what he's saying and write down what seems important."
            "It seems like no one really has an interest in you in class so you will probably need to spread your wings elsewhere to fulfill your goal."
    "Considering this was your first day of class after transferring midyear, you think you did fine! All this talk about UWU
    and what not confused you, isn't that just some weird internet thing?"
    "Regardless, you followed it as best you could and wrote down everything that you thought was important."
label classroomPMDay1:
        scene classroom pm
        "Hours past as you go from lesson to lesson, an absolute slug in which time could not go any slower. It certainly feels like a prep school with the amount of work that was packed in. "
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
                        jump street3Day1
            "Wander around to the field" if bomee_met == True:
               "Maybe I can try to find that person"
            "Blitzen" if blit_met == True:
              "stuff"
              
        #Visit one of the other places I've been to
                        
label roofDay1:
        scene black
        #makes sure to see that no teachers are watching where you two are going
        "She places a finger on her lips as she motions you to follow. Her eyes dart back and forth as she scours the route ahead for potential peepers."
        "Any time you tried to ask her a question she immediately shut you up with a shush motion, but you finally approach what seems to be the
        destination as you reach a dead end with a stairwell."
        "With confidence, she strolls up as you hesitantly follow."
        "At the top, she expertly manuevers a hairpin coaxing the door open, revealing the roof."
        scene rooftop day
        show suzu normal at left:
            zoom 0.5
            linear 1.0 xzoom -1.0 yzoom 1.0
        suzu "This is my favorite part of the school. " 
        suzu "We're not really allowed to go up here but I'm planning on changing that."
        suzu "Not that it concerns you I mean."
        show suzu determined at slightright:
        with move
        menu:
            "The view is absolutely amazing from here":
                $suzu_love +=1
                #good angles as it's quite wide and better than her room due to the limited angle
                suzu "Well of course it is you don't have to tell me."
                #It's so vast
                suzu "My favorite part is how private it feels, really separates you from everyone else."
                "She walks toward the edge of the roof and reaches towards the sky"
                suzu "Like I said I'm planning on gaining access to the rooftops and to do that I want to start an astronomy club."
                suzu "This is the perfect place to watch the stars"
                suzu "The universe is so vast, yet here we are stuck on this rock. Someday I'll explore it."
                "She lets out something like a dry laugh."
                suzu "Unfortunately that dream is far away so I'll just settle for reading the stars and studying astrology for now..."
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
                suzu "alright, that's fine forget that I even showed you this"
                "She storms off leaving you alone"
                #upset that this bitch didn't think this place is great 
                #gets more upset at their lack of appreciation for spots like thsi
                #proceeds to just storm
        "Guess you should head home before anyone catches you up here"
label street3Day1:
        scene street
        with fade
        "Your first day has been a success! You've talked to some interesting students,
        learned a lot in your classes, and are one step closer to becoming the Warrior of
        Darkness!"

label bedroomAMDay2:
    scene bedroom
    with fade
    "You wake up."
    "It's Tuesday. You're a little tired, but there's no time to waste!"
    menu:
        "Go to school early." if (taka_met ==True):
            "if you go early you might see that redhead again"
            jump streetDay2
        "Sleep in a little longer.":
            "It wouldn't hurt to get a few more moments of shut eye in order to "
            jump classroomDay2

label streetDay2:
    jump classroomDay2

label classroomDay2:
    scene classroom day
    "You arrive in class and go straight to your seat."
    if(seat == suzu):
        "She doesn’t even look in your direction."
        "Greet her?"
        menu:
            "No":
                "If she isn't going to look your way then there's no reason for you to initiate anything with this meanie. You begin setting up your workspace and
                turn your attention to the front of the class to wait for Mr. Addock to come in."
            "Yes":
                me "Good morning."
                #no humming just silent and you wonder if what happened yesterday inspired her not to talk to you
                "She hums, staring straight ahead at the board, but at last you hear her speak."
                suzu "Morning."
                "You’re happy to see that she isn’t going out of her way to ignore you at least."
                suzu "Club sign-ups are today."
                me "Eh?!"
                "She finally looks to you."
                suzu "Yeah. You didn’t know?"
                me "Who announces this stuff, anyways?!"
                "Mr. Addock enters the class just then."
                
    rook "So. Club sign-ups are today."
    "You’ve been waiting for this! The only thing more exciting than the school dances were the school clubs. 
    There were so many, how were you going to decide?! Would you even find something that you're passionate about?"
    rook "There’s a list of clubs posted outside in the hallway. Take a look and decide after class. 
    Don't let your excitement distract you from my lesson."
    
label classroomPMDay2:
    "Another boring day of classes go by, though you were tripped up when Mr. Addock asked a question about 
    how properly pass nisis."
    "It seems pretty complicated and you wonder to yourself when you'd use this in the real world"
    "Time to take a look at what clubs are available." 
    if (seat == suzu):
        "You step into the hallway, but before you get out the door, you hear someone clear their throat."
        if (suzu_love==3):
            n  "Hey, are...are you interested in joining a club?"
            "you turn around as you give a response"
            me "Of course! it's a great oppotunity to meet people and find people with similar passions!"
            show suzu normal at left:
                zoom 0.5
            "She looked nervous."
            suzu "Well. uhh remember how I said I was trying to start a club...."
            me "yea I think I recall something like that on the roof among other things"
            "In response to that comment she lets out a sudden cough. It's very brief but she managed to compose herself"
            suzu "Anyways I was wondering if you'd maybe I mean I don't know possibly join my club?"
            suzu "We just need one more member to make it official."
            menu:
                "I would love to join":
                    $AstronomyClub = True
                    "gives some sort of retort about joining but still gives you the sheet to sign your name"
                    "adds name to a petition happily skips along to turn in club submission"
                "Sorry I've got something else in mind":
                    show suzu dejected
                    suzu "oh I see..."
                    suzu "uh don't worry about it then"
        else:
            n "Hey"
            "You hear a very familiar voice calling out to you so you turn around to face them."
            "Suzu was a lot closer than you expected so you take a couple of steps back."
            suzu "I'm starting an astronomy club just fyi."
            menu:
                "Really? that sounds so cool can I join?":
                    #suzu smug
                    suzu "Oh. Of course. I mean I wasn’t saying you could join or anything like that."
                    suzu "I was just letting you know."
                "That's neat. What's that gotta do with me?":
                    suzu "..."
                    
label classroomDay3:
    if(seat == suzu):
        if(AstronomyClub == true):
                "As you approach your seat you hear Suzu humming to herself."
                suzu "Good morning [player_name]~~"
                "You're shocked that she greeted you considering how she's acted the last couple of days."
                me "Are you alright?"
                suzu "Yea why wouldn't I be?"
                me "No reason"
                "You think to yourself that it probably would be good idea not to elaborate."
                suzu "Anyways I better see you at the club room after class today. Convieniently it's the classroom 
                just by the stairwell. We're celebrating the approval of our club!"
                suzu "We don't exactly have a budget yet buuuut we're gonna do what we can."
                suzu "I know you're new so you won't know anyone there, but as the club president I'll introduce you to everyone. 
                They're all pretty nice!"
                
        else:
                "You head straight to your seat."
                "Suzu seems dejected."
                ""
    
    "Today's lessons seem to be focused on party etiquette as well as the roles that each member played in a party and how it affects the others.
    Mr Addock expressed the importance of every part of a group contributing to the party and those that don't do so are deemed failures in society."
    "It seems like a pretty extreme perspective but this is a prestigious school so you won't question it for now."
    if(seat == suzu):
        "In the midst of all this, you can't help but look in Suzu's direction every time she answers a question. You didn't really notice it the first day since you were so tense, 
        but she seems to always be the first one to raise her hands to try to do so. Her disappointment is visible when she isn't chosen."
        
 
label classroomPMDay3:
    "Another day of class ends as you manage to avoid being called upon in class. Maybe he got the message that you're still adapting to this
    new curriculum."
    menu: 
        "Head over to the clubroom." if(AstronomyClub== True):
            "You head over to the clubroom at the request of Suzu."
            $club_met = True
            "Probably a good idea cause she'd give you grief the next day if you didn't."
            jump astronomyRoomDay3
        "Go Home":
            if(AstronomyClub == True):
                "Suzu did say to go to the club meeting, but you'd rather just go home and study. It's not like you have any obligation towards her or anything"
            else:
                "You go home."
                jump streetPMDay3
            
label streetPMDay3:
        "You walk home nothing eventful happens"
label astronomyRoomDay3:
    "You arrive in front of the club room and put your hand on the door to open it. Your hands quiver as you start to get cold feet so you try to turn around."
    "Just as you do you feel a set of hands grab onto you, open the door and shove you into the room." 
    #suzu comes from behind you and basically pushes you into the room
    suzu "Listen up everyone, this is [player_name]"
    suzu "These are going to be your fellow clubmates from now on so make nice."
    suzu "With that we have our final member so we can start! Naturally as club president I have a speech to make to celebrate the founding of this soon-to-be illustrious club"  
    suzu "we stand as the astronomy club to find the stars and go further beyond."
    #speech stuff
    "After the speech everyone gave an obligatory applause but everyone else certainly didn't share the same energy as Suzu did."
    "With that you've been forced to socialize with a bunch of randos. It's great that you're potentially making friends but you still feel lke you're being put out of your comfort zone."
    "Everyone here seems quite nice and were quick to talk to a newbie."  
    "They joked around about getting roped into joining this club and they send their condolences as they assume you're in a similar position."
    "You don't really affirm or deny their suspicions but you imagine that they can read it in your expression."
    "Still, it's free food so you might as well try to enjoy yourself."
    
label entranceDay4:
    if(suzu_love >3):
        "Approaching the entrance of the school you notice that Suzu is carrying a big box by herself to the school."
        "She seems to be struggling a bit since the box looks longer than she is tall. You should probably try to give her a hand."
        menu: 
            "Help":
                "You rush over to her side and greet her"
                me "Good morning! You need a hand with that?"
                "She slightly jumps at your presence like she wasn't expecting anyone to reach out to help her."
                suzu ""
            "Don't Help":
                "You leisurely make your way through the entrance hoping to not catch her attention and make your way in. Luckily, she doesn't seem to notice under the large load."
                "Shortly after arriving in the classroom ."
                #tired from carrying the telescope by herself 
                #more down than usual as it was a depressing experiencing lugging that thing by herself
                #not apparent but her pressure makes it hard for others to approach her
                jump classroomDay4
                
            
        #when you guys manage to get to the clubroom you help her unbox it and it's a very expensive telescope that 
        #she seems to have brought from home
        #
                
label classroomDay4:
    #Split PE teacher
    "Today's curriculum seems to be PE. It would make sense that a warrior of light in training would need to be physically able in addition to mentally sharp.
    Unfortunately due to your gamer status, you dread this coming event."
    if(seatmate== suzu):
        show suzu gym smug at right:
                zoom 0.5
        "You look to your seatmate in hopes of having someone to share this struggle with."
        "Unfortunately that doesn't seem to be the case as the bespectacled bookworm doesn't seem out of her element in the slightest. She's even doing stretches!!"
        "She's emmiting a strange pressure so you find it difficult to even approach her in this state."
        "Track is the first activity and as soon as the signal was given... bang! she bolted forward like a bullet absolutely decimating the competition and having them eat her dust. To further this fact she took a victory lap just to show off."
        me "That was pretty incredible, what did you did out there. No one else even stood a chance."
        suzu "Well, it was only natural. I {i}am{/i} a student athlete after all. This is the bare minimum necessary to hold that title."
        me ""
        suzu ""
        #somethign about track and Suzu absolutely decimating the other contenders
        #you comment to her and she becomes smug at her accomplishment that was "only natural for her"
        #continues to excel in all the other stuff and calls herself a "student athelete" and when prompted about what sports she participates in
        #she doesn't acknowledge it.
    else:
        "Welp it's a little too late to complain now. You just gotta try your best."
    #your turn to go up 2 options go all out or take it easy
    menu:
        "Take it easy":
            "It's not like this really matters in the long run, so you just casually jog to the end of the lap barely going faster than a brisk walk."
            if(seatmate== suzu):
                ""
        "Full gun it!":
            "It's not or never to make a stand at this school and blitzing everyone at track would be a great spectacle!"
            "You steady yourself to start your sprint and as the signal goes off you shoot off like a bullet."
            "Your heart feels like its going a mile a minute, but at the same time...."
            "You've barely even made a dent in the track and you're already out of breath!"
            if(seatmate==suzu):
                ""
    #changes people's opinions of you if it even matters
    #take it easy: you make it to the end of the track without too much issue
    #Suzu's kinda disappointed that you didn't even try 
    #full gun it: you start off going very well but as you keep progressing it wears on you more nad more so that you're wheezing by the end of it
    #Suzu makes fun of you for trying to show off despite not being able to 
label classroomPMDay4:
    "You've got a little bit of time to kill before club starts. "
    #choice to go to library 
    #wouldn't hurt to study up on some start stuff since you don't know anything aboutit
    #mini-game to be added later for identifying stuff
    #meet Blitzen maybe
    #different dialogue depending on if you've met him already or not
    #go straight to the club room withtout studying anything
    
label AstronomyClubDay4:
    ""
    #other members didn't show up but you did
    #stuff about stars holding potential of something
    #suzu dreams about getting into the astrologian guild
    
    
label classroomDay5:
    suzu "Hey so uhh a new exibit opened up in the planetarium I asked other friends 
    to accompany me but they were all busy but I guess I'll have to settle with you"
    menu:
        "Yea, sure I'd love to go":
            ""
        "Sorry I've already got plans":
            ""
label classroomPMDay5:
    #Chrono goes over aether mechanics and why it's so important to be in tune with your aether
label AstrologyClubDay5:
    #Talks about how you need to stay after school in order to look at the stars using the neat telescope
label roofDay5:
    # supervised viewing of the stars
    #Rook is the advisor for the club, he's actually the advisor of every club
    #
    
    "It's night and "
label classroomDay6:


label  planetarium:
    "You pull up to the planetarium "
    #displays of ancient allagan tech that allowed space travel previously 
    #after a while of spending time at the planetarium

    #"Hey you wanna get something to eat?"
    #twiddles her fingers together actually I had something else in mind... as she pulls out a box of sorts from her backpack.
    #probably dropping the question of 
label classroomDay7:
    #
label calamityDance:
    #suprise!! you don't win cause you've literally been here for a week and were interacting with 1 person or no people at all
    #
label end:
return







    







