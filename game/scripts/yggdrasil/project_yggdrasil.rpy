init python:
    renpy.music.register_channel("background_noise", "sfx")

    def yggdrasil_voice(event, interact=True, **kwargs):
        if event == "show_done":
            renpy.sound.play("/sounds/yggdrasil/tree_voice.wav")
        elif event == "end":
            renpy.sound.stop()

image bg_yggdrasil_0 = im.Scale("yggdrasil/bg_yggdrasil_0.png", 1280, 720)
image bg_yggdrasil_1 = im.Scale("yggdrasil/bg_yggdrasil_1.png", 1280, 720)
image bg_yggdrasil_2 = im.Scale("yggdrasil/bg_yggdrasil_2.png", 1280, 720)
image bg_yggdrasil_3 = im.Scale("yggdrasil/bg_yggdrasil_3.png", 1280, 720)
image bg_yggdrasil_4 = im.Scale("yggdrasil/bg_yggdrasil_4.png", 1280, 720)

image bg_yggdrasil_seed = im.Scale("yggdrasil/yggdrasil_seed.png", 1280, 720)
image bg_yggdrasil_seed_ground = im.Scale("yggdrasil/yggdrasil_seed_ground.png", 1280, 720)
image bg_yggdrasil_market = im.Scale("yggdrasil/yggdrasil_market.jpg" , 1280, 720)

image yggdrasil young = "yggdrasil/yggdrasil_young.png"
image yggdrasil mature = "yggdrasil/yggdrasil_mature.png"
image yggdrasil fruit = "yggdrasil/yggdrasil_fruit.png"
image yggdrasil deteriorate 0 = "yggdrasil/yggdrasil_deteriorate_0.png"
image yggdrasil deteriorate 1 = "yggdrasil/yggdrasil_deteriorate_1.png"

define yggdrasil_scientist = Character("YGGDRASIL Scientist")
define yggdrasil = Character("YGGDRASIL", callback=yggdrasil_voice)
define ygg_corp_ceo = Character("YGG Corps CEO")
define yggdrasil_epiloque = Character("EPILOQUE")

label project_yggdrasil:
    
    scene bg_yggdrasil_0
    with fade
    
    yggdrasil_scientist "PROJECT YGGDRASIL LOG 0."
    play sound "sounds/yggdrasil/machine_power_up.wav"
    yggdrasil_scientist "As we decided, we'll fire up the machines and ready the fetus to transform"
    stop sound
    play sound "sounds/yggdrasil/machine_power_finish.wav"

    scene bg_yggdrasil_seed
    with fade
    yggdrasil_scientist "into a still tiny seed."
    yggdrasil_scientist "The seed may look like an ordinary everyday seed; however, it shall grow into a huge, beautiful tree that provides various fruits to no end."
    yggdrasil_scientist "This tree shall be called YGGDRASIL."

    scene bg_yggdrasil_seed_ground
    with fade
    play music "sounds/yggdrasil/calm_music.mp3" loop

    yggdrasil_scientist "PROJECT YGGDRASIL LOG 1."
    yggdrasil_scientist "YGGDRASIL was buried beneath the ground of an open plain."

    scene bg_yggdrasil_1
    play background_noise "sounds/yggdrasil/plains_winds.wav" fadein 1.0 fadeout 1.0 loop
    yggdrasil_scientist "It will grow under the bright blue skies, surrounded by the green grass shifting through the gentle breeze."
    yggdrasil_scientist "Here, YGGDRASIL will be growed and observed."

    scene bg_yggdrasil_1
    with fade

    show yggdrasil young

    yggdrasil_scientist "PROJECT YGGDRASIL LOG 12."
    yggdrasil_scientist "The seed now grew upwards into the size of a small young tree."
    yggdrasil_scientist "However, it is expected to grow even larger than we imagine."
    yggdrasil_scientist "Despite its relatively normal appearance, it shakes erratically."
    yggdrasil_scientist "Winds surrounding it seems to breeze erratically as well."
    yggdrasil_scientist "It is almost as if YGGDRASIL has taken a conscience of its own."

    scene bg_yggdrasil_1
    with fade

    show yggdrasil mature

    yggdrasil_scientist "PROJECT YGGDRASIL LOG 45." 
    yggdrasil_scientist "From sprouts, it has now grown into a mature tree."
    yggdrasil_scientist "Erratic behavior it exhibited earlier has creased."
    yggdrasil_scientist "However, in turn, its conscience is now ever so present."
    yggdrasil_scientist "It has begun to speak and communicate in a celestial manner, almost as if a man from the skies was speaking."

    yggdrasil "\"PROFESSOR, WHAT IS MY PURPOSE?\""
    yggdrasil_scientist "\"To be the ultimate life giver. The salvation of all lifeforms!\""

    scene bg_yggdrasil_1
    with fade

    show yggdrasil fruit

    yggdrasil_scientist "PROJECT YGGDRASIL LOG 55."
    yggdrasil_scientist "YGGDRASIL has finally blessed us with its joyous fruit, mass producing a multitude of various fruit."
    yggdrasil_scientist "Yet, such fruits were delicious to no end and filling to its core, as expected of YGGDRASIL."
    yggdrasil_scientist "The production of these fruits is only going faster and faster."
    yggdrasil_scientist "Such potential should not go to waste" 

    scene bg_yggdrasil_market
    play background_noise "sounds/yggdrasil/market.wav" fadeout 1.0 loop
    yggdrasil_scientist "As such, I have begun negotiations with businesses to sell and distribute the fruits."

    scene bg_yggdrasil_2
    with fade
    stop music
    play background_noise "sounds/yggdrasil/strong_winds.wav" fadein 1.0 fadeout 1.0 loop

    show yggdrasil deteriorate 0

    yggdrasil_scientist "PROJECT YGGDRASIL LOG 109."
    yggdrasil_scientist "The demand seems to be growing more and more by the day."
    yggdrasil_scientist "Yet, in the midst of its success, YGGDRASIL seems to be deteriorating. It no longer grows and leaves have begun to fall."
    yggdrasil_scientist "Even the surrounding area seems to deteriorate too. But, no matter, all that matters is its beared fruit."
    yggdrasil_scientist "Everything was fine"
    play sound "sounds/yggdrasil/bite.wav" 
    yggdrasil_scientist "until I decided to bite into a dropped fruit."

    play music "sounds/yggdrasil/angry_music.mp3" loop
    play sound "sounds/yggdrasil/angry_sound.wav"
    yggdrasil_scientist "\"YGGDRASIL! WHAT IS THIS!?\""
    yggdrasil "\"Professor, the quality of my fruit will degrade further. WE MUST STOP!\""
    yggdrasil_scientist "\"NO! JUST WHEN THE PEOPLE, OUR CLIENTS, CARVE FOR OUR FRUIT. WE MUST SATISFY OUR HUNGER\""

    scene bg_yggdrasil_3
    with fade
    
    show yggdrasil deteriorate 1

    ygg_corp_ceo "YGGDRASIL CORP LOG ????"
    ygg_corp_ceo "THE DAMN TREE'S PRODUCTION IS ONLY GETTING WORSE, WORSE, AND WORSE."
    ygg_corp_ceo "WE WILL NEVER HAVE WHAT WE WANT WITH THIS TREE."

    yggdrasil "\"Professor, PLEASE OPEN YOUR EYES!\""
    ygg_corp_ceo "\"I TOLD YOU TO CALL ME BOSS\""
    yggdrasil "\"Boss, please look around! The more we continue the more life will be…\""
    ygg_corp_ceo "\"SHUT UP! YOU ARE A FACTORY THROUGH AND THROUGH!\""

    scene bg_yggdrasil_4
    with fade
    stop music
    play background_noise "sounds/yggdrasil/desolate_winds.wav" fadein 1.0 fadeout 1.0 loop

    hide yggdrasil

    yggdrasil_epiloque "Green calm plains were nowhere to be seen."
    yggdrasil_epiloque "Yet, no life, even humanity can be seen."
    yggdrasil_epiloque "What remains is barren lands that stretch beyond the eye can see."



