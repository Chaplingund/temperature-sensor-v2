r = 0
i = 0
u = 0
voltage_raw = 0
r_target = 100

def on_forever():
    global voltage_raw, u, i, r
    u_raw = 0
    # imports amount of voltage, from 0-1023
    voltage_raw = pins.analog_read_pin(AnalogPin.P0)
    basic.show_number(u_raw)
    # maps amount of voltage to a 0-3 scale
    u = Math.map(voltage_raw, 0, 1023, 0, 3)
    # calculates current
    i = u / 1000
    # calculates resistance
    r = (3 - u) / i
    # triggers on too high resistance
    if r >= r_target:
        basic.show_leds("""
            . # . . .
                        . # . # .
                        . # . # .
                        . # . # .
                        . # . # .
        """)
        pins.digital_write_pin(DigitalPin.P1, 1023)
    else: 
        basic.show_leds("""
                    . # . . .
                                . # . # .
                                . # . # .
                                . # . # .
                                . # . # .
                """)
basic.forever(on_forever)
