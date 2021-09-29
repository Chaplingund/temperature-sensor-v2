let voltage_raw = 0
let u = 0
let r = 0
let i = 0
basic.forever(function on_forever() {
    
    //  imports amount of voltage, from 0-1023
    voltage_raw = pins.analogReadPin(AnalogPin.P0)
    basic.showNumber(voltage_raw)
    //  maps amount of voltage to a 0-3 scale
    u = Math.map(voltage_raw, 0, 1023, 0, 3)
    //  calculates current
    i = u / 1000
    //  calculates resitance
    r = (3 - u) / i
    basic.showNumber(r)
})
