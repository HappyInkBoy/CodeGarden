import turtle
import time
import random

colors = ["red","green","blue","white","yellow"]

def random_color_recursive(current_color):
    new_color = colors[random.randint(0, len(colors) - 1)]
    if new_color == current_color:
        print ("You shat shit")
        return random_color(current_color)
    return new_color

def random_color(current_color):
    while True:
        new_color = colors[random.randint(0, len(colors) - 1)]
        if new_color != current_color:
            print ("you win yay...")
            return new_color

bumper_color = random_color("yahoo")
delay = 1.0
max = 100

score1 = 0
score2 = 0

wn = turtle.Screen()
wn.title("Colour Press by Alex")
wn.bgcolor("black")
wn.setup(width = 600, height = 600)
wn.tracer(0)

scoreboard = turtle.Turtle()
scoreboard.speed(0)
scoreboard.color("white")
scoreboard.penup()
scoreboard.hideturtle()
scoreboard.goto(0,260)
scoreboard.write("Player 1: {}  Player 2: {}".format (score1, score2), align = "center", font=('Arial',24,'normal'))

wintext = turtle.Turtle()
wintext.speed(0)
wintext.color("white")
wintext.penup()
wintext.hideturtle()
wintext.goto(0,180)

bumper = turtle.Turtle()
bumper.speed(0)
bumper.shape("square")
bumper.color(bumper_color)
bumper.shapesize(stretch_wid = 10, stretch_len = 10)
bumper.penup()
bumper.goto(0,0)

def press1():
    global score1, score2, bumper_color, max
    if bumper_color == "yellow":
        bumper_color = "black"
        score1 += 1
        scoreboard.clear()
        scoreboard.write("Player 1: {}  Player 2: {}".format (score1, score2), align = "center", font = ('Arial',24,'normal'))
        bumper.speed(0)
        bumper.shape("square")
        bumper.color(bumper_color)
        bumper.shapesize(stretch_wid = 10, stretch_len = 10)
        bumper.penup()
        bumper.goto(0,0)
        bumper.clear()
        wintext.clear()
        wintext.write("Player 1 wins!", align = "center", font = ('Arial',32,'normal'))
        max = 300
    elif bumper_color == "black":
        return
    else: 
        score1 -= 1
        scoreboard.clear()
        scoreboard.write("Player 1: {}  Player 2: {}".format (score1, score2), align = "center", font=('Arial',24,'normal'))

def press2():
    global score1, score2, bumper_color, max
    if bumper_color == "yellow":
        bumper_color = "black"
        score2 += 1
        scoreboard.clear()
        scoreboard.write("Player 1: {}  Player 2: {}".format (score1, score2), align = "center", font=('Arial',24,'normal'))
        bumper.speed(0)
        bumper.shape("square")
        bumper.color(bumper_color)
        bumper.shapesize(stretch_wid = 10, stretch_len = 10)
        bumper.penup()
        bumper.goto(0,0)
        bumper.clear()
        wintext.clear()
        wintext.write("Player 2 wins!", align = "center", font = ('Arial',32,'normal'))
        max = 300
    elif bumper_color == "black":
        return
    else: 
        score2 -= 1
        scoreboard.clear()
        scoreboard.write("Player 1: {}  Player 2: {}".format (score1, score2), align = "center", font=('Arial',24,'normal'))

wn.listen()
wn.onkeypress(press1, 'w')
wn.onkeypress(press2, 'm')

counter = 0

while True:
    wn.update()
    counter += 1
    if counter > max:
        counter = 0
        max = 100
        time.sleep(delay)
        bumper_color = random_color(bumper_color)
        bumper.speed(0)
        bumper.shape("square")
        bumper.color(bumper_color)
        bumper.shapesize(stretch_wid = 10, stretch_len = 10)
        bumper.penup()
        bumper.goto(0,0)
        wintext.clear()
