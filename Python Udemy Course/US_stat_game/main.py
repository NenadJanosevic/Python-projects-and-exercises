import pandas 
import turtle

# def get_cor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_cor)

screen = turtle.Screen()
screen.title("U.S   States Game")
screen.setup(725,491)
screen.bgpic("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guess_states = []

while len(guess_states) < 50:
    anwser = screen.textinput(title = f"{len(guess_states)} / 50 States Correct", prompt = "Whats another state name" ).title()
    if anwser == "Exit":
        missing_states = [state for state in all_states if state not in guess_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if anwser in all_states:
        guess_states.append(anwser)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == anwser]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(anwser)

screen.exitonclick()


