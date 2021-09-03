import turtle
import time
import random

wn = turtle.Screen()
wn.title("Gardening Game by Alex!")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

player = turtle.Turtle()
player.speed(0)
player.shape("square")
player.color("white")
player.shapesize(stretch_wid = 4, stretch_len = 2)
player.penup()
player.goto(0,0)

failed = False

plant1 = turtle.Turtle()
plant1.speed(0)
plant1.shape("square")
plant1.color("green")
plant1.shapesize(stretch_wid = 2, stretch_len = 1)
plant1.penup()
plant1.goto(-250,-100)
e1 = 100.0
qe1 = 1.0

plant2 = turtle.Turtle()
plant2.speed(0)
plant2.shape("square")
plant2.color("green")
plant2.shapesize(stretch_wid = 2, stretch_len = 1)
plant2.penup()
plant2.goto(-125,-100)
e2 = 99.0
qe2 = 1.0

plant3 = turtle.Turtle()
plant3.speed(0)
plant3.shape("square")
plant3.color("green")
plant3.shapesize(stretch_wid = 2, stretch_len = 1)
plant3.penup()
plant3.goto(0,-100)
e3 = 99.0
qe3 = 1.0

plant4 = turtle.Turtle()
plant4.speed(0)
plant4.shape("square")
plant4.color("green")
plant4.shapesize(stretch_wid = 2, stretch_len = 1)
plant4.penup()
plant4.goto(125,-100)
e4 = 100.0
qe4 = 1.0

water_bassin = turtle.Turtle()
water_bassin.speed(0)
water_bassin.shape("square")
water_bassin.color("turquoise")
water_bassin.shapesize(stretch_wid = 3, stretch_len = 4)
water_bassin.penup()
water_bassin.goto(250,-100)
water_score = 8

display_water_score = turtle.Turtle()
display_water_score.speed(0)
display_water_score.color("white")
display_water_score.penup()
display_water_score.hideturtle()
display_water_score.goto(-330,260)
display_water_score.write("Water: {}/8".format (water_score), align = "center", font = ('Arial',24,'normal'))

def go_left():
    x = player.xcor()
    x = x - 125
    player.setx(x)
    wn.update()

def go_right():
    x = player.xcor()
    x = x + 125
    player.setx(x)
    wn.update()



def watering():
    global e1, e2, e3, e4, water_score
    if water_score == 0:
        return
    x = player.xcor()
    if x == -250:
        e1 += 33
        water_score -= 1
        update_water_score()
    elif x == -125:
        e2 += 33
        water_score -= 1
        update_water_score()
    elif x == 0:
        e3 += 33
        water_score -= 1
        update_water_score()
    elif x == 125:
        e4 += 33
        water_score -= 1
        update_water_score()

def refill():
    global water_score
    if water_score == 8:
        return
    x = player.xcor()
    if x == 250:
        water_score += 1
        update_water_score()

def update_water_score():
    global water_score
    display_water_score.clear()
    display_water_score.write("Water: {}/8".format (water_score), align = "center", font = ('Arial',24,'normal'))
    wn.update()

def check_failed():
    if e1 < 0 and e2 < 0:
        failed = True
        print ("Git gud")
    elif e1 < 0 and e3 < 0:
        failed = True
        print ("Git gud")
    elif e1 < 0 and e4 < 0:
        failed = True
        print ("Git gud")
    elif e2 < 0 and e3 < 0:
        failed = True
        print ("Git gud")
    elif e2 < 0 and e4 < 0:
        failed = True
        print ("Git gud")
    elif e3 < 0 and e4 < 0:
        failed = True
        print ("Git gud")

wn.listen()
wn.onkeypress(go_right, 'Right')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(watering, 'w')
wn.onkeypress(refill, 's')

wn.update()

delay = 200

def timer1():
    global e1, qe1, delay, plant1
    e1 -= qe1
    check_failed()
    draw_plant(plant1, e1)
    wn.ontimer(timer1, delay)

def timer2():
    global e2, qe2, delay
    e2 -= qe2
    check_failed()
    draw_plant(plant2, e2)
    wn.ontimer(timer2, delay)

def timer3():
    global e3, qe3, delay
    e3 -= qe3
    check_failed()
    draw_plant(plant3, e3)
    wn.ontimer(timer3, delay)

def timer4():
    global e4, qe4, delay
    e4 -= qe4
    check_failed()
    draw_plant(plant4, e4)
    wn.ontimer(timer4, delay)

wn.ontimer(timer1, delay)
wn.ontimer(timer2, delay)
wn.ontimer(timer3, delay)
wn.ontimer(timer4, delay)

def draw_plant(plant, e):
    color = "green"
    if e <= 0:
        color = "grey"
    elif e <= 33:
        color = "brown"
    elif e <= 66:
        color = "yellow"
    
    plant.speed(0)
    plant.shape("square")
    plant.color(color)
    plant.shapesize(stretch_wid = 2, stretch_len = 1)
    plant.penup()
    wn.update()

wn.mainloop()
