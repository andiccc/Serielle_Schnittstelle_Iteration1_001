def on_data_received():
    global Zeile_seriell, id2
    Zeile_seriell = serial.read_until(serial.delimiters(Delimiters.NEW_LINE))
    if Zeile_seriell == "Temp":
        id2 = 1
    if Zeile_seriell == "Licht":
        id2 = 2
serial.on_data_received(serial.delimiters(Delimiters.NEW_LINE), on_data_received)

Zeile_seriell = ""
id2 = 0
id2 = 1

def on_forever():
    basic.clear_screen()
    if id2 == 1:
        serial.write_value("Temp", input.temperature())
        basic.show_leds("""
            # # # # #
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            """)
    elif id2 == 2:
        serial.write_value("Licht", input.light_level())
        basic.show_leds("""
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            # # # . .
            """)
    else:
        basic.show_icon(IconNames.NO)
basic.forever(on_forever)
