import turtle
import pandas
from writer import Writer

screen = turtle.Screen()
writer = Writer()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")

title = "Guess the State"
count = 0
answered_states = []

while count < 50:
    answer_state = screen.textinput(title=title, prompt="What's another state's name?")
    if answer_state is None or answer_state == "Exit":
        break

    state_row = data[data['state'].str.lower() == answer_state.lower()]

    if state_row.empty:
        continue

    [state, x, y] = state_row.values[0]
    if state in answered_states:
        continue
    else:
        count += 1
        answered_states.append(state)
        writer.write_content(x, y, state)
        title = f"{count}/50 States Correct"


all_states = data.state.to_list()
unanswered_states = [s for s in all_states if s not in answered_states]
unanswered_states_frame = pandas.DataFrame(unanswered_states)
unanswered_states_frame.to_csv("states_to_learn.csv")


turtle.mainloop()
