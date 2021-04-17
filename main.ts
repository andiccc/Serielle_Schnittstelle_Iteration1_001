serial.onDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    Zeile_seriell = serial.readUntil(serial.delimiters(Delimiters.NewLine))
    if (Zeile_seriell == "Temp") {
        id = 1
    }
    if (Zeile_seriell == "Licht") {
        id = 2
    }
})
let Zeile_seriell = ""
let id = 0
id = 0
basic.forever(function () {
    basic.clearScreen()
    if (id == 1) {
        serial.writeValue("Temp", input.temperature())
        basic.showLeds(`
            # # # # #
            . . # . .
            . . # . .
            . . # . .
            . . # . .
            `)
    } else if (id == 2) {
        serial.writeValue("Licht", input.lightLevel())
        basic.showLeds(`
            # . . . .
            # . . . .
            # . . . .
            # . . . .
            # # # . .
            `)
    } else {
        basic.showIcon(IconNames.No)
    }
})
