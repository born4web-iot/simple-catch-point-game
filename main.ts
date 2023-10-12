function zobraz_XY () {
    led.plot(X, Y)
}
function trefaStred () {
    if (TREFA == 1) {
        basic.showLeds(`
            . . . . .
            . # # # .
            . # . # .
            . # # # .
            . . . . .
            `)
        basic.pause(500)
        basic.clearScreen()
        TREFA = 0
    }
}
input.onButtonPressed(Button.A, function () {
    if (X == 2 && Y == 2) {
        TREFA = 1
    } else {
        TREFA = 0
    }
})
function posun_Y () {
    Y += 1
    if (Y > 4) {
        Y = 0
    }
}
function posun_X () {
    X += 1
    if (X > 4) {
        X = 0
        posun_Y()
    }
}
let TREFA = 0
let X = 0
let Y = 0
basic.showIcon(IconNames.Happy)
basic.pause(500)
basic.clearScreen()
Y = 0
X = 0
basic.forever(function () {
    zobraz_XY()
    basic.pause(250)
    basic.clearScreen()
    basic.pause(250)
    posun_X()
    trefaStred()
})
