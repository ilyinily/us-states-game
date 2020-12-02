from turtle import Turtle, Screen
import pandas as pd

# Initial setup
screen = Screen()
twix = Turtle()
twix.hideturtle()
twix.penup()
screen.bgpic(picname="./blank_states_img.gif")

# Getting data from the dataset
dataset = pd.read_csv("./50_states.csv")

# Formatting the state names to lowercase for convenience
# for i in range(len(dataset['state'])):
#     dataset['state'][i] = dataset['state'][i].lower()

correct_answers = set()
misses = set()

game_continues = True
while game_continues:
    answer = screen.textinput(title=f"Guessed {len(correct_answers)} states of 50", prompt="Enter the state:")
    if answer.title() in dataset['state'].values:
        correct_answers.add(answer)
        twix.setposition(x=int(dataset[dataset['state'] == answer.title()]['x']), y=int(dataset[dataset['state'] == answer.title()]['y']))
        twix.write(arg=answer.title())
    elif answer.lower() == "exit":
        game_continues = False
    else:
        misses.add(answer.title())
    if len(correct_answers) == 50:
        game_continues = False

print(f"Game over.\nYou have successfully guessed {len(correct_answers)} states.")

screen.exitonclick()
