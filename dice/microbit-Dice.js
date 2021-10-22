/**
 * This code has been generated in the editor
 */
input.onButtonPressed(Button.A, function () {
    randInt = randint(1, 6)
    if (randInt == 1) {
        basic.showNumber(1)
    } else if (randInt == 2) {
        basic.showNumber(2)
    } else if (randInt == 3) {
        basic.showNumber(3)
    } else if (randInt == 4) {
        basic.showNumber(4)
    } else if (randInt == 5) {
        basic.showNumber(5)
    } else {
        basic.showNumber(6)
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
})
input.onButtonPressed(Button.B, function () {
    basic.showIcon(IconNames.Chessboard)
})
let randInt = 0
basic.showIcon(IconNames.Chessboard)
// Do nothing
basic.forever(function () {
    
})
