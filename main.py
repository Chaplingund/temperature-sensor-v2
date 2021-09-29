voltage_raw = 0
u = 0
r = 0
i = 0

def on_forever():
    global voltage_raw, u, r, i
    # imports amount of voltage, from 0-1023
    voltage_raw = pins.analog_read_pin(AnalogPin.P0)
    basic.show_number(voltage_raw)
    # maps amount of voltage to a 0-3 scale
    u = Math.map(voltage_raw, 0, 1023, 0, 3)
    # calculates current
    i = u/1000
    # calculates resitance
    r = (3 - u) / i
    
    basic.show_number(r)
basic.forever(on_forever)
