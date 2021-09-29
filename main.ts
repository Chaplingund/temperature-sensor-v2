let voltage_raw = 0
let voltage = 0
let resistance = 0
basic.forever(function on_forever() {
    
    //  imports amount of voltage, from 0-1023
    voltage_raw = pins.analogReadPin(AnalogPin.P0)
    basic.showNumber(voltage_raw)
    //  maps amount of voltage to a 0-3 scale
    voltage = Math.map(voltage_raw, 0, 1023, 0, 3)
    //  triggers on minimum amount of voltage reached
    resistance = (3 - voltage) / 0.16
})
