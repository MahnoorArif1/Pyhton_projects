
import pandas as pd
import turtle
import random
from tkinter import messagebox

def tt(state_name, idx):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(X[idx], Y[idx])
    t.write(state_name)

def show_message(msg, title="Message"):
    messagebox.showinfo(title, msg)

Guessed_states = []
correct = 0
screen = turtle.Screen()
screen.title("US STATE GAME")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pd.read_csv("50_states.csv")
states = data['state'].to_list()
X = data['x'].to_list()
Y = data['y'].to_list()

while correct != 50:
    answer = screen.textinput(f"{correct}/50 US States Correct",
                              "Enter a state name (or type 'Hint'/'Exit'):").title()

    if answer == "Exit":
        remaining_states = [s for s in states if s not in Guessed_states]
        pd.DataFrame(remaining_states).to_csv("still.csv")
        show_message("Game exited.")
        break

    elif answer == "Hint":
        remaining_states = [s for s in states if s not in Guessed_states]
        if remaining_states:
            hint_state = random.choice(remaining_states)
            show_message(f"Hint: The state starts with '{hint_state[0]}'", "Hint")
        continue

    elif answer in states and answer not in Guessed_states:
        idx = states.index(answer)
        tt(answer, idx)
        Guessed_states.append(answer)
        correct += 1

    elif answer in Guessed_states:
        show_message("You already guessed that state!")

    else:
        show_message("Incorrect guess, try again!")

screen.bye()  
