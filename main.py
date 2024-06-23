import turtle
from turtle import Turtle, Screen
import pandas
screen = Screen()
screen.title("U.S. 50 States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
game_on = True
states_as_list = data.state.tolist()
guessed_state = []
correct_state = 0
while game_on:
    screen.update()

    answer_state = screen.textinput(title=f"{correct_state}/50 States Correct", prompt="Name another State").title()
    if answer_state in states_as_list:
        guessed_state.append(answer_state)
        writer = Turtle()
        writer.penup()
        writer.hideturtle()
        state_to_check = data[data.state == answer_state]
        writer.goto(int(state_to_check.x), int(state_to_check.y))
        writer.write(answer_state)
        correct_state += 1
    if answer_state == "Exit":
        missing_states = [state for state in states_as_list if state not in guessed_state]
        new_file = pandas.DataFrame(missing_states)
        new_file.to_csv("states_to_learn.csv")
        break
    if correct_state == 50:
        game_on = False












# basically the same as exitonclick but it allows the screen to be on even though our codes are done running
# turtle.mainloop()



