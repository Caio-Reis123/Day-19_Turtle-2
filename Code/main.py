from turtle import Turtle, Screen, color
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet.', prompt='Which turtle will win the race? Enter a color: ')
print(user_bet)

# # Ex. 01 - Mover a turtle manualmente

# def move_forwards():
#     new_turtle.forward(10)

# def move_backwards():
#     new_turtle.back(10)

# def move_right():
#     new_turtle.right(10)

# def move_left():
#     new_turtle.left(10)

# def clear_screen():
#     new_turtle.clear()
#     new_turtle.penup()
#     new_turtle.home()
#     new_turtle.pendown()

# screen.listen()
# screen.onkey(key = 'w', fun = move_forwards)
# screen.onkey(key = 's', fun = move_backwards)
# screen.onkey(key = 'd', fun = move_right)
# screen.onkey(key = 'a', fun = move_left)
# screen.onkey(key = 'c', fun = clear_screen)

# Ex. 02: Turtle Race!

race_is_on = False

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
eixo_y = -60

for turtle_index in range(0,6):

    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=eixo_y)
    eixo_y += 30
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print('You Win!')
            else: 
                print(f'You Lost! The winner is {winning_color}')
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
