define yggdrasil_scientist = Character("YGGDRASIL Scientist")
define yggdrasil = Character("YGGDRASIL")
define ygg_corp_ceo = Character("YGG Corps CEO")
define yggdrasil_epiloque = Character("EPILOQUE")

image bg_yggdrasil_0 = im.Scale("yggdrasil/bg_yggdrasil_0.jpg", 1280, 720)
image bg_yggdrasil_1 = im.Scale("yggdrasil/bg_yggdrasil_1.jpg", 1280, 720)
image bg_yggdrasil_12 = im.Scale("yggdrasil/bg_yggdrasil_12.jpg", 1280, 720)
image bg_yggdrasil_45 = im.Scale("yggdrasil/bg_yggdrasil_45.jpg", 1280, 720)
image bg_yggdrasil_55 = im.Scale("yggdrasil/bg_yggdrasil_55.jpg", 1280, 720)
image bg_yggdrasil_109 = im.Scale("yggdrasil/bg_yggdrasil_109.jpg", 1280, 720)
image bg_yggdrasil_corp = im.Scale("yggdrasil/bg_yggdrasil_109.jpg", 1280, 720)
image bg_yggdrasil_epiloque = im.Scale("yggdrasil/bg_yggdrasil_epiloque.jpg", 1280, 720)

image yggrasil_seed = im.Scale("yggdrasil/yggrasil_seed.jpg", 480, 360)
image yggrasil_fruit = im.Scale("yggdrasil/yggrasil_fruit.jpg" , 480, 360)
image yggrasil_market = im.Scale("yggdrasil/yggrasil_market.jpg" , 480, 360)
image yggrasil_demand = im.Scale("yggdrasil/yggrasil_demand.jpg" , 480, 360)

label project_yggdrasil:

    scene bg_yggdrasil_0
    
    yggdrasil_scientist "PROJECT YGGDRASIL LOG 0."
    yggdrasil_scientist "As we decided, the fetus has morphed and squashed itself"
    
    show yggrasil_seed at truecenter
    yggdrasil_scientist "into a still tiny seed."

    yggdrasil_scientist "The seed may look like an ordinary everyday seed; however, it shall grow into a huge, beautiful tree that provides various fruits to no end."
    yggdrasil_scientist "This tree shall be called YGGDRASIL."

    scene bg_yggdrasil_1
    yggdrasil_scientist "PROJECT YGGDRASIL LOG 1."
    yggdrasil_scientist "YGGDRASIL was buried beneath the ground of an open plain."
    yggdrasil_scientist "It will grow under the bright blue skies, surrounded by the green grass shifting through the gentle breeze."
    yggdrasil_scientist "Here, YGGDRASIL will be growed and observed."

    scene bg_yggdrasil_12
    yggdrasil_scientist "PROJECT YGGDRASIL LOG 12."
    yggdrasil_scientist "The seed now grew upwards into the size of a regular sprout."
    yggdrasil_scientist "However, it is expected to grow even larger than we imagine."
    yggdrasil_scientist "Despite its relatively normal appearance, it shakes erratically."
    yggdrasil_scientist "Winds surrounding it seems to breeze erratically as well."
    yggdrasil_scientist "It is almost as if YGGDRASIL has taken a conscience of its own."

    scene bg_yggdrasil_45
    yggdrasil_scientist "PROJECT YGGDRASIL LOG 45." 
    yggdrasil_scientist "From sprouts, it has now grown into a simple tree."
    yggdrasil_scientist "Violent behavior it exhibited earlier has creased."
    yggdrasil_scientist "However, in turn, its conscience is now ever so present."
    yggdrasil_scientist "It has begun to speak and communicate in a celestial manner, almost as if a man from the skies was speaking."

    yggdrasil "\"PROFESSOR, WHAT IS MY PURPOSE?\""
    yggdrasil_scientist "\"To be the ultimate life giver. The salvation of all lifeforms!\""

    scene bg_yggdrasil_55
    yggdrasil_scientist "PROJECT YGGDRASIL LOG 55."
    show yggrasil_fruit at truecenter
    yggdrasil_scientist "YGGDRASIL has finally blessed us with its joyous fruit."
    yggdrasil_scientist "Such fruits were delicious to no end and filling to its core, as expected of YGGDRASIL."
    yggdrasil_scientist "The production of these fruits is only going faster and faster."
    hide yggrasil_fruit
    yggdrasil_scientist "However, the grass just right by seems to be whiten out."
    show yggrasil_market at truecenter
    yggdrasil_scientist "Regardless, I have begun negotiations with businesses to sell and distribute the fruits."

    scene bg_yggdrasil_109
    yggdrasil_scientist "PROJECT YGGDRASIL LOG 109."
    show yggrasil_demand at truecenter
    yggdrasil_scientist "The demand seems to be growing more and more by the day."
    hide yggrasil_demand
    yggdrasil_scientist "Yet, in the midst of its success, YGGDRASIL seems to be deteriorating. It no longer grows and bark only darkens."
    yggdrasil_scientist "The grass surrounding only seems to whiten even further. But, no matter, all that matters is its beared fruit."
    yggdrasil_scientist "Everything was fine" 
    yggdrasil_scientist "until I decided to bite into a dropped fruit."

    yggdrasil_scientist "\"YGGDRASIL! WHAT IS THIS!?\""
    yggdrasil "\"Professor, the quality of my fruit will degrade further. WE MUST STOP!\""
    yggdrasil_scientist "\"NO! JUST WHEN THE PEOPLE, OUR CLIENTS, CARVE FOR OUR FRUIT. WE MUST SATISFY OUR HUNGER\""

    scene bg_yggdrasil_corp
    ygg_corp_ceo "YGGDRASIL CORP LOG ????"
    ygg_corp_ceo "THE DAMN TREE'S PRODUCTION IS ONLY GETTING WORSE, WORSE, AND WORSE."
    ygg_corp_ceo "WE WILL NEVER HAVE WHAT WE WANT WITH THIS TREE."

    yggdrasil "\"Professor, PLEASE OPEN YOUR EYES!\""
    ygg_corp_ceo "\"I TOLD YOU TO CALL ME BOSS\""
    yggdrasil "\"Boss, please look around! The more we continue the more life will be…\""
    ygg_corp_ceo "\"SHUT UP! YOU ARE A FACTORY THROUGH AND THROUGH!\""

    scene bg_yggdrasil_epiloque
    yggdrasil_epiloque "Green calm plains were nowhere to be seen."
    yggdrasil_epiloque "Yet, no life, even humanity can be seen."
    yggdrasil_epiloque "What remains is barren lands that stretch beyond the eye can see."



