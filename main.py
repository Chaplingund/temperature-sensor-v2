r = 0
i = 0
u = 0
u_raw = 0
r_target = 100

def on_forever():
    global u_raw, u, i, r
    u_raw = 0
    # imports amount of voltage, from 0-1023
    u_raw = pins.analog_read_pin(AnalogPin.P0)
    # maps amount of voltage to a 0-3 scale
    u = Math.map(u_raw, 0, 1023, 0, 3)
    # calculates current
    i = u / 1000
    # calculates resistance
    r = (3 - u) / i
    # triggers on too high resistance
    if r >= r_target:
        basic.show_leds("""
            . . # . .
                        . # # # .
                        # # # # #
                        . . # . .
                        . . # . .
        """)
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        basic.show_leds("""
            . # . # .
                        . # . # .
                        . . . . .
                        # . . . #
                        . # # # .
        """)
basic.forever(on_forever)
