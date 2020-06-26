# The script of the game goes in this file.

image library = "Fetch/Library.jpg"
image lab = "Fetch/Lab.jpg"
image last = "Fetch/Last.jpg"

image angry = "Fetch/scientist_angry.png" # Is also used as a neutral face
image happy = "Fetch/scientist_happy.png"
image sad = "Fetch/scientist_sad.png"
image stressed = "Fetch/scientist_stressed.png"
image surprised = "Fetch/scientist_surprised.png"

image baby = "Fetch/B164.png"
image babyNA = "Fetch/B164WA.png"
image adult = "Fetch/B164AV.png"

define s = Character("Scientist")
define st = Character("Scientist's Thoughts")


# The game starts here.
label project_fetch:

    play music "sounds/Fetch/Sciency.mp3" fadeout 1

    scene lab:
        zoom 1

    show scientist_angry at center:
        zoom .70

    # Chapter 1

    s "Hmm..."
    s "This specimen is altering itself like..."
    s "Like something that resembles a human..."
    s "Very fascinating."

    hide scientist_angry
    show scientist_angry at center with dissolve:
        zoom .70

    s "Alright, Let’s get this over with."
    s "Log zero-zero-one Subject one-six-four"
    s "I’ve received a task from the department saying that this experiment is confidential and that I should be discrete about the experiment with others."

    # Intermission - baby stage

    show scientist_angry at right with dissolve:
        zoom .70
    show baby at left with dissolve:
        zoom .35

    s "I haven’t started the experiment yet it seems as though this experiment is starting to learn the basics..."
    s "Fascinating..."

    show scientist_angry at center with dissolve:
        zoom .70
    hide baby

    s "Log zero-zero-two"
    s "I’m going to try and give a few tests to see where I can start doing some calibrating on the experiment."

    s "It seems to have gained notice on the tests I’ve been giving it..."
    s "Seems more sentient than what I imagined."

    s "Log zero-zero-three"
    s "...experiment seems to be learning pretty quickly"
    s "Even in its early stages..."

    show scientist_surprised at center with dissolve:
        zoom .70
    hide scientist_angry
    s "I-it has now learned to walk!"

    # Intermission

    hide scientist_surprised
    scene black with dissolve
    scene lab with dissolve:
        zoom 1
    show scientist_angry at center with dissolve:
        zoom .70

    s "Log zero-zero-seven"
    s "The experiment has now learned basic principles of what a human can do"
    s "Though..."
    s "The more I think about how fast this experiment can learn"
    s "The more I question what IS inside the experiment to be able to comprehend things very quickly."

    hide scientist_angry
    scene black with dissolve

    "Later that day..."

    scene lab with dissolve:
        zoom 1
    show scientist_angry at center with dissolve:
        zoom .70

    s "Log zero-zero-nine"
    s "I’ve done the usual tests the department has given to me"
    s "Walk, hold, push, and many other..."
    s "Although"
    s "I do have done other things the department didn’t instruct me to do."
    s "I’ll keep tabs on this investigation and be discrete about this as much as possible."

    s "Alright"
    s "Let’s see what we can do about this."

    # Intermission - Black Screen

    hide scientist_angry
    scene black with dissolve

    s "Stay Calm and this won't be long..."
    s "..."
    s "Huh..."
    s "Subject seems to have dealt with the situation more peacefully than what I imagined..."
    s "Fascinating..."

    scene lab with dissolve:
        zoom 1
    show scientist_surprised at right with dissolve:
        zoom .70
    show babyNA at left with dissolve:
        zoom .35

    # Intermission - baby stage without an arm

    s "The subject seems to have recovered quick enough before it can be exposed!"
    s "Wh-what a revelation I’ve come across!"
    s "I need to take note of this."

    s "Log zero-ze-know what..."

    show scientist_angry at right with dissolve:
        zoom .70
    hide scientist_surprised

    s "No..."
    s "The department might see this as something that could disrupt their experimentation..."
    s "Alright then..."
    s "I’ll just write it up first on a piece of paper and investigate the cells of this subject to further assess what I’m dealing with."

    # Intermission

    hide scientist_angry
    scene black

    "The Scientist noticed that the cells are very much alike from that of a human immediately..."

    scene lab with dissolve:
        zoom 1
    show scientist_angry at center with dissolve:
        zoom .70

    s "Hmm..."
    s "Subject seems to have cells that’s very much alike that of a human..."
    s "It seems more likely that a human was used to create such creature..."

    show scientist_surprised at center with dissolve:
        zoom .70
    hide scientist_angry

    s "Just... what am I creating?.."

    show scientist_stressed at center with dissolve:
        zoom .70
    hide scientist_surprised

    s "I need to regroup my thoughts and just call it a day..."

    show scientist_angry at center with dissolve:
        zoom .70
    hide scientist_stressed

    s "Alright, let’s see here..."
    s "It says here that before I leave... I must put the experiment behind the door just outside my this lab..."
    s "What door?..."

    s "Says here that there should be a piston around here somewhere..."
    s "Ah, see it."
    s "Alright, guess that should be it."

    hide scientist_angry
    hide babyNA
    scene black

    # Intermission - Next Day

    "Next day"
    scene lab with dissolve:
        zoom 1
    show scientist_angry at center with dissolve:
        zoom .70

    s "Let’s see where we left off to..."
    s "Ah..."

    s "Log zero-one-zero"
    s "So I’ve been given new instructions from the department to give to the experiment"
    s "As they’ve called it, tests to further enhance its capabilities."

    s "Seems like the department really wants this experiment to be finished fast."
    s "Guess I’ll just run the tests and get back to where I left off to yesterday."

    # Intermission

    show scientist_angry at right with dissolve:
        zoom .70
    show adult at left with dissolve:
        zoom .27

    s "Log zero-one-one"
    s "I’ve run through all the tests the department has given me."
    s "Subject does seem to have perfected every trial it was given."

    s "Alright"
    s "Now that that is over with..."
    s "I guess I could ask the department how they made such specimen."

    # Intermission

    hide scientist_angry
    hide adult
    scene black
    scene lab with dissolve:
        zoom 1
    show scientist_stressed at center with dissolve:
        zoom .70

    s "Seems as if everything I’ve asked them"
    s "It’s like things I already know but..."
    s "When I’ve asked for the specifics"
    s "They just either strayed off from the topic or say that it is classified..."
    s "What sort of department would give a scientist such as myself an assignment without telling them what it is all about..."
    s "It’s stressing me out not knowing what this creature is capable of."

    show scientist_angry at center with dissolve:
        zoom .70
    hide scientist_stressed

    s "Luckily..."
    s "This creature seems to be passive at the moment."

    # Intermission

    show scientist_angry at right with dissolve:
        zoom .70
    show adult at left with dissolve:
        zoom .27

    s "Hmm..."
    s "Log zero-one-four"
    s "Looks like the tests have been running smoothly without having any tangents..."
    s "Though..."
    s "Something seems to be off..."
    s "All the tests I’ve run have been perfectly the same."

    hide adult
    show scientist_surprised at center with dissolve:
        zoom .70
    hide scientist_angry

    s "It’s like the tests limit the creature’s capabilities..."

    hide scientist_surprised
    show scientist_angry at center with dissolve:
        zoom .70

    s "I need to do something about that..."
    s "Tests need to be a bit different from the department’s tests."
    s "Hmm?"
    s "Subject seems to be...copying me..."
    s "We could use this for testing the subject."
    s "Alright, let’s see here..."
    s "I could get something for the subject to copy me."
    s "Huh?.."
    s "Is the creature..."

    show scientist_surprised at center with dissolve:
        zoom .70
    hide scientist_angry

    s "Reading my materials?"
    s "Fascinating...oh...uhh...Log zero-one-five"

    show scientist_angry at center with dissolve:
        zoom .70
    hide scientist_surprised

    s "Subject seems to have picked up some of my works and have begun to read it without any prior knowledge of some advance vocabulary."
    s "I guess it’s good that the creature started on my work called “Basic Necessities”."
    s "While the creature is on that"
    s "I’ll observe the creature and gain some new knowledge as it does its thing."

    s "Wait..."
    s "It's like..."

    show scientist_surprised at center with dissolve:
        zoom .70
    hide scientist_angry

    s "It's scanning the pages..."
    s "It’s not reading the book, it-it's scanning it!"
    s "And it’s going through all my works, one by one."

    show scientist_angry at center with dissolve:
        zoom .70
    hide scientist_surprised

    s "Wait"
    s "How ‘bout this one then."
    s "Huh"
    s "I guess it's not shy hating other’s works."
    s "I wonder why"
    s "Though it seems like the creature has a fascination with my works."
    s "Wait"

    show scientist_surprised at center with dissolve:
        zoom .70
    hide scientist_angry

    s "It’s able to distinguish which are mine and which are not?!"

    s "Log zero-one-six"

    show scientist_angry at center with dissolve:
        zoom .70
    hide scientist_surprised

    s "Subject seems to be a lot smarter than what I imagined."
    s "It is able to discern not just objects or words"
    s "It can be able to discern properties."

    s "What a fascinating little subject."
    s "B-but why is the subject only interested in my works?"

    show scientist_stressed at center with dissolve:
        zoom .70
    hide scientist_angry

    s "Why?..."
    s "Is it, because it sees me as it’s creator?"
    s "Or maybe because I’m its only contact."
    s "But why me?"

    hide scientist_stressed
    scene black with dissolve

    "Although as the scientist questions the creature’s behaviour..."
    "He did not realise for the reason..."
    "Is just under his nose."

    # Chapter 2

    scene lab with dissolve:
        zoom 1
    show scientist_angry at center with dissolve:
        zoom .70

    s "Log zero-four-eight"
    s "Creature seems to have a rough idea of moving, making decisions, solve problems, though..."
    s "I do wonder why this creature doesn’t have a mouth."

    # Branch tentative

    s "Although the creature’s movements are excellent, they do seem familiar..."

    # Intermission

    hide scientist_angry
    show scientist_angry at center with dissolve:
        zoom .70

    s "Log zero-five-five"
    s "I have noticed while doing my research on the creature I’m experimenting that it is copying everything that I’ve done."
    s "It is trying to become my own doppelganger..."

    s "I do seem to remember of an old story regarding the name of the project I'm working on..."
    s "Fetch"
    s "Now where have I heard of fetch in stories?..."
    s "Oh well... that doesn't seem to matter right now"

    # Intermission

    s "Log zero-six-two"
    s "I’ve researched on the cells I’ve acquired during my previous experiment regarding this creature."
    s "It seems that the cells of this creature are not “like” of a human but “that” of a human."

    show scientist_surprised at center with dissolve:
        zoom .70
    hide scientist_angry

    s "This came from the experiment I used to have done..."

    show scientist_angry at center with dissolve:
        zoom .70
    hide scientist_surprised

    s "I need to come find the files from that experiment."

    show scientist_angry at center with dissolve:
        zoom .70

    s "I need to find answers..."
    s "Although..."
    s "I know that this won’t end well for me."

    hide scientist_angry
    scene black

    "The scientist felt that once the experiment is over"
    "Something terrible might occur to him."

    # Intermission - Later that Day

    "Later that day"

    scene lab with dissolve:
        zoom 1
    show scientist_angry at center with dissolve:
        zoom .70

    s "Alright"
    s "I’ll keep the creature occupied for the time being while I find the files from that experiment."

    scene black

    "*locks door to prevent the creature from leaving the room*"

    # Intermission - Library

    scene library:
        zoom .40
    show scientist_angry at center with dissolve:
        zoom .70

    s "JD...JD...J..ah, found it."
    s "Experiment no. 537, John Doe..."
    s "Wait... what happened here?"

    show scientist_stressed at center with dissolve:
        zoom .70
    hide scientist_angry

    s "Everything here has been placed under classified or erased..."
    s "It’s like they’re trying to hide information regarding experiment 537."

    s "Alright"
    s "I can think this through..."

    show scientist_angry at center with dissolve:
        zoom .70
    hide scientist_stressed

    s "What is the department even planning with this project."
    s "What is it?"
    s "What could it be?"
    s "I’ve never tackled such a hurdle like this before..."

    s "Wait"
    s "Where’re the files under the experiment I’m doing?"

    show scientist_surprised at center with dissolve:
        zoom .70
    hide scientist_angry

    s "What's going on here?..."

    show scientist_stressed at center with dissolve:
        zoom .70
    hide scientist_surprised

    s "All files that are classified should be here..."
    s "Ha... just what is this..."
    s "I don’t even know why I’m doing this."

    show scientist_angry at center with dissolve:
        zoom .70
    hide scientist_stressed

    s "hmm?.."
    s "What's this..."
    s "A door?"
    s "I-it's trampled behind all these books..."

    hide scientist_angry

    "*Removes the books blocking the door*"

    show scientist_angry at center with dissolve:
        zoom .70

    s "T-this... wasn't here before..."

    hide scientist_angry

    "*Opens door*"

    scene black with fade

    # Intermission

    # show creature reading and using all the scientist’s belongings

    # Chapter 3

    scene library with dissolve:
        zoom .40
    show scientist_stressed at center with dissolve:
        zoom .70

    s "Wha-what is this..."
    s "I'm just lost for words now..."
    s "Not only is the creature came from experiment 537 but it also features the experiment’s background info..."
    s "W-wait..."

    show scientist_surprised at center with dissolve:
        zoom .70
    hide scientist_stressed

    s "I've experimented on a criminal?!"
    s "W-what is this... i-ide... this person steals people's identity?!"
    s "What!?"

    show scientist_stressed at center with dissolve:
        zoom .70
    hide scientist_surprised

    s "Wait"
    s "If this guy steals the identity of a person..."
    s "Then that would mean..."

    show scientist_surprised at center with dissolve:
        zoom .70
    hide scientist_stressed

    s "*gasp*"
    s "They’re creating a creature that can copy other people’s identity..."
    s "Kind of like a doppelganger..."

    show scientist_stressed at center with dissolve:
        zoom .70
    hide scientist_surprised

    s "Ah, I finally found the files for the project I've been working on"
    s "So... then..."
    s "This... this just proves my point even more!"
    s "And also... project Fetch is from a folklore..."

    show scientist_angry at center with dissolve:
        zoom .70
    hide scientist_stressed

    s "An Irish folklore..."
    s "If I remember correctly, it was about some sort of supernatural double or a living apparition..."
    s "Then that would mean that the creature I’ve been working on is trying to create a double out of me..."
    s "The creature is something not to be taken lightly even yet..."
    s "Due to its form and idea taken from something dangerous"
    s "It can be considered something inhumane now..."
    s "Or like... a monster..."

    show scientist_stressed at center with dissolve:
        zoom .70
    hide scientist_angry

    s "If all the creature wants is to take my identity..."
    s "Then that could mean that this is far more greater than the department’s power..."
    s "Huh?"

    show scientist_angry at center with dissolve:
        zoom .70
    hide scientist_stressed

    s "What's this..."
    s "“No one shall go near experiment 164. No one shall go near the scientist working on experiment 164.”"
    s "Who's this intended to?"
    s "Hmm..."
    s "I’ve noticed that ever since I’ve started working on this experiment"
    s "I’ve not seen that many scientists going near my lab."
    s "Wait..."

    show scientist_stressed at center with dissolve:
        zoom .70
    hide scientist_angry

    s "Working on the experiment..."
    s "Aren’t I almost finished with the experiment?.."
    s "Oh no...."
    s "Does that also mean that i-it is also almost finished copying me?"
    s "But isn’t still looking inhuman?"
    s "Could it mean that there is some sort of way for it to transform?.."
    s "No… that wouldn’t be possible with all the experiments I’ve tested."
    s "Then..."

    show scientist_surprised at center with dissolve:
        zoom .70
    hide scientist_stressed

    s "A transfer!?.."
    s "Like that of the folklore!?.."

    show scientist_stressed at center with dissolve:
        zoom .70
    hide scientist_surprised

    s "..."
    s "Oh no..."
    s "Then that would mean that what awaits me behind the doors of my lab is no longer a creature under my supervision but a monster"
    s "Trying to take my body."

    show scientist_angry at center with dissolve:
        zoom .70
    hide scientist_stressed

    s "I need to kill it before… before it kills me."

    scene black with dissolve

    # Intermission

    "Later..."

    "The scientist then went behind the monster and went to grab the nearest possible sharp object he could find."

    s "*whispers to himself* I’m sorry..."
    s "I don’t want to do this to you..."

    "Though, what the scientist would never have imagined..."
    "Was that the creature..."
    "Felt like the scientist was about to kill his own child."

    s "I... I... I just can’t..."

    # Intermission - Monster sees the scientist's about to kill it

    "Although the scientist wasn't able to attack the monster..."
    "The monster does sees this and decided to kill the scientist instead"

    s "..."
    s "Wa-wait..."
    s "NO!!!"

    "The scientist never did know what is going on inside the monster's head..."
    "And due to that..."
    "It led to the scientist's demise because..."
    "An imprint was left on the monster."
    "The monster never had trusted the scientist in the beginning."

    # Chapter 4

    scene last

    "The scientist then woke up in a dark room, unable to move."
    "A light from a small gap is shed upon the scientist body and revealed to the scientist that their body has come from the creature the scientist has created."

    st "Huh?.."
    st "What’s happening to my body?.."

    "The scientist noticed that the body was all mangled up and torn apart."

    st "I... I can’t move..."
    st "I’ve healed... but I'm torned apart..."

    "From the small gap"
    "It lets the scientist hear voices that seem familiar."
    "Upon closer inspection"
    "It was their own voice and body that someone now uses."

    st "Is… is that my body?!.."
    st "H-how?!.."
    s "*gasp*"
    st "The creature..."

    "The scientist tried to speak but was not able to..."
    "Since the monster never had a mouth to begin with..."
    "The scientist then realized that the creature was designed to be mute."
    "The scientist then thought that the scientist fell into the hands of the company conducting the project since the company had planned all of this until the very moment the scientist found themselves in currently."

    "The scientist has come to realize that Project Fetch was a success."

    "Fin"

    "Credits: "
    "Music: Inspiring Science Technology Documentary by R-Production"
    "Background: Panait Alexandra from Pinterest"

    return
