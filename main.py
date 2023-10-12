def zobraz_XY():
    led.plot(X, Y)
def trefaStred():
    global TREFA
    if TREFA == 1:
        basic.show_leds("""
            . . . . .
            . # # # .
            . # . # .
            . # # # .
            . . . . .
            """)
        basic.pause(500)
        basic.clear_screen()
        TREFA = 0

def on_button_pressed_a():
    global TREFA
    if X == 2 and Y == 2:
        TREFA = 1
    else:
        TREFA = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def posun_Y():
    global Y
    Y += 1
    if Y > 4:
        Y = 0
def posun_X():
    global X
    X += 1
    if X > 4:
        X = 0
        posun_Y()
TREFA = 0
X = 0
Y = 0
basic.show_icon(IconNames.HAPPY)
basic.pause(500)
basic.clear_screen()
Y = 0
X = 0

def on_forever():
    zobraz_XY()
    basic.pause(250)
    basic.clear_screen()
    basic.pause(250)
    posun_X()
    trefaStred()
basic.forever(on_forever)
