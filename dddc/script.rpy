label start:
    # call test
    if not persistent.seen_intro:
        call prologue_intro
        $ persistent.seen_intro = True
    call prologue_day_1
    call prologue_day_2
    call poem
    call prologue_day_3

return
