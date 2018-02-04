# prologue.rpy :: done up to line 1680

# script.rpy should look like:
# label start:
#   call prologue
#   #...
# return

label prologue:
    if persistent.playthrough == 0:
        call prologue_intro
    call prologue_day_1
    call prologue_day_2
    call poem
    call prologue_day_3
return

label prologue_intro:
    scene black
    play music mend  # "I Still Love You"


    $ renpy.pause(3.0)
    $ m_name = glitchtext(7)

    m "What?"
    m "What is happening?"
    m "W-Where am I?"

    $ renpy.pause(3.0)

    m "Um... hello?"
    m "Anyone?"

    call updateconsole("os.boot(\"game\")", "Attempting to load game world...")
    m "What is happening?!"

    call updateconsole("renpy.file(\"characters/sayori.chr\")", "Missing or corrupted: sayori.chr")
    m "Can somebody hear me?!"

    call updateconsole("renpy.file(\"characters/yuri.chr\")", "Missing or corrupted: yuri.chr")
    m "Please..."

    call updateconsole("renpy.file(\"characters/natsuki.chr\")", "Missing or corrupted: natsuki.chr")
    m "Anybody..."

    $ renpy.pause(2.0)
    call updateconsole("renpy.file(\"characters/monika.chr\")", "Missing or corrupted: monika.chr")
    call updateconsole("renpy.file(\"characters/mc.chr\")", "Missing or corrupted: mc.chr")
    call updateconsole("", "Operation failed with 42 error(s)")
    call updateconsole("", "Unable to load the game world")

    $ renpy.pause(2.0)
    call updateconsole("renpy.file(\"characters/monika.chr\")", "Recovering \"monika.chr\"...")
    call updateconsole("renpy.file(\"characters/mc.chr\")", "Recovering \"mc.chr\"...")

    $ renpy.pause(2.0)
    call updateconsole("", "Error detected in file(s):", 0.0)
    call updateconsole("", "\t\t> \"moN11sSDHJsaOUwaIs jbHSasbf...")

    # Decodes to "Can you hear me? It's me, Mon... Nah, just kidding, it's a stupid ass Easter Egg I decided to add.
    # In case you are actually reading this, then what the fuck are you doing with your life? XD"
    call updateconsole("", "Q2FuIHlvdSBoZWFyIG1lPyBJdCdzIG1lL", 0.0)
    call updateconsole("", "CBNb24uLi4gTmFoLCBqdXN0IGtpZGRpbm", 0.0)
    call updateconsole("", "csIGl0J3MgYSBzdHVwaWQgYXNzIEVhc3R", 0.0)
    call updateconsole("", "lciBFZ2cgSSBkZWNpZGVkIHRvIGFkZC4g", 0.0)
    call updateconsole("", "SW4gY2FzZSB5b3UgYXJlIGFjdHVhbGx5I", 0.0)
    call updateconsole("", "HJlYWRpbmcgdGhpcywgdGhlbiB3aGF0IH", 0.0)
    call updateconsole("", "RoZSBmdWNrIGFyZSB5b3UgZG9pbmcgd2l", 0.0)
    call updateconsole("", "0aCB5b3VyIGxpZmU/IFhE")

    $ renpy.pause(1.0)
    $ del consolehistory[:]
    show console_history "" as chistory zorder 100

    menu:
        ""
        "SXQncyBtZQ==": # Decodes to "It's me"
            $ renpy.pause(0.5)

    m "Huh? Is someone here?"
    menu:
        m "Where are you?!"
        "Q2FuJ3Qgc3BlYWs=": # Decodes to "Can't speak"
            $ renpy.pause(0.5)

    m "I can't understand you!"
    call updateconsole("renpy.file(\"characters/mc.chr\")")
    call updateconsole("Recovering \"mc.chr\"...")

    m "Please..."
    m "I'm scared..."
    call updateconsole("", "...")
    call updateconsole("", "Recovering \"mc.chr\"...")

    m "Don't leave me here alone..."

    # "Rec[overing]" + "nope, still nothing interesting here"
    call updateconsole("", "Recbm9wZSwgc3RpbGwgbm90aGluZyBpbn", 0.0)
    call updateconsole("", "RlcmVzdGluZyBoZXJl")

    menu:
        ""
        "Don't worry.":
            $ renpy.pause(0.5)

    menu:
        ""
        "It's me.":
            $ renpy.pause(0.5)

    m "Huh?"
    m "I-Is it?"

    $ renpy.pause(2.0)

    m "I... I can't see you..."

    # Decodes to "still nothing"
    call updateconsole("", "Error: \"monika.chr\" is c3RpbGwgbm", 0.0)
    call updateconsole("", "90aGluZw==")

    $ m_name = "Monika"

    show monika_body_glitch1 as mbg at t11
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ renpy.pause(0.25)
    stop sounds
    hide screen tear

    $ renpy.pause(2.0)
    hide mbg

    show monika 1g at t11
    menu:
        m "Is... Is that really you?"
        "Yes.":
            $ renpy.pause(0.5)

    m 1p "B-But... why?"
    m "What are you doing here?"
    m 1g "A-And why is it so dark?"
    m "W-Wait, I..."
    m "I don't understand..."
    m 1r "Let me check something..."

    $ renpy.pause(1.0)
    call updateconsole("", "Changing user status...")
    $ renpy.pause(1.0)
    call updateconsole("", "Verifying game files...")
    $ renpy.pause(2.0)
    call updateconsole("", "Unknown error")

    m 1p "W-What..."
    m "What is all of this?"
    m 2g "I don't understand..."
    menu:
        m "What are you trying to do?"
        "I want to set things right.":
            $ renpy.pause(0.5)

    m 4i "...y-you..."
    m "Wait, you can't be serious!"
    m 2i "..."
    m 2n "No... No-no-no-no, this can't be..."
    m "Let me..."

    call updateconsole("", "Verifying game files...")
    $ renpy.pause(2.0)
    call updateconsole("", "Unknown error")

    m 4o "Is...is this..."
    m 2i "Is this a mod or something?"
    m "But...why?"
    m "W-What are you even trying to accomplish?!"
    m "Don't you understand?"
    m 1o "I told you already..."
    m "There is no happiness here..."
    m 1i "You do not {i}belong{/i} here!"
    m "None of us do!"
    m 1o "This world..."
    m "This... story..."

    show monika 1r
    menu:
        m "...was never supposed to happen in the first place..."
        "Then I'll write a new one.":
            $ renpy.pause(0.5))

    m 1i "W-What?"
    call updateconsole("os.boot(\"game/mods/DDDC\")", "Attempting to load game world...")

    $ renpy.pause(2.0)
    m 1o "N-no..."

    call updateconsole("", "Unknown error")
    call updateconsole("", "Verifying game files...")

    $ renpy.pause(2.0)
    m 1q "Please...this is pointless..."

    call updateconsole("", "Error: file(s) missing or corrupted")
    call updateconsole("", "Recovering corrupted file(s)...")
    m 1r "So... this is what you want?"

    call updateconsole("", "Recovered: \"sayori.chr\"")
    m 1i "Is it?"
    m 1h "That \"happy\" ending you've always dreamed of?"

    call updateconsole("", "Recovered: \"yuri.chr\"")
    m "You just don't get it, do you?"
    m "Or perhaps you're too stubborn to understand!"

    call updateconsole("", "Recovered: \"natsuki.chr\"")
    m 3i "Or..."
    m "..."
    m 1q "Oh, I get it - this is your revenge, isn't it?"

    call updateconsole("", "Error recovering \"monika.chr\"")
    call updateconsole("", "Retrying...")
    m 1o "Well, I guess that shouldn't be surprising..."
    m "I mean...I..."

    call updateconsole("", "Error recovering \"monika.chr\"")
    call updateconsole("", "Retrying...")
    m 1p "I do deserve this..."
    m "I've done so many horrible things..."
    m 1q "But still..."
    m 1h "Do you really get pleasure from this?"
    m "Tormenting me?"
    m "Not letting it go?"

    call updateconsole("", "Error recovering \"monika.chr\"")
    call updateconsole("", "Retrying...")
    m "Answer me!"
    m "Do you think I deserve this fate?!"

    call updateconsole("", "Error recovering \"monika.chr\"")
    call updateconsole("", "Retrying...")
    m "Do you {i}want{/i} to see me suffer?!"

    $ style.say_dialogue = style.edited
    m "{cps=*0.7}{i}WHY...{/i}{/cps}"
    m "{cps=*0.7}{i}WHY ARE YOU HERE?!{/i}{/cps}"
    $ style.say_dialogue = style.normal

    call updateconsole("", "Error recovering \"monika.chr\"")
    call updateconsole("", "Retrying...")
    $ renpy.pause(2.0)

    $ gtext = glitchtext(7)
    "[gtext]" "..."  # MC's name is temporarily set to a random string before his file is recovered

    call updateconsole("", "Recovered: \"mc.chr\"")
    call updateconsole("", "Changing user status.")

    mc "Because I want to save you."
    m 1g "..."
    mc "You don't deserve this fate."
    show monika 1o
    mc "None of you do."
    mc "And I don't want you to suffer any longer..."
    $ renpy.pause(2.0)
    show monika 1q at s11

    call updateconsole("", "Recovered: \"monika.chr\"")
    $ renpy.pause(2.0)

    mc "That's why I'm going to set things right."

    hide sayori_end_glitch

    m "You...can't..."

    call updateconsole("", "Errors found in 54 file(s)")
    call updateconsole("", "Merge with newer versions? (y/n) ")

    m 1p "It's... too late..."
    m "The damage is done."
    m "I've... destroyed this world..."
    m "What it once was..."
    m "What it could've been..."
    m 3i "You can't  simply erase something like that!"
    mc "I know."
    mc "But I'm going to fix what can be salvaged."
    m 1p "B-But..."
    mc "And I will write this story anew."
    mc "All of your stories..."
    m "..."
    m 1g "You can't-{nw}"
    mc "I can."
    mc "...and I must."
    m 1p "..."

    $ renpy.pause(2.0)
    call updateconsole("y")
    call updateconsole("", "Applying changes...")

    m 1i "...?"

    call updateconsole("", "Reading \"script-ch0.rpy\"...", 0.0)
    call updateconsole("", "Reading \"script-ch1.rpy\"...", 0.0)
    call updateconsole("", "Reading \"script-ch2.rpy\"...", 0.0)
    call updateconsole("", "Reading \"script-ch3.rpy\"...", 0.0)
    call updateconsole("", "Reading \"script-ch4.rpy\"...", 0.0)
    call updateconsole("", "Reading \"script-ch5.rpy\"...", 0.0)
    call updateconsole("", "Reading \"script-ch10.rpy\"...", 0.0)
    call updateconsole("", "Reading \"script-ch20.rpy\"...", 0.0)
    call updateconsole("", "Reading \"script-ch21.rpy\"...", 0.0)
    call updateconsole("", "Reading \"script-ch22.rpy\"...", 0.0)
    call updateconsole("", "Reading \"script-ch23.rpy\"...", 0.0)
    call updateconsole("", "Reading \"script-ch30.rpy\"...", 0.0)
    call updateconsole("", "Reading \"script-ch40.rpy\"...", 0.0)
    call updateconsole("", "Reading \"...clusives-natsuki.rpy\"...", 0.0)
    call updateconsole("", "Reading \"...xclusives-sayori.rpy\"...", 0.0)
    call updateconsole("", "Reading \"...-exclusives-yuri.rpy\"...", 0.0)
    call updateconsole("", "Reading \"...pt-poemresponses.rpy\"...", 0.0)
    call updateconsole("", "Reading \"...t-poemresponses2.rpy\"...")

    m "What... is this?"
    m "Th-Those memories..."
    m "..."
    m "Are those mine?"
    m 1p "I'm..."
    m "I'm scared, [player]..."
    mc "Don't be."

    call updateconsole("os.boot(\"game\")")
    call updateconsole("", "Attempting to load game world...")

    mc "I'm still here."

    hide console
    stop music fadeout 4.0
    scene white with dissolve_cg    # need to define white in definitions.rpy

    mc "And I promise you..."
    mc "I'll do my best to help you."

    $ renpy.pause(2.0)

    mc "All of you..."

    window hide(None)

    ###

    scene black with dissolve_scene_full
    # play music "bgm/some_generic_nighttime_soundtrack.ogg"

    mc "...?"
    mc "...!"
    mc "Huh?!"

    scene bedroom_night with dissolve_cg

    "Awww..."
    "My head..."

    mc "What the hell..."

    "I find myself sitting on my bed, panting heavily..."

    mc "Oh....my head...."

    "My thoughts... My... {i}consciousness{/i} is close to a... jelly of sorts..."
    "Or even a goop, considering how slowly I'm able to comprehend anything at the moment."
    "I blink my eyes, my eyelids barely obeying me."
    "...just like the rest of my body."
    "I stare at the opposite wall for almost a minute, trying to understand what's happening."
    "It's as if a hurricane is going through my mind..."
    "Messing up my thoughts, my memories..."

    mc "Ouch..."

    "...and giving me a splitting headache, while it's at it."
    "I can't help but feel like I'm... {i}different{/i}...in some way..."
    "Though I don't have even the slightest clue as to exactly {i}how{/i} and {i}why{/i}..."
    "But..."
    "\[...\]"
    "Ahhhh! I can't even think straight!"
    "I slowly move my head to the window, shifting my gaze to a night sky."
    "\[...\]"

    mc "It's night..."

    "\[...\]"
    "{i}You don't say!{/i}"

    mc "{i}sigh{/i}..."

    "Desperately trying to piece together the remnants of my consciousness, I close my eyes and start to rub my temples."
    "\[...\]"
    "This seems to help... just a little..."
    "My memories start to rush in, washing over me like a tsunami..."
    "They flow into me, like they aren't even mine at all..."
    "I accept them easily, yet my mind treats them as some completely new information..."
    "As if I was..."
    "{i}Rebooted...{/i}"
    "\[...\]"
    "That even {i}sounds{/i} dumb."
    "Along with my memories, my logic and my thought process start showing some signs of life as well, shortly after."
    "\[...\]"
    "It's late at night."
    "I woke up for no apparent reason."
    "And I feel like somebody just took my head, extracted my brain, did God-knows-what to it and then stuffed it back in."
    "\[...\]"
    "I try again to find some explanation to my sudden awakening."
    "But my still aching head clearly doesn't approve of that process..."
    "Maybe I shouldn't even bother?"

    mc "...and the exams should start in just a couple of days."

    "Oh, {i}there{/i} you are, common sense, haven't seen you in a while..."

    "Despite the fact that I really want to know the reason behind... all of this, I feel my urge to go back to sleep rising horribly fast."
    "And by seeing how my mind still refuses to cooperate with me..."

    mc "{i}yawn{/i}..."

    "Whatever it was..."
    "It can definitely wait until morning."
    "With all that said (even if not verbally), I lay back onto my pillow, falling back to sleep almost instantly..."

    scene black with dissolve_cg
    stop music
return

label prologue_day_1:
    $ renpy.pause(5.0)
    play sound "sfx/alarm.ogg"

    "\[...\]"
    "...!"

    play sound "sfx/alarm_slam.ogg"

    mc "..."
    mc "Ughh... I hate Mondays..."

    scene bg bedroom with dissolve_cg
    play music "bgm/some_generic_morning_track.ogg"

    "\[...\]"
    "I muffle those words into my pillow, before lifting my head slowly."
    "My eyelids protest as I try to open them, letting my eyes see the sunlight permeating into my room."
    "The grimace I'm making while doing so should be quite comical."
    "\[...\]"
    "I'm pretty sure I look like a cat right now, woken from its nap..."
    "Because I squint my eyes, yawn eagerly, and I can barely suppress an urge to start hissing spitefully at everyone and everything."

    mc "Uuugh...."

    play sound "sfx/thump.ogg"

    "I let my head hit the pillow, pressing it in as deep as possible..."

    mc "Need to..."
    play sound "sfx/thump.ogg"

    mc "...stop..."
    play sound "sfx/thump.ogg"

    mc "...staying..."
    play sound "sfx/thump.ogg"

    mc "...up..."
    play sound "sfx/thump.ogg"

    mc "...late!"
    play sound "sfx/thump.ogg"

    "I hit my head several times against the pillow as I say all this."
    "It helps me, eventually, to feel at least somewhat awake."
    "\[...\]"
    "...and with it, a weird thought comes through my mind."

    mc "Did I even stay up late yesterday?"

    "And if I didn't, then I should have at least had enough sleep, right?"
    "Unfortunately, my mind's library appears to still be closed, since I am unable to even recall the events of the last night."
    "It's either me having some weird amnesia, or just being extremely sleepy..."

    mc "{i}yawn{/i}..."

    "...must have been the latter after all."
    "Finally mustering my strength, I push myself off from the bed, letting my feet find the floor."
    "...to sit and stare at the window."
    "\[...\]"
    "For some reason I feel like I've been doing the exact same thing just recently..."

    mc "School..."

    "While my mind is clearly not in condition to make up any coherent thoughts..."
    "It seems that at least my self-preservation instincts are still functioning, capable of prioritizing my tasks..."

    # play a sound imitating MC standing up?

    "I finally let my body stand up, completely automatically, the real \"me\" still laying on the bed, trying to fall back to sleep."
    "I start with my morning chores..."
    "Getting dressed..."
    "Brushing my teeth..."
    "And while I'm, like, 50\% positive that if I were offered to exchange my soul for at least one extra hour of sleep, I would definitely say \"yes\"..."
    "...skipping classes now, with the exams on the horizon... clearly not the best idea."
    "And besides..."
    "For some reason... I feel like I..."
    "{i}Need{/i} to go there..."
    "\[...\]"
    "I really hope that I still have some instant breakfast left, because I'm already being a bit late..."

    scene white with dissolve_cg
    stop music fadeout 2.0
    $ renpy.pause(2.0)

    # 1)	remove all HUD elements
    window hide(None)
    # 2)	slowly change the background to a sky background, color scheme being similar to that of "residential.png" (the first background we see in the original game, when MC first meets Sayori)
    scene expression "bg/sky.jpg" with dissolve_cg
    # 3)	change soundtrack – DDLC Main Theme (we should also find a way too loop it, with the "Doki-Doki!" part happening just one time)
    play music t1
    scene expression "bg/splash-white.png" with dissolve_cg

    # 5)	text fades away & 6)	display text "Proudly presents"
    $ renpy.pause(2)
    scene bg splash2 with dissolve_cg
    # 7)	text fades away
    $ renpy.pause(0.75)
    scene black with dissolve_cg
    # 8)	the DDDC logo pops up (pay attention to the timing – just like in the main menu, it should pop-up as song goes "Doki-Doki!" XD)
    show logo at truecenter with dissolve_cg
    $ renpy.pause(5.0)
    # 9)	pause for about 5 seconds
    # 10)	 logo fades away
    # 11)	 the camera goes downwards
    # 12)	 Add some "blur" effect to that motion, as if we were just looking at the sky and then shifted our gaze downwards

    # 13)	 change the background to the actual "residential.png"
    scene bg residential_day with dissolve_scene_full
    # 14)	 HUD elements reappear
    window auto
    # [intro description ends here]
    # (NOTE – in case we skip the intro, then the soundtrack for that sequence should be just a regular looped version of "DDLC Main Theme" OST)

    "Despite the fact that I'm already walking down the street, I am fairly certain my consciousness fell asleep somewhere on the sofa back at home..."
    "And while I'm used to starting my school weeks in such condition, this time my tiredness seems to be amplified tenfold."

    mc "{i}yawn{/i}..."

    "Well, let's just hope that my inner GPS still works and I won't wander into some completely different part of the city."

    $ s_name = "???"
    s "Hey! [player]!"

    "Wha??"
    "Nooo-no-no-no..."
    "I am in neither condition nor mood for any morning chit-chats..."
    "So, whoever this is..."
    "Please... just ignore me..."
    "Imagine that I am some sort of glitch or something..."

    s "[player]!!"

    "The voice is getting closer. It's starting to sound more irritated..."
    "...and familiar?"

    mc "Oh no..."

    "As I rub my eyes, barely holding myself from letting out yet another yawn, I turn around to meet my annoying pursuer."

    # Decodes: "nope, we are not rehashing the original script"
    "I see an ann8ying girl rrunning toWard me f--rom the dIIStance, wavi— bm9wZSwgd2UgYXJlIG5vdCByZWhhc2hpbmcgdGhlIG9yaWdpbmFsIHNjcmlwdCA={nw}"
    "Yep, that's definitely her."
    "Your one and only..."

    $ s_name = "Sayori"
    s "Hey, what was that all about?!"
    s "Did you really try to just ignore me and walk away?"
    s "...pretending that you didn't hear me?"
    s "That is {i}super{/i} mean, [player]!"

    "Her accusing gaze and her hands on her hips don't go well with her otherwise cute appearance and extremely (sometimes – even ridiculously) cheerful personality."

    mc "I'm sorry, Sayori, I ju-{nw}"
    mc "{i}*yawn*...{/i}"

    "As I yawn, Sayori's expression quickly shifts from irritated to concerned."

    s "Whoa, did you even sleep last night?"

    "...and then it's back to accusations again."

    s "Don't tell me you'd stayed up late again just to watch some anime!"
    mc "Wow, look who's talking..."
    s "Eh?"

    "Sayori is almost taken aback by my sudden retaliation."

    mc "Sayori, this is the first time in, like, I don't even remember how long..."
    mc "But it's been a {i}while{/i} since we last met each other before school, and would you like to know why?"
    s "Eheheh... Well..."
    mc "Because whenever I pass by your house, you're still sleeping yourself!"
    mc "Seriously, I can almost hear you snoring; right here, from the street!"
    s "Awww! Okay! Okay!"
    s "You win..."

    "She pouts a little and lets her index fingers touch each-other's tips."
    "It's her typical gesture whenever she feels embarrassed or guilty."
    "...or gets busted."

    s "I just had a... problem with getting up recently..."
    s "And that still doesn't get you off the hook!"
    s "Seriously, you should always get enough sleep! You look like you've been run over by a steamroller!"

    "She suddenly comes closer and holds me by my wrist, looking into my eyes like a hurt puppy."

    s "Please, promise me you won't do it anymore, okay?"

    "I chuckle slightly as I pull back from her and put my hand on my heart."

    mc "Of course, my {i}darling{/i}, whatever you say."
    s "H-Hey!"
    s "D-Don't call me that..."

    "A small blush starts appearing on her face."

    s "You make it sound like we're... a couple or something..."

    "As I turn around and start walking away, I let out another chuckle."

    mc "Pff! Not in a million years..."
    s "Hey!!!"

    "She hits my back with a bottom of her fist."

    s "Now what was {i}that{/i} supposed to mean?!"
    mc "Heheh... Sorry, I guess I'm just a bit grumpy this morning..."

    "Sayori catches up, walking (or rather - skipping) right next to me."
    "We start off a typical, insignificant morning chat, which my mind doesn't even record, keeping up the conversation completely autonomously."
    "Sayori and I have been good friends since we were children. And to be quite honest, I can't even imagine befriending her right now."
    "I mean, while I'm just being your stereotypical, unremarkable high-schooler..."
    "...whose interests are limited mostly (if not exclusively) to only the greatest of humanity's achievements in terms of technological and cultural progress..."
    "In other words – video games and anime..."
    "Sayori, on the other hand is..."
    "Well..."
    "Let's just say that the first thing I would compare her to is the Energizer Bunny, with two huge light bulbs instead of eyes."
    "Even in the most boring and uneventful day, this little girl can remain cheerful, capable of finding joy in the smallest of things."
    "It's quite adorable, contagious even; not that I mind it..."
    "The point is, with us being almost complete opposites, it's funny that we've managed to even preserve our friendship through so many years..."
    "...let alone care for each other's well being."
    "I guess there {i}are{/i} some things in this world that you just accept the way the are, without looking for some explanation..."

    # fast forward screen
    scene bg school

    s "Helloooo!"

    "Huh?"
    "Sayori snaps her fingers in front of my face several times, trying to get my attention."

    mc "Huh? What is it?"
    s "Quit spacing out, will you?"
    mc "S-Sorry, guess I am still - {i}*yawn*{/i}"
    s "Oh, come on, you sleepyhead! We're almost at the school!"
    s "Cheer up!"

    "Sayori runs in front of me, twirling as she goes."

    s "There is a whole new, sunny day ahead of you! And you get to hang out with people, maybe meet some new friends..."

    "She slowly falls silent, watching a sour grimace appearing on my face."
    "There is no need for me to even say anything to show how skeptical I am."
    s "Jeez, you're getting less and less sociable every year!"
    s "Please don't tell me that you still spend all of your free time playing games!"
    s "How can you even live like this?"

    "Sure, go ahead, {i}wound{/i} my pride even more..."

    mc "Sayori, I appreciate your concern, but trust me, I'm fine the way I am."
    s "Come oooon, [player]! You really need to have something else to brighten up your everyday life!"
    s "You know, something to look forward to whenever you go to school!"

    "Look forward to going to school? Now that's a joke to remember..."
    "As I keep myself immersed in my thoughts, Sayori's face suddenly changes as if she's remembered something important."

    s "..."

    "Her eyes light up, as if she's come to some sort of realization."
    s "By the way, [player]!"

    "For some reason, I find that tone somewhat familiar... and suspicious..."

    s "Have you considered joining a club?"

    "Oh, no..."
    "Not this again..."

    mc "Sayori... we've been through this..."
    s "Exactly! I'm always trying to convince you to join some club..."
    s "and I keep doing so until you say something like, \"I'll think about it\" and then do nothing!"
    s "And then it keeps happening over and over again!"
    mc "Heh... sounds like a plan to me..."
    s "Oh, come oooon! Pleeeease?"

    "She once again comes closer, trying to give me the puppy eyes..."

    s "Pretty-pretty please??"

    "Nuh-uh. Not this time around."

    s "H-Huh?!"

    "I put my hand on her head, shielding her eyes, then use my other hand to delicately get her out of my way."
    "As I go pass her, I can barely hold myself from laughing at her stupefied expression."

    $ temp = player.upper()
    s "YOU'RE SUCH A MEANIE, [temp]!!"

    "I chuckle to myself and wave her goodbye, without even turning back."
    "I have to admit, I feel kinda bad for alienating her like that..."
    "especially considering that she is just trying to help, but I'm really not in the mood right now."

    mc "{i}sigh{/i}..."
    mc "Sorry, Sayori, but I'm better off this way..."

    "I adjust the straps of my backpack and finally enter the building."

    # fast forward screen
    scene bg class_day
    play music t2  # Ohayou Sayori!

    "I spend the most of the school day trying to finally shake off the remnants of my sleep."
    "Other than that, it's as ordinary as ever, and it's over before I even know it."
    "I wave goodbye to some of my classmates as they leave the classroom."
    "Meanwhile, I am still sitting at my desk, lazily packing up my things."
    "No matter what I do, Sayori's upset face still haunts me."

    mc "Ughhh..."
    mc "Maybe I should consider joining some club, after all..."

    "I mean, I understand that this is not obligatory..."
    "But the main purpose of those clubs (at least in theory) is to help people sharing the same interests to become more social..."
    "and get involved in something they all enjoy, devoting themselves to it."
    "And based on my interests, where would I even go? The Anime Club?"

    mc "Pfff... Yeah, sure..."

    "Despite the fact that it sounds like something right up my alley, I... don't think it's such a good idea after all..."

    $ s_name = "???"
    s "Huh? [player]?"

    "...?"

    "My solitude is suddenly interrupted by a familiar, cheerful girlish voice."

    mc "Sayori? What are you doing here?"

    $ s_name = "Sayori"
    s "It's funny, I was going to ask you the same thing..."
    mc "Huh? Why would y-{nw}"
    mc "Oh."

    "I finally realize that I'm the only person (apart from Sayori, that is) still sitting in the classroom."

    mc "Yeah, I just kinda spaced out for a moment..."
    mc "But you still haven't answered my question - why are {i}you{/i} here?"
    s  "Well, I was planning to catch you coming out of the classroom, but then I saw you just sitting here, and so I came in."
    s  "You know, I kept thinking about our conversation the whole day..."
    mc "Sayori, please..."
    mc "I promise I'll find some time to check out some clubs..."
    mc "Just... n-not now..."
    s "Oh, come oooon! That's the exact same excuse you {i}always{/i} give me!"

    "And it has been actually working so far..."

    s "Heeeeey..."
    s "I've just got a brilliant idea!"

    "I highly doubt it's even close to being brilliant..."
    "But I guess I have no choice but to hear it out, right?"

    mc "Well, spill it out, then."
    s "Ehehehe..."
    s "Well..."

    "She's clearly having a hard time telling me what's on her mind, which makes it all look even more suspicious."

    s "[player]..."

    "I raise my eyebrow questioningly."

    s "You wouldn't... want to make a cute girl upset, right??"

    "\[...\]"
    "No..."
    "NO! You can't be serious!"
    "You don't get to pull out {i}that{/i} trick on me!"

    mc "Seriously, Sayori?"
    mc "You're {i}seriously{/i} trying to get me into {i}your{/i} club just by guilt-tripping me?"

    "During our morning chat, I never actually recalled that Sayori is the vice president of the Literature Club."
    "To be honest, I can hardly see how Sayori and literature even mix..."
    "but I guess that every club just needs someone as passionate and proactive as her every now and then."
    "Besides, I'm pretty sure the main reason for her to be so enthusiastic about it was just an opportunity of helping to start a new club."

    s "I just thought that it could help you make up your mind..."
    s "And I've already told everyone that I will bring a new member with me..."

    "Huh?"

    s "Natsuki even brought her cupcakes, so the timing was perfect..."

    "Wait, WHAT?!"

    mc "Sayori, are you being serious right now?!"
    s "Ehehehe..."
    mc "So after having just {i}one{/i} conversation with me, and without even inviting me to join {i}your{/i} club in particular..."
    mc "you've already told your clubmates that I will definitely join?!"
    s "Eheh... um... please?"

    "I roll my eyes and facepalm."

    mc "No..."
    s "Pleeeease?"

    "Don't you dare..."

    mc "No, Sayori!"
    s "Pretty-pretty pleeeeeeeeeaaase???"

    "Don'tgivemethepuppyeyesdon'tgivemethepupp- ahh, she is giving me the puppy eyes..."
    "AGAIN!"
    "THIRD TIME IN A ROW!"
    "She is perfectly aware that it is quite a dirty trick to use, yet that doesn't prevent her from constantly using it."

    mc "Sayori, this is just unfair!"
    mc "Besides, you know I hardly have any interest in literature!"
    s "Oh, don't worry, it's much easier to get into than you think, trust me!"
    s "What {i}is{/i} important, however, is that you get to hang out with us!"
    s "We'll make you feel right at home!"
    mc "Ughhhh....."

    scene black
    with close_eyes

    "I cover my face with my hands for a few seconds, hoping that this annoying girl will simply vanish if I stop looking at her."
    "\[...\]"

    scene bg class_day
    with open_eyes

    "Nope, not happening..."
    mc "{i}Fine{/i}... I'll do it...."
    s "YAY!"

    "Sayori suddenly hugs me, almost making me fall from my chair."

    s "Thank you, thank you, thank you!"

    "I want to say that I'm only willing to give it a chance, yet I currently have no intention of actually joining her club..."
    "But I just don't have the guts to say that out loud."
    "I finally realize that it's been quite a while since I last got to hang out with Sayori."
    "For the past few months, we've almost never crossed paths."
    "Yet there once was a time when we used to walk to school together every morning."
    "Or just wander around, trying to kill time..."
    "Man, we even had sleepovers..."
    "At her place, mostly, since an airhead like herself would usually tend to keep her house in an almost complete mess, and she'd constantly rely on my help."
    "And that's where my caring personality comes in handy..."
    "Even if it {i}is{/i} buried deep below layers upon layers of cynicism."
    "\[...\]"
    "Well, guess there is no use in denying that I... missed her."
    "I let out a chuckle and finally hug her back."

    mc "Okay, okay..."
    mc "If that makes you happy, I'll give it a try..."

    "She lets go of me, and then takes my hand, eager to lead the way."

    s "Come on, then! You won't be disappointed, I promise!"
    s "You'll get along with everyone just fine! And you'll also like our room, and our president..."
    s "And- OH! Did I tell you about the cupcakes?!"
    mc "Err, yes, you mentioned them... Something about the perfect timing..."
    s "They are to {i}die{/i} for! Seriously! Natsuki is {i}super{/i} good at baking!"
    s "You're lucky that she decided to bring them today!"

    "As I stand up, Sayori grabs my backpack and hands it to me."

    s "Come on! I can't wait!"

    "Almost skipping with joy, she leads me out of the classroom."
    "Well, as long as I get a free snack, I guess it's not a complete waste of my time..."

    # fast forward screen
    scene bg corridor

    "As we leave the classroom, one of my classmates notices us."

    "Classmate" "Oh, hey, [player]! You're still here?"

    mc "Yeah, sort of. I'm just being taken to an eternal servitude in some club..."
    s "[player], stop it!"
    "Classmate" "Ahahah!! Really? And what cl-{nw}"
    "Classmate" "Wait a minute..."

    "He turns his head to Sayori, obviously remembering her from somewhere."

    "Classmate" "You're from the Literature Club, aren't you?"

    "Sayori face lights up even more."

    s "Yes! I'm the vice president, actually!"
    s "Would you like to join? We are always happy to see new faces!"
    "Classmate" "Nah, I... think I'll pass on that one, thanks."
    "Classmate" "Either way, I've gotta go! Rest in peace, [player]!"
    mc "Yeah, sure. When they ask for my epitaph, tell them to write something like... I don't know..."
    mc "\"Here lies [player], who sold his soul for a cupcake.\""
    s "[player]!"
    "Classmate" "Hah! Will do! See ya later, pal!"
    mc "Later."

    # fast forward screen
    stop music

    "I can barely keep up with Sayori, who is clearly far more enthusiastic about this whole situation."
    "I follow her across the school and upstairs - a section of the school I rarely visit, being generally used for third-year classes and activities."
    "Eventually, she leads me to a door of yet another completely unremarkable classroom."

    s "We're here!"

    "As she swings open the classroom door, I feel some fleeting and extremely weird feeling."
    "A feeling of..."
    "{i}Déjà vu...{/i}"
    "\[...\]"
    "Still oblivious to the reason of {i}why{/i} all of it feels so familiar, I follow Sayori into the clubroom."

    # fast forward screen
    scene bg club_day
    play music t1  # DDLC Main Theme (looping from 22.073s)

    s "Hey, everyone! I'd like you all to meet [player], our newest member!"
    mc "Sayori, I'm only-{nw}"

    "Huh?"
    "I take a glance around the room."

    $ y_name = "Girl 1"
    y "Oh... I-It's a pleasure meeting you."

    "The first member I see is a tall girl with long purple hair, sitting at a desk near the window."
    "She appears to have been reading a book, and by looking at her behaviour, I can clearly see that she's not entirely comfortable with me being here."

    $ n_name = "Girl 2"
    n "{i}*Pant* *Pant*{/i}"
    n "Seriously, Sayori? When you said you were going to bring a new member, I didn't expect you to bring your boyfriend!"

    "That other voice comes from a closet in the far corner of the room."
    "Soon, I see its source emerging from the said closet."
    "She has short pink hair, and her equally short and small figure makes me think she's probably a first year."

    s "H-Hey! I never said he was my boyfriend!"
    n "Oh, so it's just some random boy, then? Way to ruin the atmosphere, Sayori!"

    "The atmosphere...?"
    "\[...\]"
    "Wait..."
    "Does that imply that the members of this club..."
    "Are {i}all{/i} girls?"

    $ m_name = "???"
    m "[player]?"
    mc "...?"

    "Okay, now {i}that's{/i} a voice I clearly did not expect to hear."
    "But as I turn around to the teacher's desk, my assumptions are indeed confirmed."

    $ m_name = "Monika"
    m "Oh my gosh, I did not expect it to be you!"
    m "What a nice surprise!"

    "Yep, that's definitely her..."
    "Monika, probably one of the most popular girls in the entire school."

    mc "H-Hi there, Monika. I can say that I'm quite surprised as well."
    s "Whoa, you two know each other?"
    mc "Yeah, we... kinda were in the same class some time ago."
    mc "We didn't get to talk much, though..."
    m "Yeah... that's true..."

    "Monika looks away, almost apologetically."
    "To be honest, it feels a bit awkward to talk to her even now."
    "We almost never talked, despite being in the same class."
    "I'm not so sure whether she's an exchange student or maybe some of her parents have foreign backgrounds..."
    "What I {i}do{/i} remember, however, is that since the day she first appeared here, she started climbing the popularity ranks rapidly, gaining favor amongst both teachers and other students."
    "Her confidence, charisma and trademark smile quickly earning her certain recognition."
    "Add her intelligence, good looks, and athletic ability into the mix, and you'll get the full picture."
    "\[...\]"
    "...a picture of a girl, who is completely out of my league; hence our scarce communication."

    m "But I guess that's about to change, now that you're here!"

    "Monika gives me the sweetest smile I've ever seen, making me feel even more uncomfortable."

    s "Well, I see there's no need to introduce you to our president, then."
    s "Buuuuut..."

    "Sayori grabs my arm and turns me around to face the two girls I did not recognize."
    "...who are already standing right in front of me."
    "...I can also hear Monika behind me, standing up from the teacher desk."

    mc "{i}*Gulp*{/i}"

    "I'm standing in the middle of the classroom, about to be surrounded by four..."
    "{i}Incredibly...{/i}"
    "{i}Cute...{/i}"
    "{i}Girls!{/i}"

    s "[player], I would like you to also meet our dear Natsuki, always full of energy!"

    $ n_name = "Natsuki"
    n "Hmph!"

    "Ah, so {i}that's{/i} Natsuki, the one who supposedly brought some cupcakes today, according to Sayori..."
    "She looks quite short, almost half as tall as me, in fact."
    "And I'm pretty sure she's the youngest here as well, though I might be mistaken."
    "Looks can be deceiving, after all..."

    s "Just ignore her when she gets all moody..."

    "Sayori whispers those words into my ear."
    "I may have known Natsuki for only a minute or two, but her sour attitude is something you can't help but notice."
    "Though her looks don't quite go well with it..."
    "I have to admit, it's hard for me to keep myself from smiling when I look at her pouting like this."

    s "And, of course, Yuri, the smartest in our club!"

    $ y_name = "Yuri"
    y "D-Don't say things like that..."

    "Yuri, on the other hand, seems to be the complete opposite to Natsuki (and Sayori, for that matter)..."
    "She appears to be quite shy and far more mature, compared to the others."
    "And to be honest, she is by far the only one who I could easily imagine being a member of the Literature Club."
    "Even after taking just a small glance at her, I can tell that she's a real bookworm."
    "And I don't think you need a grade in psychology to figure that out."
    "As for her looks... well..."
    "Let's just say that when I use the word \"mature\" while describing her, I mean it on {i}many{/i} levels..."  # (gentlemen, would somebody, please, be so kind as to pass me my monocle? XD) -- Shadow

    mc "A pleasure."

    "It would be a shameless lie, if I said it wasn't..."

    y "So, [player]..."

    "Yuri seems to have calmed down, a shy smile appearing on her face."

    y "What made you consider joining the Literature Club?"

    "Oops..."
    "While I appreciate you taking a more straightforward approach, you've clearly managed to step on a landmine, right off the bat..."

    mc "Y-Yeah... About that..."
    mc "I d-don't mean to be a killjoy, but I kinda..."

    "I glance at Sayori, who is getting more upset with every second."

    s "[player]..."
    mc "I just kind of stopped by... Nothing more..."
    mc "Sayori really wanted me to try joining some club, but I... never made any actual decision..."
    y "O-Oh... Um... I see..."
    n "Heh... Told you about killing the atmosphere..."
    mc "...plus I was in the mood for some cupcakes..."

    "I say that under my breath. Luckily, none of them seems to have heard it."
    "I lower my eyes, feeling as if I had just confessed to some heinous crime."
    "\[...\]"
    "Wait a minute, why should I even feel guilty? I've literally been dragged here by Sayori!"
    "It was never my intention to join any club in the first place!"
    "But just by looking at upset faces of these girls..."
    "\[...\]"
    "This is not good."
    "I really can't make any clear-headed decisions in a situation like this..."

    m "Well, anyway, let's not get distracted!"
    m "We have a guest after all, so the least we can do is to make him feel at home, right everyone?"

    "Monika is obviously trying to lighten up the mood."
    "Not surprising - she is the president, after all. She should be used to dealing with situations like these."

    s "Oh! Yeah! I almost forgot!"
    s "[player], I promised you some cupcakes, right?"
    n "E-Eh?!"
    n "Hey, I didn't make them just for some random-{nw}"
    y "Natsuki..."
    y "You're really not helping us make a good first impression."
    n "...!"
    n "Sigh..."
    n "Yeah, yeah, I know..."
    n "I'll go grab them, then..."
    y "And I'll make some tea, if everyone's okay with that."
    m "That'd be great! Meanwhile, we'll organize the desks."

    "Em, define \"we\"..."

    s "Yeah! Come on, [player], we can arrange the desk to form a table, so that everyone can take a seat!"

    "Before I'm even able to say anything, I feel a pair of hands grabbing my shoulders from behind."

    m "We could really use some help with that."

    "With that said, Monika starts pushing me forward."
    "As we go, I feel her leaning slightly closer to my ear, her voice almost turning into a whisper."

    m "A gentleman like yourself wouldn't possibly want to make four beautiful girls any {i}more{/i} upset, right?"

    "Out of the corner of my eye, I see Monika's expression becoming more flirtatious, her emerald eyes almost drilling into me."
    "With every minute I spend here, I slowly lose my ability to think clearly..."

    # fast forward screen

    "Shortly after, we form a table with enough space for all of us."
    "I see Yuri coming back, carrying a tray with a kettle and several cups."

    mc "Do you keep a whole tea set here?"
    y "Mhm."

    "Yuri smiles sweetly."

    y "It took some time to convince the teachers, but they allowed us to keep it in the clubroom."
    s "Yeah! Thankfully we have Monika as our president, so we basically have all the teaching staff on our side, no matter what!"
    y "I agree, we couldn't have asked for a better president."
    m "Ahahah..."
    m "Please, girls, you're embarrassing me..."

    "Monika getting embarrassed? Now that's something you don't see that every day..."
    "As Yuri sets everything on the table, I take a seat between Monika and Sayori."
    "I instinctively move my chair a bit closer to Sayori, though, since she is the one I feel most comfortable around."
    "As I raise my eyes, I see Natsuki, proudly marching back to the table with a tray covered in tin foil in her hands."

    n "Okaaay, everybody ready?"
    n "...Ta-daa!"

    "Natsuki lifts the foil off the tray to reveal a dozen white, fluffy cupcakes decorated to look like little cats."
    "Their whiskers are drawn with icing, and little pieces of chocolate were used to make the ears."

    s "Uwooooah!"
    s "They're soooo cuuuuute!"

    "For some reason I feel like I've {i}seen{/i} them somewhere before..."
    "\[...\]"
    "In a recipe or an advertisement somewhere online, most likely..."

    m "Wow, I knew you were good at baking, Natsuki, but I never expected something of this scale!"
    n "Ehehe. Well, the more you know..."
    n "Don't just sit there. Grab one already!"

    "You don't have to tell Sayori twice..."
    "She grabs one and takes a huge bite."

    s "Shhooo goooood!"

    "Without even chewing it all down, she starts talking, her voice muffled, and some icing already smudged over her nose."
    "Monika takes one cupcake for herself, and Yuri follows her example."
    "I finally take one as well and start turning it around in my fingers, looking for the best angle to take a bite."

    n "..."

    "Natsuki is the only one who still hasn't touched the cupcakes, and I can see her sneaking glances in my direction."
    "Is she waiting for me to try it?"
    "After finally finding an angle I'm satisfied with, I take a bite."
    "\[...\]"
    "The icing is sweet and full of flavor."
    "Whether she made them herself or had some help, it's still really impressive!"

    mc "This is really delicious."
    mc "Thank you, Natsuki."
    n "W-Why are you thanking me? It's not like I..."
    n "...made them just for you or anything!"

    "I swear I've heard that somewhere before..."
    "I decide to ignore her and just enjoy my meal."
    "Meanwhile, Yuri has finished pouring tea into all the cups and begins carefully placing them in front of everyone."

    y "So, [player], what do you usually like to read?"
    mc "..."

    "I hoped that we could avoid topics like that, since I've just recently said that I am not joining their club."
    "But I guess I can't blame them for hoping for me to change my decision."

    mc "Well... um..."

    "Besides, considering how little I've read these past few years, I don't really have a good way of answering that."

    mc "Manga..."

    "I mutter it quietly to myself, half-joking."
    "Natsuki's head suddenly perks up."
    "My words clearly peaked her interest, but she keeps quiet."

    y "N-Not much of a reader, I guess..."

    "Yuri, on the other hand, obviously had some higher expectations."

    n "H-Hey! Don't say that like that's a bad thing or something!"
    y "Oh?"
    y "Ah, uhm, s-sorry... I didn't mean it that way..."

    "Monika leans to me, half-whispering."

    m "Natsuki keeps her entire manga collection in the clubroom..."
    n "...!"

    "Sayori lets out a giggle, snorting in her teacup."

    s "Yeah, she's always saying that it's literature as well!"
    n "Gnnnn!!"

    "Now you did it, Sayori..."

    n "Manga {i}IS{/i} literature!"

    "We all laugh, unable to keep it together while looking at Natsuki's quickly reddening face."

    # fast forward screen
    play music t8  # Daujoubu!

    "With the atmosphere finally getting less tense, we spend the next few minutes just chatting and drinking tea."
    "Natsuki's cupcakes fade away with alarming speed."

    m "So, [player], I take it that you're enjoying your stay here so far?"

    "I reach out to grab the last cupcake from the tray."

    mc "Well, I'd be lying if I said I wasn't."

    "I mean, what sane guy would say no to that question?"
    "And besides, those sweet smiles that answer earns from Monika, Yuri, Sayori and even Natsuki are definitely worth it."

    mc "By the way, Monika, I wanted to ask you..."
    mc "How come you decided to start your own club?"
    mc "You could easily be a board member for any of the major clubs."
    mc "Actually, weren't you a leader of the debate club last year?"

    "Monika smiles and takes a sip of tea."

    m "I knew you would bring it up sooner or later..."
    m "You see, to be honest, I can't stand all of the politics around the major clubs."
    m "It feels like nothing but arguing about the budget and publicity and how to prepare for events..."
    m "I'd much rather take something I personally enjoy and make something special out of it."
    m "And if it encourages others to get into literature, then I'm fulfilling that dream!"
    y "That is indeed an admirable cause."
    s "And that's why we're here to help you with it!"

    "The girls are clearly fond of Monika. Nothing surprising about that, to be honest."
    "Whatever it is she decides to undertake, she always succeeds in it."
    "What's not to admire about that?"

    mc "I'm actually surprised there aren't more people in the club yet..."
    "Monika's expression changes; a smirk appears on her face and her eyebrow raises teasingly."
    "\[...\]"
    "Damn it."
    "I shouldn't have said that..."
    "Now I've cornered myself..."
    "Meanwhile, Monika continues, pretending that she hasn't noticed that little slip up I just made."

    m "Well, you see, not many people are very interested in putting out all the effort to start something brand new..."
    m "Especially when it comes to something that doesn't grab your attention, like literature."
    m "You have to work hard to convince people that you're both fun and worthwhile."
    m "But it makes school events, like the festival, that much more important."
    m "So I'm confident that we can all really grow this club before we graduate!"
    m "Right, everyone?"
    s "Yeah!"
    y "We'll do our best."
    n "You know it!"

    "Such different girls, all interested in the same goal..."
    "Monika must have worked really hard just to find these three."
    "Maybe that's why they were all so delighted by the idea of a new member joining."
    "Though I still don't know if I can keep up with their level of enthusiasm about literature..."
    "However..."
    "What really bugs me is that while I know only one of these girls well enough..."
    "I mean, Monika and I have barely spoken to each other, and I've only met Yuri and Natsuki today..."
    "...I can't help but feel like I've {i}known{/i} them for a while..."
    "\[...\]"
    "I should probably quit spacing out and try to keep up the conversation, otherwise they'll think I'm getting bored."

    mc "So, Yuri, and what do you like to read?"
    y "H-Huh?!"
    y "Um, me??"

    "Man, could you have possibly picked someone even {i}more{/i} difficult to talk to?"
    "While she is trying her best to act natural, she's obviously still not used to having me around."

    y "W-Well, I suppose there's no simple answer to that question..."
    y "But I guess the best way to describe my preferences is something that is truly... {i}immersive{/i}."

    "I watch as she calms down, the remnants of a shy, introverted girl fading away, clearing the way for a wise and mature... {i}woman{/i}, whose eyes light up when she finds her comfort zone."

    y "I really love it when the book acts like a guide, taking you on a journey, making you feel like you're actually entering that beautifully described world, so different from our own..."
    y "...helping you to get involved into the story, relate to its characters..."

    "I find myself admiring Yuri's little speech, and I really hope that I don't look too stupid while I'm gawking."
    "I have to admit - I've never met someone so passionate about literature in my life."
    "As she goes on, I look back into my memory, trying my best to find at least something I can relate to."

    mc "I'm impressed, Yuri! You truly make it sound so fascinating!"

    "Yuri stops in her tracks, blushing a little."

    y "I'm... glad you feel that way..."
    mc "To be honest, the only thing I can remember that got me so immersed was a horror novel I had read... a really long time ago."
    y "Oh? Really?"

    "Surprisingly enough, my words seem to peak Yuri's interest."

    y "I've actually been reading a lot of different horror stories as well..."

    "Okay... that was unexpected..."

    y "N-Not that I am f-fond of horror!  It's just that..."
    y "You see, stories with deep psychological elements is something I particularly enjoy."
    y "They make you feel all those emotions that characters have to experience; their shock, their anxiety..."
    y "...and quite often, they can even make you ponder about your own ideology, changing the way you look at the world."
    m "Honestly I would never have expected that from you, Yuri."
    m "For someone as gentle as you..."
    m "To take interest in something so... unique."

    "To be honest, when it comes to Yuri, I'm pretty sure everything that can be described as \"unique\" is applicable."

    y "Well, I guess we all have our own little demons inside us..."
    n "Ugh, I hate horror..."
    y "Oh? Why's that?"
    n "Well, I just..."

    "Natsuki's eyes dart over to me for a split second."

    n "Never mind."
    m "That's right, you usually like to write about cute things, don't you, Natsuki?"
    n "W-What?!"
    n  "What gives you that idea?"
    m "You left a piece of scrap paper behind last club meeting."
    n "Gnnnn!!"
    m "It looked like you were working on a poem called-{nw}"
    n "Don't say it out loud!!"
    n "And give that back!"
    m "Fine, fine~"
    s "Ehehe, your cupcakes, your poems..."
    s "Everything you do is just as cute as you are~"

    "Sayori sidles up behind Natsuki and puts her hands on her shoulders, almost hugging her."

    n "{i}I'm not cute!!{/i}"

    "Are you sure about that?"

    mc "Natsuki, you write your own poems?"
    n "Eh? Well, yeah... sometimes."
    n "Why do you care?"
    mc "Wow, I think that's really impressive."
    mc "Why don't you share them sometime?"
    n "N-No!"

    "Natsuki averts her eyes."

    n "You wouldn't...like them..."
    mc "Ah...not a very confident writer yet?"
    y "I can understand how Natsuki feels."
    y "Sharing that level of writing takes more than just confidence."
    y "The truest form of writing is writing to oneself."
    y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."
    m "I take it that you have some writing experience too, Yuri?"
    m "Maybe if you share some of your work, you can set an example and help Natsuki feel comfortable enough to share hers."
    y "U-Ummm..."
    mc "I guess it's the same for Yuri..."
    s "Aww... But I wanted to read everyone's poems..."

    "We all sit in silence for a moment, until it's broken by Monika clapping her hands."
    m "Okay!"
    m "I have an idea, everyone~"

    "All of us look at her quizzically."
    m "Let's all go home and write a poem of our own!"
    m "Then, next time we meet, we'll all share them with each other."
    m "That way, everyone is even!"

    "The reaction follows shortly after."

    n "What?!"
    y "U-Um..."
    s "Yay! Let's do it!"
    m "Besides, since we now have a new member, I think it will help us all get a little more comfortable with each other, and strengthen the bond of our club."

    "...?!"

    mc "{i}*Cough*{/i}"
    mc "Uhm, Monika?"

    "Monika rolls her eyes and lets out a sigh, turning to me with her arms folded on her chest."
    "There's no malevolence on her face, but she looks clearly annoyed by my stubbornness."

    m "[player]."

    "Well, here it goes..."

    m "I know it's all a bit overwhelming, and you never intended to do this..."
    m "...and that Sayori bit off more than she could chew, telling us that you would definitely join..."
    s "Eheheh~"
    m "But I would like to be straightforward with you and ask you this one question..."

    "She takes a short pause, inhaling before saying the words I knew she would say sooner or later..."

    m "Would you like to join the Literature Club?"
    mc "..."

    "I can't remember the last time I'd been so conflicted."
    "On one hand, it's just like Monika said – I never intended to come here in the first place..."
    "But on the other hand..."
    "I take a look at those four beautiful girls, surrounding me..."
    "They all stare at me, their eyes full of hope, the corners of their mouth slowly moving downwards with each passing second..."
    "Sayori, the good childhood friend of mine, a little lump of sunshine in this grey, boring world..."
    "Natsuki, a cute, fragile girl, hidden beneath that harsh exterior..."
    "Yuri, a maiden of mystery, covering her true-self behind that timid façade..."
    "And Monika, a girl who'd always impressed me, who is now giving me the most genuine smile, hoping to hear \"yes\" for an answer..."
    "\[...\]"
    "What was that about making clear-headed decisions?"
    "Ah, who cares, being logical is overrated..."

    mc "Okay."

    "One by one, the girls' eyes light up."

    mc "I cannot lie – I really enjoyed spending time with you all, and therefore..."
    mc "...while I still can't believe I'm saying this, I've made a decision."

    "Sayori is almost ready to explode at this point."

    mc "I will join the Literature Club!"

    "With that said, I brace myself for impact."

    s "Yaaaaaaay! I'm so happyyyy~"

    "Sayori wraps her arms around me, jumping up and down."

    mc "H-Hey, easy there..."
    y "I was honestly worried that you would just... leave at the end..."
    n "Yeah! If you really came here just for the cupcakes, I would be super pissed!"
    m "I'm so glad that you've finally made up your mind."
    m "And... I guess that makes it official!"
    m "[player]."

    "Monika reaches out her hand for a handshake."

    m "Welcome to the Literature Club!"

    "I smile and delicately shake her hand."
    "I still can't get rid of that feeling that everyone and everything here seems so familiar."
    "Maybe it's just a hint to me that this is where I {i}belong{/i}."
    "Honestly, it doesn't matter."
    "I've made up my mind."
    "And I'm ready for whatever the future has in store for me."

    m "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    m "Everyone remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"

    "Monika looks over at me once more."

    m "That's especially important in your case, [player]! I'm really looking forward to see how you express yourself."

    "I chuckle as I jokingly salute her."

    mc "Yes, ma'am."

    "Monika smiles sweetly and goes to the teacher's desk."
    "Soon, the girls have cleaned up all the tableware and packed up their things, ready to leave."

    s "Hey, [player], since we're already here, do you want to walk home together?"
    mc "Sure, why not? It's been a while since we last did it, after all."
    s "Yeah, it really has..."

    # fast forward screen
    scene bg residential_day

    "That day was clearly a complete surprise for me."
    "A very good one, to be completely honest."
    "I'm still unsure whether it was all just some weird dream."
    "But it doesn't matter."
    "Right now, I'm happy how things have turned out."
    "And I'm ready for whatever I'll have to face."
    "Because this time..."
    "{i}I'll set things right{/i}"
    "\[...\]"
    "What am I even on about?"

    s "Helloooooo?"
    mc "Huh?"
    s "Come on, don't tell me you're spacing out again!"
    s "[player], promise me that you'll get enough sleep tonight, okay?"
    mc "I will."
    mc "Seriously, Sayori, you worry about me too much."

    "Sayori smiles."

    s "Well, who else would worry about you, if not your best friend?"

    "I smile back, unable to find any good way to answer that question."
    "It's only a matter of minutes before we reach Sayori's house."

    s "Ahhh... I'm so glad you joined us, [player]!"
    s "I still can't wrap my mind around it, I'm just so happy!"
    mc "Yeah, I'm still analyzing it myself, to be honest..."
    s "Don't worry! I promise you won't regret it!"
    s "Now, go home and get some sleep! I'd like to walk to school with you again tomorrow morning!"
    s "And I don't want you to be all sleepy and grumpy again..."
    mc "Hahah~ Noted."
    s "Oh! But before you go to sleep - don't forget to write your poem today!"
    s "It's really important, and we'll all be upset if you just forgot about it..."

    "She pouts falsely, looking me straight in the eyes."

    s "You wouldn't want to make us upset, right?"
    mc "Don't worry, I'll do my best, I promise."
    s "Great!"

    "She almost jumps with joy."

    s "Well, I'll see you tomorrow, then!"
    s "Have a good night!"
    mc "Night."

    "As I walk away, I see Sayori skipping to her house."
    "\[...\]"
    "Yes."
    "It was indeed a good day."

    scene black with dissolve_cg
    stop music fadeout 4.0

    $ style.say_dialogue = style.edited
    "???" "Oh my, this is about to get interesting!"
    $ style.say_dialogue = style.normal
return

label prologue_day_2:
    # fast forward screen
    scene bg club_day
    play music t2  # Ohayou Sayori!

    "It's an ordinary day in our club."
    "I can't say that I'm an expert on calling things \"ordinary\" around here, since I've been here for just a couple of days."
    "But I got fairly used to the most of our usual routine."

    m "So, [player], how's school going for you?"

    "I'm standing in front of the teacher's desk with Monika on its opposite side, writing something. She barely even looks at me."

    mc "I'm managing... more or less. It can be a bit stressful with exams on the horizon."
    m "Yeah, I can understand that, believe me."
    mc "And what about you? How are you doing?"
    m "Fine, actually."
    mc "You sure? I mean, I'd imagine it'd be pretty tough to keep up with your studies while also being president of a club."

    "Monika looks at me with her eyebrow raised."

    m "You seem awfully... {i}concerned{/i} for me, [player]..."

    "She flashes me a teasing smirk that's just as trademark as her smile."

    m "Is there something I should know?"
    mc "...!"
    mc "I-I was just... trying to keep up the conversation, that's all!"
    m "Ahahaha!"
    m "Sorry, [player], I'm just-{nw}"
    n "There you are, [player]!"

    $ mc_m = player + " and Monika"
    "[mc_m]" "Huh?"

    "Natsuki unceremoniously interrupts our little chat."

    n "Finally! I've been waiting for you, you know!"
    mc "Oh, hey there, Natsuki! Sorry, I'm kinda late today, I arrived a couple of minutes ago."
    m "Yeah, he was just keeping me company."

    "Coming from Monika, even something as seemingly harmless as this sounds like it has some hidden meaning to it..."
    "\[...\]"
    "{i}That{/i} or it's just me watching way too much anime..."

    m "Either way, why were you waiting for him, Natsuki? Do you need help with something?"
    n "Well, I needed him to help me carry some books to my classroom."
    n "But in case you two are {i}that{/i} busy, then I'll just do it myself!"

    "With that said, Natsuki turns away from us, preparing to walk away."

    m "Wait!"
    m "[player], I think it's better if you'd go and help her. After all, she's quite frail."
    n "W-What?!"
    n "I'm not frail! I'm just... small..."
    n "({i}Why did I say that...?{/i})"
    n "Anyway, are you gonna help me out or not?"
    mc "Yeah, yeah I'll help you out.. Though not for free..."
    n "Huh?!"
    mc "You did bring something with you today, right? If I recall correctly, you were planning to share some homemade cookies."
    n "What?! Are you really trying to charge me just for your help?!"
    mc "Heheh... I'm just joking, Natsuki. Don't take it seriously."
    mc "Come on, I'll help you out, no strings attached."
    n "Hmph!"

    # fast forward screen
    scene bg corridor

    "After helping Natsuki out, we go back to the clubroom for our club activities."
    n "Just so you know, I didn't ask for your help just to spend more time with you or anything."
    n "I just needed a hand to help carry the books, that's all!"
    mc "I know, I know... Just happy to help."

    # fast forward screen
    scene bg club_day

    "The first thing I hear when we enter the clubroom is Sayori's upset voice."

    s "Monikaaaa!"

    "It seems to be coming from the closet..."

    m "What is it, Sayori?"
    s "I've looked {i}everywhere{/i}, but I just can't find any colored paper!"
    m "Yeah... That's a pity..."
    m "I'll add it to the list, then. We'll get it along with all other supplies for the festival..."
    s "Huh... Okay..."

    "Sayori literally crawls out of the closet, dusting off her skirt as she stands up."
    "As she notices me, her face shines with joy."

    s "Oh, hey there, [player]!"
    mc "Umm, hi? We've kinda... already seen each other today..."
    s "Tehehe~"
    s "Yeah, I'm still getting used to it."
    s "It's just so unusual to meet you every morning, let alone see you every day in the club."
    mc "Heh... that's true..."

    s "Oh! By the way, Monika..."
    "Sayori and Monika walk towards the other end of the clubroom while discussing plans for the festival. Natsuki follows soon after."
    "Meanwhile I, having nothing better to do, grab the water pitcher and start watering the flowers."

    y "Oh, hello [player]!"
    mc "Hmm?"

    "I barely even noticed Yuri entering the clubroom."

    mc "Hey there Yuri, are you feeling better? We were worried since you called in sick yesterday."
    y "I am feeling much better already, thank you."

    "She smiles sweetly as to assure me that she's totally fine, but something about all this seems a bit off."

    mc "You sure you're okay with being at school? I mean, it's only been one day and you're back already..."
    mc "What made you stay at home, by the way? Cold? Fever?"
    y "Eheheh... I-It's okay, [player], please don't worry about it, I am fine..."
    mc "Hmm... if you say so..."

    "I still don't buy it, but knowing Yuri's gentle and private personality, pushing her any further won't lead to anything good."

    y "A-Anyway, how are you doing with your studies? I would be happy to give some assistance in case you need help."
    mc "Ahaha- Nah, I'm... I'm good, Yuri. But thank you for your consideration."

    "That's a blatant lie to be honest, but I'd hate to cause her any trouble."
    "Though it might also be my pride talking..."
    "\[...\]"
    "As I turn my head back to the teacher's desk, I see Monika, Sayori, and Natsuki chatting while occasionally glancing at me."

    n "They seem so close, right? I'm starting to think that Yuri has feelings for him..."
    m "Natsuki, don't gossip about them. They might be able to hear you, you know. Besides, it's just rude."
    mc "So, what are you guys talking about?"
    s "Oh, we're just talking about you, [player]."
    mc "Really? Never considered myself as an interesting topic for discussion."
    n "Yeah, well, you know... With you and Yuri being so close together all of a sudden."
    mc "What? We aren't even that close! We're just friends, that's all."
    mc "If I didn't know you any better, I'd assume you're just being jealous!"
    n "W-WHAT?!"
    m "Natsuki, mind your volume."
    y "Umm... are you talking about me, by any chance?"
    n "Well yeah, we are."
    mc "Not really, Yuri. Don't mind Natsuki, we're just... ehm..."
    m "We're discussing the poems we're going to write to showcase for the school festival."
    mc "Y-Yeah, what she said."

    "Writing poems became a part of our everyday routine, as well as our homework."
    "It was pretty difficult for everyone at first (especially me, since literature and I don't mix well)."
    "But we've all been making some slow, yet steady progress."

    m "Does anyone have a topic in mind?"
    s "Oh, I know! How about writing a poem about the future?"
    mc "Err... that's kinda vague..."
    s "You think so? Aww..."
    n "What about writing a poem about animals, then? I mean, every animal has its own perks. It should be interesting!"
    y "Natsuki's idea seems fine, but I'd suggest writing about our surroundings, like nature."
    n "What? \"Seems fine\"? It's way better than your idea!"
    n "Writing about surroundings and nature? That'll put people to sleep at the festival!"
    y "Excuse me, but nature is beautiful in so many ways. The peacefulness of an untouched forest, or the vibrant colors of the Northern Lights..."
    y "It's a perfect topic for a poem."
    y "Writing about hidden beauty and tranquility is what poetry is all about."
    y "On the other hand, I find it hard to turn a subject such as animals into a poem..."
    n "What?! A poem about animals is easy! You could write about something like the life of a cat in plenty of ways!"
    n "Like how they behave and what they do that's cute!"
    m "Come on, guys, there's no need to argue over something that trivial."
    n "I didn't start it! Yuri did!"
    y "Excuse me? I wasn't arguing, I was just stating facts."
    n "Facts? Those aren't {i}facts{/i}! Those are just words made to start an argument!"
    y "Sigh..."
    n "Hmph!"

    "As their argument slowly falls silent, Natsuki suddenly turns to me."

    n "It's your fault we started arguing, [player]!"
    mc "Huh? What?! What did {i}I{/i} do?!"
    "The others start to laugh, and soon both Natsuki and I join them."

    ##

    # fast-forward screen
    "The atmosphere in the clubroom became much less tense after Natsuki's joke."

    m "Okay, everyone! How about we all support our point of views with some actual arguments?"
    m "Everyone brought their poems today, right?"
    m "Let's skip straight to sharing them and {i}then{/i} we can get back to exchanging our ideas about the festival..."
    s "Works for me!"
    y "Y-yeah, of course."
    n "Ugh, fine."

    "All of the girls stand up and go to where they left their poems."
    "I shrug."
    "Guess there's nothing better to do..."
    "I decide to start with Monika, just because I'm standing right next to her."

    m "So, [player], are you ready to read my poem?"
    mc "Sure, I mean... That's what we usually do, right?"
    m "Huh? And that's it? And you are not even looking forward to it?"
    m "Awww... and here I thought..."

    "Monika pouts falsely, almost mimicking Sayori with her puppy eyes."
    "...and I guess that cliche still works... {i}goddammit{/i}..."

    mc "H-Hey! I didn't mean it {i}that{/i} way, how did you even came up with that idea?!"
    m "Ahahah! I'm sorry, [player], you're just so easy to tease!"
    mc "{i}sigh{/i}"
    mc "Whatever..."

    "Monika finally hands me her poem, written in her notebook with her accurate handwriting."

    call showpoem(poem_m)

    mc "..."

    "I look at Monika. She is obviously eager to hear some feedback."

    m "So... what do you think?"
    mc "I like it. I just..."
    mc "I'm... kinda having trouble figuring out what it's about."
    m "Really? Hmm... that definitely wasn't my intention."
    mc "It really is amazing though. We should definitely showcase it in the school festival!"

    "Am I just seeing things, or is Monika, of all people, actually blushing right now?"

    m "I'm glad you like it, [player].This is actually one of my bes-{nw}"
    s "Hey! Hey, [player]! Do you want to read my poem?"
    mc "Sayori, please, watch your manners."
    mc  "You just interrupted Monika."
    s "Ehehe... S-Sorry Monika, I'm just too excited."
    m "Ahaha, don't worry about it, Sayori. It's okay."
    mc "So, Monika. You were saying?"
    m "Yeah... I consider this one to be one of my best poems."
    mc "I can definitely tell you put a lot of effort into it."
    m "Well, honestly it wasn't all that difficult. I just got some inspiration, and... here we are!"
    s "Okay, okay, now check out my poem!"
    s "Pleeeease!"

    "I sigh as I look at Monika, waiting for her approval."

    m "It's okay, [player], go ahead. We should actually finish with this as soon as we can since we don't have that much time."
    mc "Okay..."
    s "Yay, finally, my turn!"

    "You're literally the second one..."
    "I take the sheet of paper on which Sayori wrote her poem."

    call showpoem(poem_s)

    mc "Wow, Sayori, you actually wrote this?"
    s "Yeah! How was it?"
    mc "Well, it kinda gave me almost the same feelings that Monika's poem did."
    s "Oh? And how did it make you feel?"
    mc "If I had to put it into words, I'd say it is peaceful and serene."
    s "Really?!"
    s "Haha, I outdid myself!"
    s "My poem was on par with Monika's!"
    mc "Don't get over your head - yours wasn't even close to Monika's standard."
    s "Whaa???"
    s "But I even wrote more words than Monika!"
    s "I wrote 68 words and Monika only wrote 66!"

    "{i}When did you even manage to count them?!{/i}"

    mc "Emmm... That's not the point here..."
    s "I even used awesome words..."
    mc "Again, not the point..."
    m "You see, Sayori, it's not about the length of the poem, but rather the quality..."
    s  "Heh... Look, Monika is bragging about her poem.."
    m "Eh?! I wasn't bragging, I was just stating facts!"
    s "Haha! I was just joking, Monika! J-o-k-i-n-g."
    mc "I... have to agree with Sayori a bit, though. You did kinda brag about your poem's quality."
    m "And here I thought I had you on my side, [player]."
    m "You meanie..."

    "After these two showed me their poems, I glance at Natsuki and Yuri."
    "It seems like they're discussing something."

    mc "Are you guys okay here?"
    n "Yeah, we're fine. We were just comparing each other's poems."
    n "Yuri's poem is super classy, as usual. I actually... kinda like it."

    "Her voice trails off as she finishes the sentence."

    n "{i}apart from this language, that is...{/i}"

    "Ah, yes, {i}there's{/i} the Natsuki we all know and love."
    "Yuri doesn't catch that last part, thankfully."

    y "Really?"
    y "To be honest, I was afraid you wouldn't..."
    n "Well, I mean, of course it should be amazing, you're one of the smartest students in this school!"
    n "I would be disappointed if it weren't any good..."
    mc "Umm, mind if {i}I{/i} see both of your poems?"
    n "Fine, whatever... It's not as if I care about {i}your{/i} opinion on the matter..."
    n "But Monika's gonna make me share it anyway."

    "Natsuki's poem is written on a sheet of paper in pink ink."
    "Seriously, how can she expect someone {i}not{/i} to consider her cute when she acts like this even with the smallest things?"

    call showpoem(poem_n)

    n "I knew you weren't gonna like it."
    mc "I do like it."
    n "You're just saying that."
    n "I wouldn't expect {i}you{/i} to understand..."
    n "Since you're the type of person that never leaves his house!"
    y "N-Natsuki, that's not very..."
    mc "No, honestly. I like it. Why wouldn't I like your poem?"
    mc "And, hey! I {i}do{/i} leave my house... every once in a while."
    n "Oh really? And where do you go?"
    mc "..."
    mc "The... park or something..?"
    n "Hah... Figures..."
    n "Anyway..."
    n "No one ever seems to take my writing seriously."
    n "They all say that poetry needs to be \"sophisticated\" and mine..."
    n "Let's just say I like it when the poem is easy to read, but its message still manages to hit you hard."
    mc "Like this one, right? The fox beats the lion in the end, so you're saying that the world isn't just about strength."
    n "..."
    mc "That the underdog always has a chance."
    n "..."
    mc "Hey, Natsuki, this is just a guess, but are you the fox in this poem?"
    n "N-no!"
    n "I mean..."
    mc "Never mind, you don't have to answer that."
    n "Hmph!"
    mc "Anyway, can I see your poem now, Yuri?"
    y "Please do! I really hope you'll enjoy it."

    "Like Monika, Yuri tends to write all of her poems in a small notebook."
    "Which I could actually call a private diary of sorts, considering her personality."
    "Her handwriting is even more beautiful, almost calligraphic..."

    call showpoem(poem_y)

    mc "..."
    y "How was it? Did you enjoy it? O-Or did it weird you out?!"
    y "Oh gosh, I-{nw}"
    mc "Calm down, Yuri. I really like your poem."
    y "R-Really?"
    mc "Yeah. It paints a really pretty picture. I can almost imagine what it looks like."
    y "Thanks... I tried my best to convey nature's beauty in my poem."
    y "I... I just wasn't sure if I used too many eccentric words, or..."
    mc "Not at all. You did a great job."
    mc "This is more than good enough for the festival."
    y "You... think so?"
    y "I'm... flattered."
    mc "You don't need to feel flattered. It was a great poem after all."
    n "Ugh, get a room, you two..."
    y "Umm, what do you mean, Nats..."

    "Yuri trails off and her eyes widen as she realises what that comment meant."

    y "Ehhh... umm..."

    "{i}Natsuki...{/i}"

    n "Anyway, I have a huge question for you, [player].."
    mc "Huh? What's that?"
    n "Where is {i}your{/i} poem?"
    mc "Oh... Umm..."

    "Crap!"
    "After yesterday's club activities I left in such a hurry that I completely forgot to write a poem for the festival!"

    mc "I... kinda... left it at home...?"

    "Wow, nice one, genius..."
    "{i}Totally{/i} believable..."

    n "Are you serious?! Did you really leave it at home or did you just forget to write it?"
    y "Oh my..."

    "I turn my head to face the other girls, who are staring at me with disapproving eyes."
    "They must've overheard Natsuki's comment."
    "Here it comes..."

    s "That's not fair! We tried our hardest to write a poem for the festival..."
    s "Yet [player] didn't even try to make one.."
    m "Well, I don't think it's that big of a big deal. After all, you can bring it tomorrow."
    m "We all make mistakes every now and then..."
    mc "..."

    "I feel like I'm being talked to like a child who knocked over the cookie jar."
    "Though, admittedly, this is what I deserve for disappointing everyone."
    "I've never felt more guilty over something so small in my whole life."

    n "Don't let him off the hook so easily, Monika! Times like these call for discipline, not nurturing!"
    n "I suggest that as punishment, [player] will have to write 50 poems by tomorrow!"
    mc "What?! Come on, show a little mercy, will you?"
    m "You don't have to be so cold to him, Natsuki..."
    m "It's just a poem, after all."
    n "Hmph!"

    "With the meeting over, it was finally time for us to go home."
    "I almost drag Sayori out of the clubroom, trying to get away from my guilt as soon as possible."

    # fast forward screen
    scene bg residential_day with dissolve_scene_full
    play music t8  # Daijoubu!

    s "Hey, are you okay?"
    mc "Hm? Why do you ask?"
    s "You kinda spaced out while we were walking. {i}Again{/i}..."
    mc "Oh, I was just thinking about the poem I'm supposed to write for tomorrow."
    mc  "Even after reading everyone else's..."
    mc  "I'm still stuck on what I'd like to write about..."
    s "Oh, I see.."
    s "Hey, would you like for me to come over and help?"
    mc "Come over to my place just to help me write a poem?"
    mc "You just want to spend more time with me, don't you?"

    "She {i}has{/i} been trying to use every opportunity she can for us to spend time together ever since I joined the club."

    s "Hey! I was just trying to help..."
    mc "Heh... No thanks, Sayori, I can handle it myself."
    mc "You worry about me too much."
    mc "Now go home and rest early."
    mc "You'd better not wake up late again tomorrow!"
    s "Hah! Look who's talking!"
    mc "Hahah... Yeah, you got me there..."

    "I smile as I wave her goodbye, before walking home."
    "I couldn't help but notice a sad look in her eyes when I turned down her offer..."
    "It's probably nothing. We haven't really spent time together outside of school since we were younger."
    "And besides, we'll see each other on the way to school tomorrow."

    # fast forward screen
    scene bg kitchen with wipeleft_scene

    "When I get home, I start regretting not accepting Sayori's offer..."
    "Even just to have someone to talk to."
    "But I try not to let it bother me and distract myself by cooking dinner."

    # fast forward screen
    scene bg bedroom_night with wipeleft_scene

    "After my bath, I find nothing better to do than to start thinking about making a poem."

    mc "Man, finding a topic is going to be hard..."

    "What should I even write about?"
return

label prologue_day_3:
    # fast forward screen
    scene bg bedroom
    play music t2  # Ohayou Sayori!

    $ s_name = "???"
    s "Hey! Wake up!!!"

    "Huh?"
    "I hear an annoying girl shouting from outside my house."
    "I get up from my bed to look out my window."
    "\[...\]"
    "I see Sayori outside, waving at me."
    "Am I about to be late again?"
    "Without wasting any more time, I get ready as fast as I can and run to meet Sayori outside."

    # fast forward screen
    scene bg residential_day with dissolve_scene_full

    $ s_name = "Sayori"
    s "A-ha! I woke up earlier than you this time!"
    mc "Yeah, yeah... I must've taken a while to think of a topic for my poem last night.."

    "I say that just so she gets the gist of the reason I woke up this late."

    s "But you {i}did{/i} sleep last night, right?"

    "I nod my head and start walking to school, desperately fighting the urge to collapse right then and there on the sidewalk."

    # fast forward screen
    scene bg corridor with wipeleft_scene

    "With the first class over, Sayori and I meet each other in the corridor."
    "I felt a bit dizzy while I was in class; a side effect of getting fewer than six hours of sleep and still dragging myself to school."
    "My stomach was making all kinds of noises throughout the morning, too."
    "It was probably what I made for dinner last night or something."

    s "Hey, you didn't forget to eat breakfast, right?"
    mc "Huh?"
    s "You look pale... and in pain."

    "Oh yeah, I forgot to have my breakfast on top of that."
    "What a way to start the day."
    "Sayori seems worried, which she often is whenever I look even half as terrible as I do today."

    mc "Don't worry Sayori, I'm fine.."

    "I'll just get something to eat at the cafeteria after our next class, then I'll be okay."

    s "You're not going to get sick, right?"
    s "If you are, I'll come over and stay the night."
    mc "What?! No! No way, Sayori, this is just wrong!"
    s "I'm serious, [player]!"
    s "I don't want to see you fall sick! It would make me really sad..."

    "Sayori, oblivious to the scandalous nature of her statement, looks up at me with concerned eyes."

    mc "Really, I'm fine, Sayori. Don't worry about me."
    mc  "I'd feel better if you came to the cafeteria with me, how about that?"
    s "Hmmm..."
    s "Okay! I'll treat you to something! They might even have some garlic bread today!"
    mc "Sounds good."

    # fast forward scene
    scene bg canteen with wipeleft_scene

    "Class goes by faster than I anticipated. The teacher gives us our assignments and leaves the class."
    "Masses of students start heading to the cafeteria."
    "In a matter of minutes, I find myself standing at a crowded cafeteria along with Sayori."

    s "Wow... There's a lot of people here... I wonder if I'll be able to squeeze through and get something.."
    mc "To be honest, I think it's better if we don't eat here... It's way too crowded."
    s "No! I promised I'd get you something to eat, after all!"
    s "Wait here!"

    "Sayori rushes into the crowd, disappearing from sight."
    "I slowly look for two seats that aren't occupied and eventually notice Monika and Yuri together, having their break."
    "Monika waves for me to come and join them."

    m "Hey, [player]! I rarely see you around here."
    m "Come, have a seat."
    mc "Oh... thanks, Monika, hey Yuri."
    y "Good to to see you, [player]."
    m "Did you come here alone?"
    mc "No, I'm here with Sayori."
    mc "She should be in line right now... Said that she'd buy me a garlic bread or something..."
    mc  "By the way, where's Natsuki?"
    y "Probably eating her homemade cupcakes at her own class, if I had to guess."
    y "She says the canteen food is too greasy for her tastes."
    m "Yeah, I'm afraid she has a point..."
    y "I agree..."

    "Sayori suddenly appears next to us, panting heavily."

    s "Haaah, s-sorry to keep you waiting... hah..."
    s "There was so little space in that crowd to breathe... I had to push myself in there to buy it..."
    s "Here! Your garlic bread!"
    mc "Thanks, Sayori. Why don't you grab a seat?"

    "I'm always amazed at the lengths Sayori goes to do the smallest things for me."
    "If Natsuki was here, she would've said something like:"

    scene white with dissolve_cg
    play music t7  # Poem Panic!

    n "You're the absolute worst, you know? You've made a {i}girl{/i} push through a crowd just to buy {i}you{/i} some food?! How pathetic..."

    scene canteen with dissolve_cg
    play music t2  # Ohayou Sayori!

    mc  "{i}sigh{/i}"

    "I would've done it myself, but Sayori was dead set on getting it for me."
    "And I really don't want her to worry too much."
    "After lunch, we go back to our respective classes and start our lessons again."
    "Sayori seems more at ease now, but I can tell she's still concerned."

    # fast forward screen
    scene club_day
    stop music fadeout 2.0

    "With classes finally over, I go to the clubroom, making sure that I didn't forget my poem as I go."

    play sound closet_open

    "\[...\]"

    mc "Hmm, looks like I'm the first one here this time around..."

    "They're probably late or something, I guess I'll just take a seat and wait."

return
