import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.penup()
pen.hideturtle()

game_is_on = True

states_data = pandas.read_csv('50_states.csv')
right_guesses = []

while len(right_guesses) < 50:
    answer_state = screen.textinput(title=f"You guessed {len(right_guesses)}/50 states", prompt="What's another state's name?")
    if answer_state.title() == "Exit":
        break

    right_guess = (states_data[states_data.state == answer_state.title()])

    if not right_guess.empty:
        answer = right_guess.state.item()
        pen.goto(right_guess.x.item(), right_guess.y.item())
        pen.write(answer, font=("Arial", 10, 'normal'))
        if answer not in right_guesses:
            right_guesses.append(answer)

all_states = states_data.state.to_list()
not_guessed_states = list(set(all_states) - set(right_guesses))
not_guessed_states.sort()
data = pandas.DataFrame(not_guessed_states)
data.to_csv("states_to_learn.csv")


