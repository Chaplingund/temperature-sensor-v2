voltage_raw = 0
voltage = 0
resistance = 0

def on_forever():
    global voltage_raw, voltage, resistance
    # imports amount of voltage, from 0-1023
    voltage_raw = pins.analog_read_pin(AnalogPin.P0)
    basic.show_number(voltage_raw)
    # maps amount of voltage to a 0-3 scale
    voltage = Math.map(voltage_raw, 0, 1023, 0, 3)
    # triggers on minimum amount of voltage reached
    resistance = (3 - voltage) / 0.16
basic.forever(on_forever)
