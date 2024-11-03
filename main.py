def en_polsar_boto_a():
    temperatura = input.temperature()
    basic.show_string("Calor" if temperatura > 22 else "Fred")
input.on_button_pressed(Button.A, en_polsar_boto_a)

def en_polsar_boto_b():
    llum = input.light_level()
    if llum < 50:
        music.play(music.string_playable("E D G F B A C5 B", 120), music.PlaybackMode.UNTIL_DONE)
    elif llum > 200:
        music.play(music.string_playable("E B C5 A B G A F", 120), music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.B, en_polsar_boto_b)

basic.show_icon(IconNames.HEART)
