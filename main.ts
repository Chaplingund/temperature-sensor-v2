let r = 0
let i = 0
let u = 0
let u_raw = 0
let r_target = 100
basic.forever(function () {
    u_raw = 0
    // imports amount of voltage, from 0-1023
    u_raw = pins.analogReadPin(AnalogPin.P0)
    basic.showNumber(u_raw)
    // maps amount of voltage to a 0-3 scale
    u = Math.map(u_raw, 0, 1023, 0, 3)
    // calculates current
    i = u / 1000
    // calculates resistance
    r = (3 - u) / i
    // triggers on too high resistance
    if (r >= r_target) {
        basic.showLeds(`
            . . # . .
            . # # # .
            # # # # #
            . . # . .
            . . # . .
            `)
        pins.digitalWritePin(DigitalPin.P1, 1023)
    } else {
        basic.showLeds(`
            . # . # .
            . # . # .
            . . . . .
            # . . . #
            . # # # .
            `)
    }
})
