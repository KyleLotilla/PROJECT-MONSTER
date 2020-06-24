# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pa = Character("PA System")
define s = Character("Scientist")
define m = Character("Monster")
define n = Character("Narrator")
define hs = Character("Doctor Berger")
define d = Character("Dad")

image sci = "chef/scientist.png"
image sciH = "chef/scientist_happy.png"
image sciA = "chef/scientist_angry.png"
image sciSa = "chef/scientist_sad.png"
image sciSu = "chef/scientist_surprised.png"
image sciSt = "chef/scientist_stressed.png"
image hand = "chef/sciHand.png"
image hS = "chef/head_scientist.png"
image dad = "chef/dad.png"
image dFlip = im.Flip("chef/dad.png", horizontal = True)

image mon = "chef/slime.png"
image monH = "chef/slimeH.png"

image lab = "chef/lab.jpg"
image kitchen = "chef/kitchen.jpg"
image grocery = "chef/grocery.jpg"
image black = "chef/black.jpg"


# The game starts here.

label project_chef:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene lab
    
    play music "sounds/chef/231578__lemoncreme__floating-synth-melody-at-130-bpm-c-major-loop-music.mp3" fadeout 1
    
    window hide
    pause
    window show

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show hS

    # These display lines of dialogue.

    hs "Well done everyone! We have succesfully brought our creation to life!"
    hs "You will all now take turns in taking the creature home for a week to observe how it evolves."
    hide hS
    show hS at left
    show sciSu at right
    hs "For this week, I assign the creature to you, Scientist #159."
    hs "And please, do take care of the creature, will you?"
    hide hS
    hide sciSu
    show sci at right
    show hS at left
    show mon
    m "*Stares at the scientist*"
    hide hS
    hide mon
    show mon at left
    s "What are you lookin at?"
    pa "Best of luck to you, Scientist #159. Don't forget to update us on how things are going with the monster every now and then."
    s "I guess I better start heading home then."
    hide sci
    show sciH at right
    s "Let's go blobby."
    
    stop music fadeout 1
    
    scene kitchen
    
    play music "sounds/chef/504686__foolboymedia__uplifted.wav" fadeout 1
    
    window hide
    pause
    window show
    
    show sciH at right
    show mon at left
    s "Home at last."
    hide sciH
    show sciSa at right
    s "Hmmm... I feel like I'm forgetting something. Wait what date is it?"
    s "*Checks the calendar*"
    hide sciSa
    show sciSu at right
    s "Oh crap, it's dinner night with my dad!"
    s "I need to hurry up and get to the grocery to get ingredients but I can't just leave ol' slimey face here alone."
    hide sciSu
    show sci at right
    s "Meh, I'll just hide him in bag. Come here boy."
    s "There's some vampire comics there to keep you entertained if you can read that is... Wait can you even understand me?"
    m "*Nods*"
    hide sci
    show sciH at right
    s "Oh neat!"
    s "Alright, time to go."
    
    stop music fadeout 1
    
    scene grocery
    
    play music "sounds/chef/475703__ecfike__grocery-store-3-deli.wav" fadeout 1
    
    window hide
    pause
    window show
    
    show sci
    s "Okay, we're here, blobert."
    s "Gotta get everything in my shopping list fast so I still have time to cook."
    s "Let's see here..."
    window hide
    hide sci
    show hand
    pause
    window show
    s "Oh, that's quite simple huh?"
    s "I guess fried chicken doesn't really require much."
    hide hand
    n "The scientist then proceeds to buy everything in his shopping list. Although for some reason, he bought other ingredients without realizing it."
    show sciH
    s "That was fast."
    hide sciH
    show sciSa
    s "Wait, when did I buy chicken breasts, ham, eggs, and cheese? I don't even need these for fried chicken."
    hide sciSa
    show sci
    s "Oh well, gotta get home quick."
    
    stop music fadeout 1
    
    scene kitchen
    
    play music "sounds/chef/504686__foolboymedia__uplifted.wav" fadeout 1
    
    window hide
    pause
    window show
    
    show sciH at right
    show mon at left
    
    s "Let's do this. time to cook"
    hide sciH
    show sciSu at right
    s "Wait, what happened to my cookbook!?"
    hide sciSu
    show sciSa at right
    s "Hey man, did you eat this?"
    m "*Smiles*"
    s "Oh man, I'm so screwed. I don't even know how to cook fried chicken."
    s "Dad's coming over real soon. Whatever, I'll just wing it."
    hide mon
    hide sciSa
    n "The scientist attempts to cook the fried chicken, but without his cookbook, he fails miserably."
    show sciSa at right
    show mon at left
    s "It's completely ruined! What am I supposed to do now?"
    s "*Checks watch*"
    hide sciSa
    show sciH at right
    s "I still have time. I'll just run over to the store real quick and get more ingredients and a new cookbook."
    s "Stay put jelly-ace, and don't touch anything while I'm gone."
    hide sciH
    hide mon
    n "As the scientist was about to leave his house, he runs into someone in his living room."
    show sciSu at right
    show dad at left
    s "Dad!?"
    s "What are you doing here so early?"
    d "Hey kiddo. I just wanted to help you with the cooking."
    hide sciSu
    show sciSa at right
    s "Uhh, about that..."
    d "Yeah?"
    s "Nevermind. I'll be right back."
    s "Whatever you do, don't go into the kitchen."
    hide  sciSa
    d "Hmm..."
    
    stop music fadeout 1
    
    scene grocery
    
    play music "sounds/chef/475703__ecfike__grocery-store-3-deli.wav" fadeout 1
    
    window hide
    pause
    window show
    
    show sciSt
    s "Finally, I made it."
    s "Man I'm so tired. I need to catch my breath for a sec."
    hide sciSt
    n "The scientist succesfully buys all of the ingredients again."
    show sciSt
    s "Good thing I got the last stock of chicken. Time to head home."
    s "I'm still so tired. I'm probably gonna collapse in the middle of the street or something. Whatever."
    
    stop music fadeout 1
    
    scene kitchen
    
    play music "sounds/chef/504686__foolboymedia__uplifted.wav" fadeout 1
    
    window hide
    pause
    window show
    
    n "The scientist enters the living room looking for his dad"
    show sciSt
    s "Hey dad, I'm back"
    s "Dad? Where'd you go?"
    s "*Hears a noise in the kitchen*"
    s "What's that sound? And why is it so messy here?"
    d "AHHHH!!!"
    hide sciSt
    show sciSu
    s "Oh no. Dad!"
    hide sciSu
    show monH at left
    show dFlip
    show sciSu at right
    d "My my, this dish is absolutely delicious! Very well done you creature!"
    s "Dad?"
    hide dFlip
    show dad
    d "Ah, my boy! What took you so long? This creature already started cooking without you."
    hide sciSu
    show sciSt at right
    s "Oh. I just uhh... had to... I don't know anymore."
    d "This creature is one hell of a chef, let me tell you that."
    d "Is this why you didn't want me to enter the kitchen?"
    hide sciSt
    show sciH at right
    s "Oh! Uhh, yeah. It was supposed to be a surprise hehe."
    d "Well it's an excellent surprise."
    s "Thanks, dad."
    hide sciH
    hide monH
    hide dad
    n "After dinner, the scientist goes to talk with the monster."
    show sci at right
    show monH at left
    s "Hey, how'd you do that?"
    s "Did you learn to cook from eating the cookbook?"
    m "*nods*"
    s "Then I guess you also probably learned mind control from eating my vampire comics huh? That's why I bought all those extra ingredients without knowing."
    n "*nods*"
    hide sci
    show sciH at right
    s "This is a sick discovery."
    s "Let's go to my library and see what other books I can feed you you."
    hide sciH
    hide monH
    n "Over the next few days, the scientist fed his entire library to the monster. It eventually learned to talk and they became best friends."
    n "The end."
    
    stop music fadeout 1

    # This ends the game.

    return
