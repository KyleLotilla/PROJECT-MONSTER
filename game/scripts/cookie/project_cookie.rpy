define sc = Character("Scientist")
define mc = Character("Player")
define dog = Character("???")
define c = Character("Cookie")
define ch = Character("Canine Hero")

image whitebg = im.Scale("cookie/white.jpg", 1280, 720)
image under_lab = im.Scale("cookie/undergroundlab.jpg", 1280, 720)
image lab_table = im.Scale("cookie/labtable.jpg", 1280, 720)
image car = im.Scale("cookie/car.jpg", 1280, 720)
image park = im.Scale("cookie/park.jpg", 1280, 720)
image house = im.Scale("cookie/house.jpg", 1280, 720)

image s1 = im.Scale("cookie/scientist.png", 480, 720)
image s2 = im.Scale("cookie/scientist_surprised.png", 480, 720)
image s3 = im.Scale("cookie/scientist_sad.png", 480, 720)
image s4 = im.Scale("cookie/scientist_happy.png", 480, 720)
image s5 = im.Scale("cookie/scientist_angry.png", 480, 360)
image c1 = im.Scale("cookie/babydog.png", 864, 612)
image c2 = im.Scale("cookie/babydog2.png", 864, 612)
image c3 = im.Scale("cookie/adultdog.png", 864, 612)

label project_cookie:
    
    scene black
    with fade
    play music "sounds/cookie/dreams.mp3" loop
    
    mc "We’ve tested and looked up every method we could, and I’m confident that this would work."
    sc "Then what are we waiting for? Let's do this!"
    
    scene under_lab
    
    "My partner and I decided to take the fetus for our own experiment."
    "Our goal... to recreate the fetus into a dog-like creature. A replica of my deceased pet dog, Cookie."
    
    show s1 at center
    sc "Flip that switch for me please."
    mc "Right. You might want to step back once I activate the machine."
    
    hide s1
    stop music fadeout 1.0   
    
    scene whitebg
    "A bright light surrounded the laboratory seconds after the machine was activated."
    "After the light faded, I quickly ran up to where the specimen was placed earlier."
    
    scene under_lab
    with fade
    show s1 at center
    sc "So? What happened?"
    mc "I don't know... The creature isn't here anymore."
    
    play music "sounds/cookie/crypto.mp3" loop
    dog "*whimper*"
    
    show s2 at center
    mc "What was that!?"
    
    scene lab_table
    with fade
    
    show c2 at center
    
    "A small creature was lurking from the corner underneath one of our tables in the laboratory."
    "It was hiding from us. It was scared."
    
    mc "Cookie?"
    mc "It's okay... We won't harm you."
    
    "The creature slowly went up to me. I slowly began to pet the creature on its head, trying to calm it down."
    
    mc "Here take some food too, you're probably hungry."
    
    scene under_lab
    with fade
    
    play music "sounds/cookie/happyalley.mp3" loop
    "We were in awe of the result. The creature had slowly became comfortable with us. This experiment is a big success!"
    
    mc "W-We did it... It actually worked! This is... thank you!"
    show s4 at center
    sc "Always a pleasure to help a friend."
    sc "Come on, let's go and have some fun with your new pet outside!"
    
    stop music fadeout 1.0   
    
    scene black
    with fade
    
    "Two weeks have passed since the creation of Cookie"
    play music "sounds/cookie/dreams.mp3" loop
    
    scene house
    with fade
    
    c "*BARK!*"
    
    mc "What? He's been barking loudly just now..."
    mc "Is there someone trying to break into our house?"
    
    mc "Cookie? What's wrong, buddy?"
    
    show c2 at center
    c "...Your friend! He's in trouble, I-I can sense it!"
    
    mc "W-Whoa whoa, wait. You can talk!?"
    hide c2
    show c1 at center
    c "I'll explain later! We have to go now!"
    
    scene car
    with fade
    
    show c1 at left
    c "He's in that car!"
    mc "But what do we do?"
    c "Stand aside!" 
    
    scene black
    play sound "sounds/cookie/break.mp3"
    "Cookie leaped and bashed his head against the window, breaking it. My partner safely got out of the car."
    
    scene car

    show c1 at left
    show s2 at right
    sc "I was just about to contact you guys but you're both here already."
    sc "How did you know?"
    
    mc "It's a long story. Even I'm not fully sure of it, but..."
    show s1 at right
    mc "I think Cookie here has super powers. He's not just a dog-like creature."
    mc "I-I mean... he can talk. He talks!"
    show s3 at right
    sc "Alright, let's all calm down for a minute. So, you can talk."
    show s1 at right    
    sc "Can you tell us more about it? What else can you do?"
    
    scene park
    
    "We all settled down on a nearby bench to talk about all the stuff that happened today."
    "We began listening to Cookie and learned that our experiment also had side effects on Cookie."
    "Thankfully, none of the side effects he had mentioned so far were negative."
    
    show c1 at center
    c "...And so long story short, something in the components you used to create me gave me these powers."
    c "They seemingly enhanced my abilities. So far I can talk and I have super senses and strength."
    
    show c1 at left
    show s2 at right
    mc "Woah..."
    sc "Amazing..."
    "I looked at my friend, and he also looked at me. He gave me a slight nod."
    
    show s4 at right
    sc "Looks like the first thing we need to do is to get you up to shape."
    sc "Don't worry. My partner and I will help you hone yourself to the best of your abilities."
    mc "R-Right, we will do our best!"
    
    c "I appreciate the help, you guys."
    c "Let's get started as soon as possible, shall we?"
    
    scene black
    with fade
    "After almost two months..."
    
    scene house
    mc "You've earned yourself quite the reputation around our community."
    
    show s4 at center
    sc "Yup. That is right, and we want to let you know that we are so proud of you."
    hide s4
    
    c "Come on! You know all this wouldn't be possible without help from you both."
    
    mc "I guess we all get some credit."
    mc "Welcome back, Canine Hero!"
    
    show c3 at center
    
    ch "Having a codename around really does feel great, don't you think?"
    ch "Really makes all this hero stuff feel so cool, yet so real!"
    
    sc "I can't agree any less with that, but today, you've earned yourself a well-deserved break!"
    
    scene black
    with fade
    
    "And so our creation had led on to be the greatest hero in their community."
    "Donning the name, Canine Hero, what was originally supposed to be just an ordinary dog had turned out to be a superhero."
    
    #Credits
    "Credits"
    "Royalty Free Music from Bensound and Kevin Macleod"
    "Sound Effects from Fesliyan Studios"
    