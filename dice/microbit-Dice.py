"""

This code has been generated in the editor

"""

def on_button_pressed_a():
    global randInt
    randInt = randint(1, 6)
    if randInt == 1:
        basic.show_number(1)
    elif randInt == 2:
        basic.show_number(2)
    elif randInt == 3:
        basic.show_number(3)
    elif randInt == 4:
        basic.show_number(4)
    elif randInt == 5:
        basic.show_number(5)
    else:
        basic.show_number(6)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.CHESSBOARD)
input.on_button_pressed(Button.B, on_button_pressed_b)

randInt = 0
basic.show_icon(IconNames.CHESSBOARD)
# Do nothing

def on_forever():
    pass
basic.forever(on_forever)
