import turtle
import time
import random

# Seting up the window
wn = turtle.Screen()
wn.title("Gardening Game by Alex!")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)
wn.bgpic("Background.gif")
wn.addshape("Gardener.gif")
wn.addshape("flower1.gif")
wn.addshape("flower2.gif")
wn.addshape("flower3.gif")
wn.addshape("flower4.gif")

# Player sprite
player = turtle.Turtle()
player.speed(0)
player.shape("Gardener.gif")
player.penup()
player.goto(0,0)

failed = False
paused = False

plant1 = turtle.Turtle()
plant1.speed(0)
plant1.shape("flower1.gif")
plant1.penup()
plant1.goto(-250,-100)
e1 = 100.0
qe1 = random.uniform(1.0, 2.0)

plant2 = turtle.Turtle()
plant2.speed(0)
plant2.shape("flower1.gif")
plant2.penup()
plant2.goto(-125,-100)
e2 = 99.0
qe2 = random.uniform(1.0, 2.0)

plant3 = turtle.Turtle()
plant3.speed(0)
plant3.shape("flower1.gif")
plant3.penup()
plant3.goto(0,-100)
e3 = 99.0
qe3 = random.uniform(1.0, 2.0)

plant4 = turtle.Turtle()
plant4.speed(0)
plant4.shape("flower1.gif")
plant4.penup()
plant4.goto(125,-100)
e4 = 100.0
qe4 = random.uniform(1.0, 2.0)

side_bar_left = turtle.Turtle()
side_bar_left.speed(0)
side_bar_left.shape("square")
side_bar_left.color("white")
side_bar_left.shapesize(stretch_wid = 3, stretch_len = 0.25)
side_bar_left.penup()
side_bar_left.goto(155,250)

water_meter1 = turtle.Turtle()
water_meter1.speed(0)
water_meter1.shape("square")
water_meter1.color("turquoise")
water_meter1.shapesize(stretch_wid = 3, stretch_len = 1)
water_meter1.penup()
water_meter1.goto(350,250)

water_meter2 = turtle.Turtle()
water_meter2.speed(0)
water_meter2.shape("square")
water_meter2.color("turquoise")
water_meter2.shapesize(stretch_wid = 3, stretch_len = 1)
water_meter2.penup()
water_meter2.goto(325,250)

water_meter3 = turtle.Turtle()
water_meter3.speed(0)
water_meter3.shape("square")
water_meter3.color("turquoise")
water_meter3.shapesize(stretch_wid = 3, stretch_len = 1)
water_meter3.penup()
water_meter3.goto(300,250)

water_meter4 = turtle.Turtle()
water_meter4.speed(0)
water_meter4.shape("square")
water_meter4.color("turquoise")
water_meter4.shapesize(stretch_wid = 3, stretch_len = 1)
water_meter4.penup()
water_meter4.goto(275,250)

water_meter5 = turtle.Turtle()
water_meter5.speed(0)
water_meter5.shape("square")
water_meter5.color("turquoise")
water_meter5.shapesize(stretch_wid = 3, stretch_len = 1)
water_meter5.penup()
water_meter5.goto(250,250)

water_meter6 = turtle.Turtle()
water_meter6.speed(0)
water_meter6.shape("square")
water_meter6.color("turquoise")
water_meter6.shapesize(stretch_wid = 3, stretch_len = 1)
water_meter6.penup()
water_meter6.goto(225,250)

water_meter7 = turtle.Turtle()
water_meter7.speed(0)
water_meter7.shape("square")
water_meter7.color("turquoise")
water_meter7.shapesize(stretch_wid = 3, stretch_len = 1)
water_meter7.penup()
water_meter7.goto(200 ,250)

water_meter8 = turtle.Turtle()
water_meter8.speed(0)
water_meter8.shape("square")
water_meter8.color("turquoise")
water_meter8.shapesize(stretch_wid = 3, stretch_len = 1)
water_meter8.penup()
water_meter8.goto(175,250)

water_bassin = turtle.Turtle()
water_bassin.speed(0)
water_bassin.shape("square")
water_bassin.color("turquoise")
water_bassin.shapesize(stretch_wid = 3, stretch_len = 4)
water_bassin.penup()
water_bassin.goto(250,-100)
water_score = 8

display_tip = turtle.Turtle()
display_tip.speed(0)
display_tip.color("white")
display_tip.penup()
display_tip.hideturtle()
display_tip.goto(-385,200)
display_tip.write("Water your plants before they die!", align = "left", font = ('Arial',24,'normal'))

display_water_score = turtle.Turtle()
display_water_score.speed(0)
display_water_score.color("white")
display_water_score.penup()
display_water_score.hideturtle()
display_water_score.goto(-330,230)
display_water_score.write("Water: {}/8".format (water_score), align = "center", font = ('Arial',24,'normal'))

time_score = 0

display_time_score = turtle.Turtle()
display_time_score.speed(0)
display_time_score.color("white")
display_time_score.penup()
display_time_score.hideturtle()
display_time_score.goto (-386,260)
display_time_score.write("Score: {} sec".format (time_score), align = "left", font = ('Arial',24,'normal'))

def score_timer():
    global time_score, display_time_score, delay, paused
    time_score += 1
    if time_score == 20:
        delay = 190
    elif time_score == 25:
        delay = 180
    elif time_score == 30:
        delay = 170
    elif time_score == 40:
        delay = 160
    elif time_score == 50:
        delay = 150
    elif time_score == 60:
        delay = 140
    elif time_score == 70:
        delay = 130
    elif time_score == 80:
        delay = 120
    elif time_score == 90:
        delay = 110
    elif time_score == 100:
        delay = 100
    display_time_score.clear()
    display_time_score.write("Score: {} sec".format (time_score), align = "left", font = ('Arial',24,'normal'))
    wn.update()
    if not failed and not paused:
        wn.ontimer(score_timer, 1000)

paused_text = turtle.Turtle()
paused_text.hideturtle()

def pause_game():
    global paused, paused_text
    paused = not paused
    if paused:
        paused_text.speed(0)
        paused_text.color("white")
        paused_text.penup()
        paused_text.hideturtle()
        paused_text.goto(0,100)
        paused_text.write("Paused", align ="center", font = ('Arial',32,'normal'))
    else:
        paused_text.clear()
    wn.update()
    if not failed and not paused:
        wn.ontimer(score_timer, 1000)
        wn.ontimer(timer1, delay)
        wn.ontimer(timer2, delay)
        wn.ontimer(timer3, delay)
        wn.ontimer(timer4, delay)

def display_lose_game():
    lose_game = turtle.Turtle()
    lose_game.speed(0)
    lose_game.color("white")
    lose_game.penup()
    lose_game.hideturtle()
    lose_game.goto(0,100)
    lose_game.write("You Lost", align ="center", font = ('Arial',32,'normal'))
    wn.update()

def water_meter_update():
    global water_score
    if water_score == 8:
        water_meter8.showturtle()
    else:
        water_meter8.hideturtle()
    if water_score >= 7:
        water_meter7.showturtle()
    else:
        water_meter7.hideturtle()
    if water_score >= 6:
        water_meter6.showturtle()
    else:
        water_meter6.hideturtle()
    if water_score >= 5:
        water_meter5.showturtle()
    else:
        water_meter5.hideturtle()
    if water_score >= 4:
        water_meter4.showturtle()
    else:
        water_meter4.hideturtle()
    if water_score >= 3:
        water_meter3.showturtle()
    else:
        water_meter3.hideturtle()
    if water_score >= 2:
        water_meter2.showturtle()
    else:
        water_meter2.hideturtle()
    if water_score >= 1:
        water_meter1.showturtle()
    else:
        water_meter1.hideturtle()

def go_left():
    global failed, paused
    if failed or paused:
        return
    x = player.xcor()
    x = x - 125
    player.setx(x)
    wn.update()

def go_right():
    global failed, paused
    if failed or paused:
        return
    x = player.xcor()
    x = x + 125
    player.setx(x)
    wn.update()

def watering():
    global e1, e2, e3, e4, water_score, failed, paused
    if failed or paused:
        return
    if water_score == 0:
        return
    x = player.xcor()
    if x == -250:
        if e1 >= 70:
            return
        if e1 <= 0:
            return
        e1 += 33
        water_score -= 1
        update_water_score()
    elif x == -125:
        if e2 >= 70:
            return
        if e2 <= 0:
            return
        e2 += 33
        water_score -= 1
        update_water_score()
    elif x == 0:
        if e3 >= 70:
            return
        if e3 <= 0:
            return
        e3 += 33
        water_score -= 1
        update_water_score()
    elif x == 125:
        if e4 >= 70:
            return
        if e4 <= 0:
            return
        e4 += 33
        water_score -= 1
        update_water_score()

def refill():
    global water_score, failed, paused
    if failed or paused:
        return
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
    water_meter_update()
    wn.update()

def check_failed():
    global failed
    if e1 < 0 and e2 < 0:
        failed = True
    elif e1 < 0 and e3 < 0:
        failed = True
    elif e1 < 0 and e4 < 0:
        failed = True
    elif e2 < 0 and e3 < 0:
        failed = True
    elif e2 < 0 and e4 < 0:
        failed = True
    elif e3 < 0 and e4 < 0:
        failed = True
    if failed:
        display_lose_game()

def game_over():
    global failed
    if failed:
        return

wn.listen()
wn.onkeypress(go_right, 'Right')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(watering, 'w')
wn.onkeypress(refill, 's')
wn.onkeypress(pause_game, 'p')

wn.update()

delay = 200

display_time_score.speed(0)
display_time_score.color("white")
display_time_score.penup()
display_time_score.hideturtle()
display_time_score.clear()
display_time_score.write("Score: {} sec".format (time_score), align = "left", font = ('Arial',24,'normal'))
wn.update()

def timer1():
    global e1, qe1, delay, paused
    e1 -= qe1
    check_failed()
    draw_plant(plant1, e1)
    if not failed and not paused:
        wn.ontimer(timer1, delay)

def timer2():
    global e2, qe2, delay, paused
    e2 -= qe2
    check_failed()
    draw_plant(plant2, e2)
    if not failed and not paused:
        wn.ontimer(timer2, delay)

def timer3():
    global e3, qe3, delay, paused
    e3 -= qe3
    check_failed()
    draw_plant(plant3, e3)
    if not failed and not paused:
        wn.ontimer(timer3, delay)

def timer4():
    global e4, qe4, delay, paused
    e4 -= qe4
    check_failed()
    draw_plant(plant4, e4)
    if not failed and not paused:
        wn.ontimer(timer4, delay)

wn.ontimer(timer1, delay)
wn.ontimer(timer2, delay)
wn.ontimer(timer3, delay)
wn.ontimer(timer4, delay)

def draw_plant(plant, e):
    shape = "flower1.gif"
    if e <= 0:
        shape = "flower4.gif"
        game_over()
    elif e <= 33:
        shape = "flower3.gif"
    elif e <= 66:
        shape = "flower2.gif"
    
    plant.speed(0)
    plant.shape(shape)
    plant.penup()
    wn.update()

score_timer()
wn.mainloop()
