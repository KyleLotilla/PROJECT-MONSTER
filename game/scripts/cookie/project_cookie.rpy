define sc_one = Character("Scientist #1")
define sc_two = Character("Scientist #2")
define r = Character("Ron")
define m = Character("Mike")
define dog = Character("???")
define c = Character("Cookie")
define ch = Character("Canine Hero")

#as of now, the lab, car and park images are placeholders, as I am unable to get corresponding images yet
image under_lab = im.Scale("cookie/undergroundlab.jpg", 1280, 720)
image lab_table = im.Scale("cookie/labtable.jpg", 1280, 720)
image car = im.Scale("cookie/car.jpg", 1280, 720)
image park = im.Scale("cookie/park.jpg", 1280, 720)
image house = im.Scale("cookie/house.jpg", 1280, 720)

label project_cookie:
    
    scene black
    
    sc_one "We’ve tested and looked up every method we could, and I’m confident that this would work."
    sc_two "Then what are we waiting for? Let's do this!"
    
    scene under_lab
    
    "Two young scientists, Ron and Mike, decided to take the fetus for their own experiment."
    "Their goal... to recreate the fetus into a dog-like creature. A replica of Ron's deceased pet dog, Cookie."
    
    #show Mike with neutral expression at left
    m "Ron, flip that switch for me please."
    
    #show Ron with neutral expression at right
    r "Right. You might want to step back once I activate the machine."
    
    #hide Ron
    #hide Mike
    "A bright light surrounded the laboratory seconds after the machine was activated."
    "After the light faded, Ron quickly ran up to where the specimen was placed earlier."
    
    #show Mike with surprised expression at left
    m "So? What happened?"
    #show Ron with worried expression at right
    r "I don't know, Mike... The creature isn't here anymore."
    
    dog "*whimper*"
    
    #show Ron with surprised expression at right
    r "Cookie?"
    
    scene lab_table
    
    #show Ron with neutral expression at left
    #show Cookie at right
    
    r "It's okay... We won't harm you."
    
    "The creature slowly went up to Ron. Ron, in return began to pet the creature slowly on its head."
    
    r "Here take some food too, you're probably hungry."
    
    scene under_lab
    
    "The two scientists were in awe of the result. The creature had slowly became comfortable with them."
    
    #show Ron with happy expression at left
    r "W-We did it... It actually worked! Mike, this is... thank you!"
    #show Mike with happy expression at right
    m "Always a pleasure to help a friend, Ron."
    m "Come on, let's go and have some fun with your new pet outside!"
    
    scene black
    
    "Two weeks have passed since the creation of Cookie"
    
    scene house
    
    c "*BARK!*"
    
    #show Ron with surprised expression at center
    r "What? He's been barking loudly just now..."
    r "Is there someone trying to break into our house?"
    #hide Ron
    
    #show Ron with worried expression at left
    r "Cookie? What's wrong, buddy?"
    
    #show Cookie with worried expression at right
    c "...Your friend, Mike! He's in trouble, I-I can sense it!"
    #show Ron with surprised expression at left
    r "W-Whoa whoa, wait. You can talk!?"
    c "I'll explain later! We have to go now!"
    
    scene car
    
    #show Ron with neutral expression at left
    #show Cookie with neutral expression at right
    c "He's in that car!"
    r "But what do we do?"
    c "Stand aside!"
    
    "Cookie leaped and bashed his head against the window, breaking it. Mike safely got out of the car."
    
    #hide Cookie
    #show Mike with neutral expression at left
    #show Ron with neutral expression at left
    m "Ron? Cookie? I was just about to contact you guys but you're both here already."
    m "How did you know?"
    
    r "It's a long story. Even I'm not fully sure of it, but..."
    r "I think Cookie here has super powers. He's not just a dog-like creature."
    #show Ron with surprised expression
    r "I-I mean... he talks, Mike. He talks!"
    m "Alright, let's all calm down for a minute. So, Ron told me you can talk."
    m "Can you tell us more about it?"
    
    scene park
    
    "The two scientists and Cookie settled down on a nearby bench."
    "They began listening and learned more about the other effects of their experiment on Cookie."
    
    #show Cookie with neutral expression at center
    c "...And so long story short, something in the components you used to create me gave me these powers."
    c "They seemingly enhanced my abilities. So far I can talk and I have super senses and strength."
    
    #hide Cookie
    #show Ron and Mike with surprised expression
    m "Woah..."
    r "Amazing..."
    
    #show Mike with happy expression at left
    m "We will help you hone yourself to the best of your abilities."
    #show Ron with happy expression at right
    r "R-Right, we will do our best!"
    
    #hide Mike
    #hide Ron
    #show Cookie with happy expression at center
    c "I appreciate the help, you guys."
    c "Let's get started as soon as possible, shall we?"
    
    scene black
    "After a month..."
    
    scene house
    #show Ron with happy expression at center
    r "You've earned yourself quite the reputation around our community."
    #hide Ron
    
    #show Mike with happy expression at center
    m "Yup. That is right, and we want to let you know that we are so proud of you."
    #hide Mike
    
    c "Come on! You know all this wouldn't be possible without help from you both."
    
    r "I guess we all get some credit."
    r "Welcome back, Canine Hero!"
    
    #show Canine Hero with proud/neutral expression
    
    ch "Having a codename around really does feel great, don't you think?"
    ch "Really makes all this hero stuff feel so cool, yet so real!"
    
    m "I can't agree any less with that, but today, you've earned yourself a well-deserved break!"
    
    scene black
    
    "And so the creation of the two scientists had led on to be the greatest hero in their community."
    "Donning the name, Canine Hero, what was originally supposed to be just an ordinary dog had turned out to be a superhero."
    