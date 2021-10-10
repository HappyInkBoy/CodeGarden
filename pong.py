#export TK_SILENCE_DEPRECATION=1
import turtle as t
playerAscore=0
playerBscore=0

window=t.Screen()
window.title("THE PONG GAME!")
window.bgcolor("white")
window.setup(width=800, height=600)
window.tracer(0)

leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("black")
leftpaddle.shapesize(stretch_wid = 5, stretch_len = 1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("black")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(+350,0)

ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=1.8
ballydirection=1.8

pen=t.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score",align="center",font=('Arial',24,'normal'))

def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+45
    leftpaddle.sety(y)

def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-45
    leftpaddle.sety(y)

def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+45
    rightpaddle.sety(y)

def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-45
    rightpaddle.sety(y)

window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')

while True:
    window.update()
    print ("ballx {} y {}, leftpaddlex {} y {}".format( ball.xcor(), ball.ycor(), leftpaddle.xcor(), leftpaddle.ycor()))

    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)

    if ball.ycor()>290:
        ball.sety(290)
        ballydirection=ballydirection*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        ballydirection=ballydirection*-1
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection=ballxdirection*-1
        playerAscore=playerAscore+1
        pen.clear()
        pen.write("Player A: {}        Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',24,"normal"))
    
    #if(ball.xcor()>330) and (ball.xcor()<340) and (ball.ycor()<rightpaddle.ycor()+40 and ball.ycor()>rightpaddle.ycor()-40):
    if(ball.xcor()>330) and (ball.xcor()<=340) and (ball.ycor()<rightpaddle.ycor()+40 and ball.ycor()>rightpaddle.ycor()-40):
        ball.setx(330)
        ballxdirection=ballxdirection*-1
    
    if (ball.xcor()>-350) and (ball.xcor()<-340):
        print("collision x !!!!")
    if (ball.ycor()<leftpaddle.ycor()+40 and ball.ycor()>leftpaddle.ycor()-40):
        print ("collision y!!!")


    #if(ball.xcor()>-330) and (ball.xcor()<-340) and (ball.ycor()<leftpaddle.ycor()+40 and ball.ycor()>leftpaddle.ycor()-40):
    if(ball.xcor()>-350) and (ball.xcor()<=-330) and (ball.ycor()<leftpaddle.ycor()+40 and ball.ycor()>leftpaddle.ycor()-40):
        ball.setx(-330)
        ballxdirection=ballxdirection*-1
        print ('left collision')
