init python:
    class Poem:
        def __init__(self, author="", title="", text="", yuri_2=False, yuri_3=False):
            self.author = author
            self.title = title
            self.text = text
            self.yuri_2 = yuri_2
            self.yuri_3 = yuri_3

        @property
        def num_words(self):
            replaced = self.text.replace("\n", " ").replace("-", "")
            words = [word for word in replaced.split(" ") if word]
            return len(words)

    poem_m = Poem(
    author = "monika",
    title = "Just Another World",
    text = """\
Life that idles
Swiftly floats into the abyss,
The dark abyss known as stagnation.
Within it, life decays, bringing but pain and sorrow.
It tears through us, in a slow, endless torment,
Through the mind, body, and soul.

Life that storms
Leaves a scar,
The one that scarred another world.
The air of this new world flows through us -
A breeze that brings purpose and satisfaction
Through the mind, body, and soul.

We long for a revelation,
An answer we shall bring ourselves to accept.
The reality between us and the world we dream of -
None of it is real.
This world isn't ours -
Only our lives are.

Our world is just another world."""
    )

    poem_s = Poem(
    author = "sayori",
    title = "Winds",
    text = """\
I hear the winds' gentle breeze outside my window.
I see tree branches swaying lazily.
Kids in the nearby park fly kites against the mostly blue skies,
And part of me wants to join them.

I close my eyes.

I hear the winds' stronger gusts rattle against my skull.
I see the branches crashing wildly.
The sky darkens, the near-blue clarity now full of clouds.
It looks like it might rain.

The winds grow stronger, howling now.
The branches groan and creak under the weight of the winds.
These sounds overwhelm my mind and it's all I can hear.
The sky darkens... darkens... darkens... until it's just clouds -
The sun hid a long time ago.

Are those kids still there?
Their kites won't last long in these winds.
Are those kids still there?
I certainly don't want to join them.

I open my eyes.

The sun shines."""
    )

    poem_n = Poem(
    author = "natsuki",
    title = "{color=#FF1493}The Fox{/color}",
    text = """\
{color=#FF1493}The lion was proud
And its prey feared its strength.
The birds hid in fear.
The rabbits hid in fear.
The zebras hid in fear.
But the fox didn’t hide.
The fox ran.
The lion chased.
The fox and lion ran around a corner.
And the lion fell in a trap.
And the fox didn’t need to run anymore.{/color}"""
    )

    poem_y = Poem(
    author = "yuri",
    title = "Aurora",
    text = """\
Far from everything she finds herself,
A lone, hooded figure traversing the open tundra,
An outcast, desperate to stay warm.
The harsh winds of winter strike at her frame –
Behind little shelter she cowers, almost whimpering.
   It is little wonder her path is nearly bare of travel.

She perseveres, placing one foot forward, mechanically,
The burdens she carries, neglected by others, ignored at last.
The vibrant blurs of green and pink dare her to look at the once-dark sky above.
The harsh winds of winter match not the wild flare of solar winds.
With these brilliant colors from a conflict born,
   It is great wonder her path is nearly bare of travel."""
    )

image paper = "images/bg/poem.jpg"
image paper_glitch = LiveComposite((1280, 720), (0, 0), "paper_glitch1", (0, 0), "paper_glitch2")
image paper_glitch1 = "images/bg/poem-glitch1.png"
image paper_glitch2:
    "images/bg/poem-glitch2.png"
    block:
        yoffset 0
        0.05
        yoffset 20
        0.05
        repeat


transform paper_in:
    truecenter
    alpha 0
    linear 1.0 alpha 1

transform paper_out:
    alpha 1
    linear 1.0 alpha 0

screen poem(currentpoem, paper="paper"):
    style_prefix "poem"
    vbox:
        add paper
    viewport id "vp":
        child_size (710, None)
        mousewheel True
        draggable True
        has vbox
        null height 40
        if currentpoem.author == "yuri":
            if currentpoem.yuri_2:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
            elif currentpoem.yuri_3:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text_3"
            else:
                text "[currentpoem.title]\n\n[currentpoem.text]" style "yuri_text"
        elif currentpoem.author == "sayori":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "sayori_text"
        elif currentpoem.author == "natsuki":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "natsuki_text"
        elif currentpoem.author == "monika":
            text "[currentpoem.title]\n\n[currentpoem.text]" style "monika_text"
        null height 100
    vbar value YScrollValue(viewport="vp") style "poem_vbar"



style poem_vbox:
    xalign 0.5
style poem_viewport:
    xanchor 0
    xsize 720
    xpos 280
style poem_vbar is vscrollbar:
    xpos 1000
    yalign 0.5

    ysize 700





style yuri_text:
    font "gui/font/y1.ttf"
    size 32
    color "#000"
    outlines []

style yuri_text_2:
    font "gui/font/y2.ttf"
    size 40
    color "#000"
    outlines []

style yuri_text_3:
    font "gui/font/y3.ttf"
    size 18
    color "#000"
    outlines []
    kerning -8
    justify True

style natsuki_text:
    font "gui/font/n1.ttf"
    size 28
    color "#000"
    outlines []
    line_leading 1

style sayori_text:
    font "gui/font/s1.ttf"
    size 34
    color "#000"
    outlines []

style monika_text:
    font "gui/font/m1.ttf"
    size 34
    color "#000"
    outlines []

label showpoem(poem=None, music=True, track=None, revert_music=True, img=None, where=i11, paper=None):
    if poem == None:
        return
    play sound page_turn
    if music:
        $ currentpos = get_pos()
        if track:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>" + track
        else:
            $ audio.t5b = "<from " + str(currentpos) + " loop 4.444>bgm/5_" + poem.author + ".ogg"
        stop music fadeout 2.0
        $ renpy.music.play(audio.t5b, channel="music_poem", fadein=2.0, tight=True)
    window hide
    if paper:
        show screen poem(poem, paper=paper)
    else:
        show screen poem(poem)
    if not persistent.first_poem:
        $ persistent.first_poem = True
        show expression "gui/poem_dismiss.png" as poem_dismiss:
            xpos 1050 ypos 590
    with Dissolve(1)
    $ pause()
    if img:
        $ renpy.hide(poem.author)
        $ renpy.show(img, at_list=[where])
    hide screen poem
    hide poem_dismiss
    with Dissolve(.5)
    window auto
    if music and revert_music:
        $ currentpos = get_pos(channel="music_poem")
        $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
        stop music_poem fadeout 2.0
        $ renpy.music.play(audio.t5c, fadein=2.0)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
