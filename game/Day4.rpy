label bedroomAMDay4:
    scene bedroom
    with fade
label streetDay4:
    #
label hallwayDay4:
    #Decide where you want to go visit before class (if you know the location)
label entranceDay4:
    if(suzu_love >3):
        #might change this so that you can see suzu at the entrance regardless 
        "Approaching the entrance of the school you notice that Suzu is carrying a big box by herself to the school."
        "She seems to be struggling a bit since the box looks longer than she is tall. You should probably try to give her a hand."
        menu: 
            "Help":
                "You rush over to her side and greet her"
                me "Good morning! You need a hand with that?"
                "She slightly jumps at your presence like she wasn't expecting anyone to reach out to help her."
                suzu "OH, uhh hey there. Why would I need help from someone like you. I mean if you want to help sure "
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
    #Rook seems to be absent on sick leave, so you're getting replacement teachers for the rest of the week.
    "Today's curriculum seems to be PE. It would make sense that a warrior of light in training would need to be physically able in addition to mentally sharp.
    Unfortunately due to your gamer status, you dread this coming event."
    if(seatmate== suzu):
        show suzu gym smug at right:
                zoom 0.5
        """You look to your seatmate in hopes of having someone to share this struggle with.
        Unfortunately, that doesn't seem to be the case as the bespectacled bookworm doesn't seem out of her element in the slightest. She's even doing stretches!!
        She's emmiting a strange pressure so you find it difficult to even approach her in this state.
        Track is the first activity and as soon as the signal was given... bang! she bolted forward like a bullet absolutely decimating the competition and having them eat her dust. 
        To further this fact she took a victory lap just to show off."""
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
    "After waiting anxiously for everyone to take their turn it's "
    menu:
        "Take it easy":
            "It's not like this really matters in the long run, so you just casually jog to the end of the lap barely going faster than a brisk walk."
            if(seatmate== suzu):
                ""
        "Full gun it!":
            """It's not or never to make a stand at this school and blitzing everyone at track would be a great spectacle!
            You steady yourself to start your sprint and as the signal goes off you shoot off like a bullet.

            Your heart feels like its going a mile a minute, but at the same time....

            You've barely even made a dent in the track and you're already out of breath!"""
            if(seatmate==suzu):
                ""
    #changes people's opinions of you if it even matters
    #take it easy: you make it to the end of the track without too much issue
    #Suzu's kinda disappointed that you didn't even try 
    #full gun it: you start off going very well but as you keep progressing it wears on you more nad more so that you're wheezing by the end of it
    #Suzu makes fun of you for trying to show off despite not being able to 
label lunchbreakDay4:
    #
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
label endDay4:
    #
jump BedroomAMDay5
