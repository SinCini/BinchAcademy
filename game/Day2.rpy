label bedroomAMDay2:
    scene bedroom
    with fade
    "You wake up."
    "It's your second day! After a whole summer of pulling all nighters you're still tired, but there's no time to waste!"
    "Or is there?"
    menu:
        "Go to school early." if (taka_met ==True):
            "If you go early you might see that redhead again"
            jump streetDay2
        "Sleep in a little longer.":
            """It wouldn't hurt to get a few more moments of shut eye in order to be completely rested for the morning.
                
                You managed to not sleep past your alarm today. Maybe your body has finally gotten the hint that you can't slack off anymore.
                
                With this in mind you get dressed, have a decent breakfast and make your way to school.
            """
            jump hallwayDay2

label streetDay2:
    #stuff about Taka 
        jump classroomDay2
label hallwayDay2:
    #Decide where you want to go visit before class (if you know the location)
label classroomDay2:
    scene classroom day
    #Sil and Beren scene where they're kind of showing off the fact that they're wizkids and are a shoe-in for the calamity couple status
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
                #She doesn't say anything 
                "She hums, staring at the cards on her desk, but at last you hear her speak."
                suzu "Morning."
                "You’re happy to see that she isn’t going out of her way to ignore you at least."
                me "What are those cards on your desk? I've never seen them before."
                suzu "Seriously? You've never heard of Tarot readings before? 
                        It's basic astrology, and a great way to see how the week will pan out, which obviously it's going to go well for me."
                #Can comment on how cool it was potentially 
                suzu "I can make another prediction for you."
                suzu "Club sign-ups are today."
                me "Eh?!"
                me "Who announces this stuff, anyways?!"
                "Mr. Addock enters the class just then."
    else:
        """You plant your butt down at your seat. Once again it doesn't seem like anyone's taken an interest in you. To make matters worse
            the groups are too tightly knit and you can't find a single hole to interject youself into. This is the second day and no one's noticed that you're sitting the main character's seat!

            Before you managed to get too wrapped up in your own thoughts you see Mr. Rooklan open the door and turn your head to him.
        """
    "The bell rings and you hear Mr. Addock"
    rook "Believe it or not class, I've got a big accouncement to make."
    
    rook "So. Club sign-ups are today."
    #rest in piece "so club sign-ups are today"
    #have a reaction when you talked to Suzu and she predicted it.
    "You’ve been waiting for this! The only thing more exciting than the school dances were the school clubs. 
    There were so many, how were you going to decide?! Would you even find something that you're passionate about?"
    rook "There’s a list of clubs posted outside in the hallway. Take a look and decide after class. 
    Don't let your excitement distract you from my lesson."
label lunchbreakDay2:
    #
label classroomPMDay2:
    """Another boring day of classes go by, though you were tripped up when Mr. Addock asked a question about 
        how properly pass nisis. This only made more 

        It seems pretty complicated and you wonder to yourself when you'd use this in the real world.

    Time to take a look at what clubs are available."""
    if (seat == suzu):
        "You step into the hallway, but before you get out the door, you hear someone clear their throat."
        if (suzu_love>=3):
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
        #Need to include a scnario in the case that you don't 
#explore the school to see what's up

#
label endDay2:
#
jump BedroomAMDay3
