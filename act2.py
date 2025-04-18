from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors = ["green", "black", "blue", "pink", "cyan"]
   
def color():
    "Return a random color"
    return colors[randrange(len(colors))]

def reviewColor():
    "Make sure that snake and food have different color"
    snakeColor = color()
    foodColor = color()
    while snakeColor == foodColor:
        foodColor = color()
    return snakeColor, foodColor

def move_food():
    "Move food one step randomly."
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move_direction = directions[randrange(len(directions))]

    new_food = food + move_direction
    if inside(new_food):  # Verifica que la comida no salga de los límites
        food.move(move_direction)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def turn(head):
    "Allows the snake to turn around the edges"
    if head.x > 190:
        head.x = -190
    elif head.x < -190:
        head.x = 90
    if head.y > 190:
        head.y = -190
    elif head.y < -190:
        head.y = 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    turn(head)

    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeColor)

    square(food.x, food.y, 9, foodColor)
    move_food() #Llamar a la función para mover la comida aleatoriamente un paso a la vez.
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
snakeColor, foodColor = reviewColor()
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
