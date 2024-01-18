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


                    

    

    
    



   #         "Keep walking.":
      #      scene spooky
         #   with fade
            #show dino normal
    #        n "Yo'. You're in the wrong hallway, kid."
      #      "There's a rugged looking Miqo'te eyeing you with what looks like a
        #    cigarette in her mouth. She screams of coolness, and looks a little
          #  surprised to see you standing in front of her."
    #        menu:
      #          "S-sorry! I'll go!":
      #              jump runawayDay1
     #           "S-sorry! Please don't kill me!":
     #               $dino_love +=1
      #              n "Kill?"
      #              "Her eyes go wide and then she bursts into laughter."
      #              n "Haha! You're pretty funny. I like that. What are you doing
      #              here, though?"
      #              me "I'm [player_name]. I think I'm lost."
       #             "She stares you down, looking very punk-rock and pretty and
        #            scary, and then stands up, walking closer..."
        #            "And past you."
        #            n "Come on, kid. I'll help you out, but you  owe me one."
        #            "She helps you out more than you expect, but you're mostly
         #           too nervous to talk to her otherwise. She seems nice for
       #             a school gangster, though."
        #            n "I'll see you around again, okay? Good luck in class."
          #          jump classroomDay1
    







    







