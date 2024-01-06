from turtle import Turtle, Screen
import random

game_on = False

colors = ["red", "green", "blue", "orange", "purple", "yellow", "brown"]
y_position = [-150, -100, -50, 0, 50, 100, 150]

screen = Screen()
screen.setup(width= 500, height= 400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color : ")
if user_bet:
    game_on = True

turtle_list = []

for turtle in range(0, 7):
    t = Turtle(shape= "turtle")
    t.color(colors[turtle])
    t.pencolor(colors[turtle])
    t.penup()
    t.goto(x=-230, y=y_position[turtle])
    turtle_list.append(t)
    
while game_on:
    for turt in turtle_list:
        if turt.xcor() > 230:
            game_on = False
            win = turt.pencolor()

            if user_bet == win:
                print(f"you {win} win")
            else:
                print(f"you {user_bet} lose , {win} win.")

        r_num = random.randint(0, 10)
        turt.forward(r_num)

screen.exitonclick()