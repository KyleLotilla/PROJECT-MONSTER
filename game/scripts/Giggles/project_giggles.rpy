# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character("Narrator")
define scientist = Character("Scientist Kylan")
define creation = Character("Creation")
define Giggles = Character("Giggles")
define Fellow_scientist = Character("Scientist Denzel")
define headScientist = Character("Head Scientist Abram")
define unknown = Character("??????")

image home = "Giggles/home.jpg"
image desk = "Giggles/Desk.jpg"
image lab = "Giggles/lab.jpg"
image bedroom = "Giggles/Bedroom.jpg"
image kitchen = "Giggles/Kitchen.jpg"
image beach = "Giggles/Beach.jpg"


image blob = "Giggles/tempblob.png"
image Giggles = "Giggles/Giggles_left.png"
image RightGiggles = "Giggles/Giggles_Right.png"
image SadGiggles = "Giggles/Sad_Giggles.png"
image SickGiggles = "Giggles/Sick_Giggles.png"
image About_to_die_Giggles = "Giggles/About_to_die_Giggles.png"
image failure = "Giggles/Messed_up.png"

image neutralscientist = "Giggles/scientist.png"
image Happyscientist = "Giggles/happyscientist.png"
image Shockedscientist = "Giggles/shockedScientist.png"
image Sadscientist = "Giggles/scientist_sad.png"
image Cryingscientist = "Giggles/scientist_crying.png"
image Stressedscientist = "Giggles/scientist_stressed.png"

image Clone1 = "Giggles/happyscientist_clone2.png"
image Clone2 = "Giggles/Scientist_clone3.png"

image spaghetti = "Giggles/spaghetti.png"
image tombstone = "Giggles/tombstone.png"

image logo alias = "spaghetti"


define teleport = ImageDissolve("imagedissolve teleport.png", 1.0, 0)
transform logopos:
    xalign .5
    ypos 25


# The game starts here.

label project_giggles:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene home
    with fade

    play music "sounds/Giggles/154972__setuniman__nervous-and-calm-together-0n-16mi.mp3" fadeout 1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.


    #scene 1 start

    narrator "After a long day from work. The scientist decided to return to his beach house near the lab"

    narrator "and bring his creation home. He wanted to love and care for it as if it was his own child."

    narrator "The reason for this is because of the amount of time and money he placed into this project"

    scene desk
    with dissolve

    show Happyscientist:
        xalign 0.75
        yalign 1.0


    scientist "Two months have passed since the project began."

    scientist "I wanted to make a creature that could make others happy and that could feel empathy"

    scientist "and also have high intelligence."

    show blob:
        xalign 0.25
        yalign 1.0

    scientist "I know once you take your own original appearance. You would be able to spread joy and laughter to the world."

    scientist "That is why I have decided to name you Giggles."

    scientist "I'm excited to see what form you will end up taking."

    creation "Master... "

    creation "So my name is Giggles and my purpose is to make people happy."

    hide blob with dissolve

    narrator "The creation of the scientist started to change appearance"

    scene desk

    show Shockedscientist:
        xalign 0.75
        yalign 1.0

    show Giggles:
        xalign 0.25
        yalign 1.0


    Giggles "I feel alive. "

    Giggles "Master how can I serve you"

    hide Shockedscientist

    show Happyscientist:
        xalign 0.75
        yalign 1.0

    scientist "For now we will rest but tomorrow we will present you to the other scientists."

    scientist "They will see what you are capable of."

    scientist "I hope they are as excited as I am."

    stop music fadeout 1

    pause .5

    #end scene 1

    #start scene 2

    scene lab
    with fade

    play music "sounds/Giggles/504686__foolboymedia__uplifted.mp3" fadeout 1

    show Happyscientist:
        xalign 0.25
        yalign 1.0

    scientist "Fellow scientists"

    scientist "I present to you my creation Giggles."

    hide Happyscientist with fade

    show Giggles:
        xalign 0.25
        yalign 1.0

    Giggles "It is my pleasure to meet you all!"

    show Clone1:
        xalign 0.75
        yalign 1.0

    Fellow_scientist "Wow, so what can you do?"

    Giggles "I can serve you in any way to make you happy. Afterall, that is how I was designed by my master."

    Fellow_scientist "Hmmm"

    Fellow_scientist "I guess a nice cup of coffee will be good."

    Giggles "Ok, one cup of coffee coming right up!"

    Fellow_scientist "Wow, this tastes delicious!"

    Fellow_scientist "I guess you are also very intelligent if you are able to make coffee this good without anyone teaching you."

    Giggles "Thank you!"

    hide Clone1 with fade

    show Clone2:
        xalign 0.75
        yalign 1.0

    headScientist "Giggles was it?"

    headScientist "May I speak with your master?"

    Giggles "Of course sir, I will call him right away!"

    stop music fadeout 1

    hide Giggles with fade

    hide Clone2

    show Clone2:
        xalign 0.75
        yalign 1.0

    show Happyscientist:
        xalign 0.25
        yalign 1.0

    scientist "What is it sir?"

    play music "sounds/Giggles/154972__setuniman__nervous-and-calm-together-0n-16mi.mp3" fadeout 1

    headScientist "Aside from speaking and being able to understand people, and serving others with simple commands,"

    headScientist "has the creation you brought here done anything mindblowing like show super strength?"

    headScientist "Or read minds?"

    hide Happyscientist

    show Sadscientist:
        xalign 0.25
        yalign 1.0

    scientist "No sir, Giggles hasn't shown us anything like that."

    headScientist "Really..."

    headScientist "All this time and effort on the project."

    headScientist "This is all we get."

    headScientist "A cute blue creature capable of simple service and speech."

    scientist "Don't worry sir, I'll make a more impressive creature for sure."

    headScientist "I hope so."

    headScientist "You have to live up to the expectations of your fellow scientists here."

    headScientist "You already have so much success."

    headScientist "And you have become very rich because of your accomplishments."

    headScientist "Don't start messing up now with projects like this."

    scientist "Yes sir."

    stop music fadeout 1

    scene desk
    with dissolve

    narrator "It has been six months since the presentation."

    narrator "The scientist has tried several times to recreate a creature like Giggles but with super powers."

    show Sadscientist:
        xalign 0.75
        yalign 1.0

    scientist "I don't understand what I'm doing wrong."

    scientist "Everytime I try to recreate a new creature like Giggles."

    scientist "It always ends in a mess."

    show failure:
        xalign 0.25
        yalign 0.5

    unknown "WWWWWWWWWWRRRRRRRYYYYYYYYYYY!!"

    scientist "huhhh...."

    scientist "Well..."

    scientist "Time to terminate another failure."

    scientist "I think I'm gonna rest after."

    play music "sounds/Giggles/460900__dekstromoramid__hide-my-time.mp3" fadeout 1

    scene bedroom with fade

    show Cryingscientist:
        xalign 0.25
        yalign 1.0

    scientist "Sob Sob."

    Giggles "WWUUAAH!"

    Giggles "WWWWWUUUUUAAAAAHHH!"

    Giggles "WWWWWWUUUUUUAAAAAAAHHHHHH!"

    scientist "Giggles is that you?"

    pause 1.0

    show SadGiggles:
        xalign 0.75
        yalign 1.0

    scientist "Why are you crying so loudly?"

    Giggles "Because I feel like I failed my master?"

    Giggles "He is always tired and sad."

    Giggles "I failed to make him happy."

    hide Cryingscientist

    show Sadscientist:
        xalign 0.25
        yalign 1.0

    scientist "No Giggles you didn't fail me in any way."

    scientist "I didn't consider how you would feel if you saw me like this."

    scientist "It's okay Giggles stop crying now."

    hide SadGiggles

    show RightGiggles:
        xalign 0.75
        yalign 1.0

    Giggles "Don't worry about what the head scientist said."

    Giggles "Because to me "

    Giggles "I think you're great."

    scientist "Really?"

    Giggles "Of course."

    Giggles "You gave me the ability to talk."

    Giggles "And you gave me the ability to feel empathy."

    Giggles "At first, I felt bad because of what the head scientist said to you"

    Giggles "but then I realized that words like that can't mentally break down my master."

    Giggles "I'm able to think, talk and act the way I can now because of my master's intelligence."

    show Happyscientist:
        xalign 0.25
        yalign 1.0

    scientist "Thank you so much Giggles!"

    scientist "I needed those words of encouragement!"

    scientist "it's been a while since I heard words like that."

    pause 2

    stop music fadeout 1

    narrator "Taking his creation's words to heart"

    narrator "The scientist decided not to let the expectations of others get the better of him"

    narrator "He also has decided that tomorrow he would prepare Giggles something in the kitchen"

    #end scene 2

    #start scene 3

    play music "sounds/Giggles/410520__jamessi__light-tune-no.mp3" fadeout 1
    pause .5

    scene kitchen
    with fade

    narrator "The scientist decided to research on a dish to cook for Giggles and he worked hard to prepare it."

    show Happyscientist:
        xalign 0.75
        yalign 1.0

    scientist "Giggles I made something special for you!"

    show Giggles:
        xalign 0.25
        yalign 1.0

    pause .5

    Giggles "Wow master I am honored."

    Giggles "What is it?"

    scientist "This dish is called spaghetti."

    show logo alias at logopos

    Giggles "It looks delicious!"

    Giggles "You must also be a good cook!"

    Giggles "num num num num."

    hide logo alias

    Giggles "It tastes great master."

    stop music fadeout 1

    scene bedroom with fade

    play music "sounds/Giggles/415186__psovod__sad-heaven-piano-3.mp3" fadeout 1

    pause 1.5

    Giggles "Cough Cough.."

    scientist "Giggle what is wrong?"

    pause 1.5

    show SickGiggles:
        xalign 0.75
        yalign 1.0

    Giggles "I feel really sick and weak master."

    show Shockedscientist:
         xalign 0.25
         yalign 1.0

    Giggles "Cough Cough.."

    scientist "HOW COULD THIS HAPPEN?!"

    scientist "I CAN'T BELIEVE"

    scientist "THE ONE WHO GIVES ME ENCOURAGEMENT ENDS UP SICK!"

    scientist "DON'T WORRY GIGGLES!"

    scientist "I'LL DISCOVER A CURE TO YOUR ILLNESS!"

    stop music fadeout 1

    #end scene 3

    #start scene 4

    scene kitchen
    with fade

    narrator "The scientist decided to keep his head high and approach this problem with a calm and optimistic mindset."

    show neutralscientist:
        xalign 0.25
        yalign 1.0

    play music "sounds/Giggles/327924__shadydave__determined.mp3" fadeout 1

    scientist "Alright first I'll gather the ingredients I used to make that spaghetti."

    scientist "Giggles became sick a few hours after he ate the spaghetti."

    scientist "Then I'll analyze Giggles' cellular structure back at the lab."

    scientist "Hopefully I can find out why he got sick from eating the spaghetti."

    scientist "Given that I have the ingredients"

    scientist "as well as an understanding of how Giggles' cellular structure works."

    scientist "Then create a cure right after."

    scientist "Don't worry Giggles I have it all figured out."

    scientist "I'll make a cure in no time"

    scene lab
    with fade

    show neutralscientist:
        xalign 0.25
        yalign 1.0

    scientist "Excuse me."

    show Clone1:
        xalign 0.75
        yalign 1.0

    Fellow_scientist "Yes, how may I help you?"

    scientist "Do you happen to have the data about the cellular structure of the creation from project Giggles?"

    Fellow_scientist "Oh..."

    Fellow_scientist "Sorry I don't unfortunately."

    Fellow_scientist "Information like that has restricted access."

    Fellow_scientist "The heads won't allow just anyone to have that information."

    Fellow_scientist "They allowed you to bring the project home and observe it's change because of your large involvement in it."

    Fellow_scientist "But they don't trust that you will keep the information secure."

    Fellow_scientist "Talk to the head scientist that called you six months ago after your presentation."

    Fellow_scientist "Maybe he can give you access for that information."

    scene lab
    with dissolve

    show neutralscientist:
        xalign 0.25
        yalign 1.0

    scientist "Excuse me sir."

    show Clone2:
        xalign 0.75
        yalign 1.0

    pause .5

    headScientist "Yes, how may I help you?"

    scientist "I need access to the documents about Giggles cell structure."

    scientist "It seems that I cannot access it and I need permission from the head scientist."

    headScientist "And what will you use this information for?"

    scientist "I believe that Giggles has the ability to evolve into a creature far more amazing."

    scientist "All I need to do is modify his cellular structure."

    headScientist "hhmm."

    pause 1

    headScientist "Interesting.."

    headScientist "Ok. Come with me I will lead you to the area where we keep the data about project Giggles."

    headScientist "You should be able to get what you need in there."

    scene desk
    with dissolve

    show neutralscientist:
        xalign 0.25
        yalign 1.0

    scientist "I spend the whole day in the lab studying for the reason why Giggles got sick."

    scientist "And I still don't have any leads."

    scientist "I'll go to the lab tomorrow to study again."

    scene lab
    with dissolve

    show neutralscientist:
        xalign 0.25
        yalign 1.0

    scientist "Ok things seem to clearer."

    scientist "So Giggles cells react negatively to the pasta in the spaghetti."

    scientist "And I also found out that his body also reacts negatively to the tomato in the spaghetti."

    show Clone2:
        xalign 0.75
        yalign 1.0

    scientist "Hello sir"

    headScientist "If I may ask why are you analyzing the reaction of Giggles' cellular structure with spaghetti ingredients?"

    scientist "Sir, I believe spaghetti ingredients are key to turning Giggles into the creature that could amaze you."

    scientist "I even have research to prove my point."

    headScientist "I dont't need to see that I was just curious."

    scientist "Ok"

    hide Clone2

    scientist "I can't let him find out I'm using restricted information to cure Giggles."

    scientist "After all, he doesn't see the value of Giggles the way I do."

    scientist "Ok, I'll try to find substances in the lab that I could use of my medicine."

    scene desk
    with dissolve

    show neutralscientist:
        xalign 0.25
        yalign 1.0

    scientist "Ok maybe this medicine will work."

    pause 1.5

    scene bedroom with fade

    show neutralscientist:
        xalign 0.25
        yalign 1.0

    show SickGiggles:
        xalign 0.75
        yalign 1.0

    Giggles "Master I feel hotter and weaker than before."

    scientist "Don't worry about it Giggles take this."

    scientist "It will make you feel better."

    Giggles "Thank you master."

    pause 2.0

    scene lab
    with dissolve

    show Stressedscientist:
        xalign 0.25
        yalign 1.0

    scientist "The medicine I gave Giggles didn't work"

    scientist "I barely got any sleep just trying to develop that medicine"

    scientist "I'll just try again but this time with different ingredients for the medicine."

    scientist "Maybe I can find the ingredients I need in that area in the lab."

    scene lab
    with dissolve

    show Stressedscientist:
        xalign 0.25
        yalign 1.0

    scientist "Ok, after a few hours of analyzing the data and creating the medicine."

    scientist "I think this is the cure to Giggles' illness."

    stop music fadeout 1

    #end scene 4

    #start scene 5

    scene bedroom with fade

    narrator "The scientist feels excited because after days of no sleep and hard work a proper cure for Giggles' illness is finally made."

    narrator "But will this one actual heal Giggles or will it fail again?"

    show Happyscientist:
        xalign 0.25
        yalign 1.0


    scientist "Giggles I finally got it."

    scientist "Say goodbye to your illness."

    scientist "Giggles..."

    play music "sounds/Giggles/255581__moz5a__remembered.mp3" fadeout 1

    pause 2.0

    show About_to_die_Giggles:
        xalign 0.75
        yalign 1.0

    hide Happyscientist

    show Shockedscientist:
        xalign 0.25
        yalign 1.0

    Giggles "Master I don't even feel anything anymore."

    Giggles "I think I'm gonna die."

    Giggles "My only regret is not making more people happy like I was intended to."

    hide Shockedscientist

    show Cryingscientist:
        xalign 0.25
        yalign 1.0

    scientist "Giggles no."

    scientist "Here! Take the medicine!"

    scientist "Take it and this illness will go away!"

    Giggles "What master?"

    Giggles "I can't"

    Giggles "even hear you anymore."

    Giggles "Farewell master."

    Giggles "Stay strong and get some rest."

    hide About_to_die_Giggles with dissolve

    hide Cryingscientist with dissolve
    pause 1

    show Cryingscientist:
       xalign 0.5
       yalign 1.0

    scientist "NNNOOOO!"

    scientist "GGGGIIIIGGGLLEES!"

    scientist "AAAAAAHHHHHHH!"

    scene beach with fade
    pause .5

    show tombstone:
        xalign 0.25
        yalign 1.0

    show Cryingscientist:
        xalign 0.75
        yalign 1.0

    pause 1.5

    scientist "Giggles I found a place to bury you."

    scientist "I made a tombstone for you and engraved these words on it."

    scientist "It says:"

    scientist "Here lies my greatest creation and success"

    scientist "the one who manage to make me smile and encouraged me to keep my head up high."

    scientist "Rest in peace,"

    pause 2.0

    scientist "Giggles."

    stop music fadeout 1



    # This ends the game.

    return
