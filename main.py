from turtle import Turtle, Screen
import random
is_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Turtle Race", prompt="Place your bet on which turtle will win!")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-150, -110, -70, -30, 10, 50]

list_of_turtles = []

for index in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[index])
    list_of_turtles.append(new_turtle)


if user_bet:
    is_on = True



while is_on:
    for turtle in list_of_turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() > 230:
            is_on = False
            winning_color = turtle.pencolor()
            print(f"The winning turtle is: {winning_color}!")
            if winning_color == user_bet:
                print("Your chosen turtle has won!")
            else:
                print("Unlucky, your chosen turtle has not won")


screen.exitonclick()