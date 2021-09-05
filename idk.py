import turtle
import time
import keyboard
import winsound

wn = turtle.Screen()
wn.title("idk just play fam")
wn.bgpic('BG.gif')
wn.setup(width=801, height=600)
wn.tracer(0)
vel1 = 5.5
vel2 = -5.5

# scoring
score_a = 0
score_b = 0
play_a_htl = 100
play_b_htl = 100
game_over = False
game_state = 0
win_state = 0

# player a
play_a = turtle.Turtle()
turtle.register_shape('LC.gif')
play_a.speed(0)
play_a.shape("LC.gif")
play_a.penup()
play_a.goto(-350, 0)

# player b
play_b = turtle.Turtle()
turtle.register_shape('RC.gif')
play_b.speed(0)
play_b.shape("RC.gif")
play_b.penup()
play_b.goto(350, 0)

# bullet a
bulleta = turtle.Turtle()
bulleta.shape("square")
bulleta.shapesize(0.14, 0.7)
bulleta.color("grey")
bulleta.up()
bulleta.goto(play_a.xcor(), play_a.ycor())
bulleta.state = 'ready'

# bullet b
bulletb = turtle.Turtle()
bulletb.shape("square")
bulletb.shapesize(0.14, 0.7)
bulletb.color("grey")
bulletb.up()
bulletb.goto(play_b.xcor(), play_b.ycor())
bulletb.state = 'ready'

# marker
pen = turtle.Turtle()
pen.speed(0)
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: {} Health: {}             Score: {} Health: {}".format(
    score_a, play_a_htl, score_b, play_b_htl), align="center", font=("Comic Sans MS", 18, "normal"))

# functions

def play_a_up():
    y = play_a.ycor()
    if play_a.ycor()<120:
        y += 20
    play_a.sety(y)
    if bulleta.xcor() < -345:
        bulleta.sety(y)

def play_a_down():
    y = play_a.ycor()
    if play_a.ycor()>-250:
        y -= 20
    play_a.sety(y)
    if bulleta.xcor() < -345:
        bulleta.sety(y)

def play_b_up():
    y = play_b.ycor()
    if play_b.ycor()<120:
        y += 20
    play_b.sety(y)
    if bulletb.xcor() > 345:
        bulletb.sety(y)

def play_b_down():
    y = play_b.ycor()
    if play_b.ycor()>-250:
        y -= 20
    play_b.sety(y)
    if bulletb.xcor() > 345:
        bulletb.sety(y)

def shoota():
    bulleta.state = 'fire'
    winsound.PlaySound("SHOT.wav", winsound.SND_ASYNC)

def shootb():
    bulletb.state = 'fire'
    winsound.PlaySound("SHOTB.wav", winsound.SND_ASYNC)

def bulleta_shoota():
    bulleta.fd(vel1)
    if bulleta.xcor() > 400:
        bulleta.goto(play_a.xcor(), play_a.ycor())
        bulleta.state = 'ready'

def bulleta_shootb():
    bulletb.fd(vel2)
    if bulletb.xcor() < -400:
        bulletb.goto(play_b.xcor(), play_b.ycor())
        bulletb.state = 'ready'

def playagain():
    global game_state
    global play_a_htl
    global play_b_htl
    global score_a
    global score_b
    bulleta.goto(-350, 0)
    play_a.goto(-350, 0)
    bulletb.goto(350, 0)
    play_b.goto(350, 0)
    bulleta.state = 'ready' 
    bulletb.state = 'ready'
    play_a_htl = 100
    play_b_htl = 100
    score_a = 0
    score_b = 0
    pen.clear()
    pen.write("Score: {} Health: {}             Score: {} Health: {}".format(score_a, play_a_htl, score_b, play_b_htl), align="center", font=("Comic Sans MS", 18, "normal"))
    game_state = 0

def quit():
    global game_state
    game_state = 2

def restart():
    opt = 1
    pen.clear
    wnscr = turtle.Turtle()
    wnscr.speed(0)
    wnscr.color("black")
    wnscr.penup()
    wnscr.hideturtle()
    wnscr.goto(0, 0)
    wnscr.clear()
    wnscr.write(("Player {} Wins".format(win_state)), align="center", font=("Comic Sans MS", 20, "normal"))
    pen2 = turtle.Turtle()
    pen2.speed(0)
    pen2.color("white")
    pen2.penup()
    pen2.hideturtle()
    pen2.goto(0, 60)
    pen2.clear()
    pen2.write(("U - Play Again            I - Quit"), align="center", font=("Comic Sans MS", 18, "normal"))
    while opt != 0:
        if keyboard.is_pressed('u'):
            playagain()
            opt = 0
        elif keyboard.is_pressed('i'):
            quit()
            opt = 0
    pen2.clear()
    wnscr.clear()

def increment():
    global vel1, vel2
    vel1 += 1
    vel2 -= 1

def lower():
    global vel1, vel2
    vel1 -= 1
    vel2 += 1

# keyboard

wn.listen()
wn.onkeypress(play_a_up, "w")
wn.onkeypress(play_a_down, "s")
wn.onkeypress(play_b_up, "Up")
wn.onkeypress(play_b_down, "Down")
wn.onkey(shoota, "d")
wn.onkey(shootb, "Left")
wn.onkey(increment, "6")
wn.onkey(lower, "7")

# main game loop

while not game_over:
    wn.update()
    time.sleep(0.002)

    if game_state == 0:
        if bulleta.state == 'fire':
            bulleta_shoota()
        if bulletb.state == 'fire':
            bulleta_shootb()

     # collisions
        if (bulleta.xcor() > 340 and bulleta.xcor() < 350) and (bulleta.ycor() < play_b.ycor() + 25 and bulleta.ycor() > play_b.ycor() - 25):
            
            bulleta.goto(play_a.xcor(), play_a.ycor())
            bulleta.state = "ready"
            pen.clear()
            score_a += 15
            play_b_htl -= 10
            pen.write("Score: {} Health: {}             Score: {} Health: {}".format(
            score_a, play_a_htl, score_b, play_b_htl), align="center", font=("Comic Sans MS", 18, "normal"))
        if play_b_htl <= 0:
            game_state = 1
            win_state = 1

        if (bulletb.xcor() < -340 and bulletb.xcor() > -350) and (bulletb.ycor() < play_a.ycor() + 25 and bulletb.ycor() > play_a.ycor() - 25):
            
            bulletb.goto(play_b.xcor(), play_b.ycor())
            bulletb.state = "ready"
            pen.clear()
            score_b += 15
            play_a_htl -= 10
            pen.write("Score: {} Health: {}             Score: {} Health: {}".format(
                score_a, play_a_htl, score_b, play_b_htl), align="center", font=("Comic Sans MS", 18, "normal"))

            if play_a_htl <= 0:
                game_state = 1
                win_state = 2

    elif game_state == 1:
        restart()

    elif game_state == 2:
        game_over = True