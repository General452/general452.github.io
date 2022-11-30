"""
  _______         _   _              _______         _   _      
 |__   __|       | | | |            |__   __|       | | | |     
    | |_   _ _ __| |_| | ___ _   _     | |_   _ _ __| |_| | ___ 
    | | | | | '__| __| |/ _ \ | | |    | | | | | '__| __| |/ _ \
    | | |_| | |  | |_| |  __/ |_| |    | | |_| | |  | |_| |  __/
    |_|\__,_|_|   \__|_|\___|\__, |    |_|\__,_|_|   \__|_|\___|
                              __/ |                             
                             |___/                              
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                            Version 1.2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

# import modules
import turtle
import time
import random

# initialize variables / lists
points = 0
pointSet1 = True
pointSet2 = True
highScore = 0
gamesList = []
gamesPlayed = 0
currentWindow = "game"
pointSum = 0

# setup window
win = turtle.Screen()
win.setup(400, 450)
win.tracer(0)

# import external textures
win.addshape("pearl.png")
win.addshape("Game_Over.png")
win.addshape("rock.png")
win.addshape("sub.png")
win.addshape("comingsoon.png")
win.addshape("lock.png")
win.addshape("gamebackground.png")
win.addshape("pole.png")
win.addshape("gameforeground.png")

# background
bg = turtle.Turtle()
bg.shape("gamebackground.png")
bg.hideturtle()
bg.left(90)
bg.stamp()

bg2 = turtle.Turtle()
bg2.shape("gamebackground.png")
bg2.hideturtle()
bg2.penup()
bg2.left(90)
bg2.goto(700, 0)
bg2.stamp()

# move background function
def bgMove():
    global s

    bg.clear()
    bg2.clear()

    x = bg.xcor()
    x2 = bg2.xcor()

    if x <= -700:
        bg.goto(660, 0)
    if x2 <= -700:
        bg2.goto(660, 0)

    x = bg.xcor()
    x2 = bg2.xcor()

    bg.setx(x - (s / 2))
    bg2.setx(x2 - (s / 2))

    bg.stamp()
    bg2.stamp()

# make the turtle
turt = turtle.Turtle()
turt.speed(0)
turt.shape("turtle")
turt.color("green")
turt.penup()
turt.goto(-150, 0)
turt.direction = "stop"

# poles
# pole1 center
pole1 = turtle.Turtle()
pole1.speed(0)
pole1.shape("pole.png")
pole1.hideturtle()
pole1.penup()
pole1.goto(250, 0)
pole1.left(90)
pole1.direction = "stop"
# pole2 center
pole2 = turtle.Turtle()
pole2.speed(0)
pole2.shape("pole.png")
pole2.hideturtle()
pole2.penup()
pole2.goto(450, 0)
pole2.left(90)
pole2.direction = "stop"

# foreground
fg = turtle.Turtle()
fg.shape("gameforeground.png")
fg.hideturtle()
fg.penup()
fg.left(90)
fg.stamp()

fg2 = turtle.Turtle()
fg2.shape("gameforeground.png")
fg2.hideturtle()
fg2.penup()
fg2.goto(660, 0)
fg2.left(90)
fg2.stamp()

def fgMove():
    global s

    fg.clear()
    fg2.clear()

    x = fg.xcor()
    x2 = fg2.xcor()

    if x <= -700:
        fg.goto(660, 0)
    if x2 <= -700:
        fg2.goto(660, 0)

    x = fg.xcor()
    x2 = fg2.xcor()

    fg.setx(x - (s * 1.2))
    fg2.setx(x2 - (s * 1.2))

    fg.stamp()
    fg2.stamp()

# current
current1 = turtle.Turtle()
current1.penup()
current1.goto(1150, 0)
current1.hideturtle()

currentOn = False
currentPos = [200, 400, 600, 800, 1000]
currentPosChoice = random.choice([currentPos])


def current():
    global gravInc
    global flapS
    global currentOn
    global s
    x = turt.xcor()
    x1 = current1.xcor()
    current1.setx(x1 - s)
    if x > (x1 - 60):
        if x < (x1 + 60):
            currentOn = True
    if x > (x1 + 60):
        currentOn = False
    if x < (x1 - 60):
        currentOn = False
    if currentOn == True:
        flapS = 15
        gravInc = 0.1
    if currentOn == False:
        flapS = 30
        gravInc = 0.06
    if x1 < -210:
        current1.goto(currentPosChoice, 0)


# game running?
running = True
start = False

# gravity stuff
grav = 1
gravInc = 0.06

# reset the game
def reset():
    time.sleep(0.1)
    global grav
    global points
    global s
    global pointSet1
    global pointSet2
    global flapS
    global currentWindow

    currentWindow = "game"
    s = 1
    flapS = 30
    current1.goto(1400, 0)
    turt.goto(-150, 0)
    turt.direction = "stop"
    pole1.goto(250, 0)
    pole1.direction = "stop"
    pole2.goto(450, 0)
    pole2.direction = "stop"
    pearl.goto(350, 0)
    bg.goto(0, 0)
    bg2.goto(700, 0)
    grav = 1
    points = 0
    pointSet1 = True
    pointSet2 = True
    win.bgpic("gamebackground.png")
    display.clear()
    lock.clear()
    turt.showturtle()
    pearl.showturtle()


# enact gravity on the turtle
def gravity():
    global grav
    global gravInc
    y = turt.ycor()
    turt.sety(y - grav)
    if grav <= 10:
        grav = grav + gravInc


# points system
def point():
    global pointSet1
    global pointSet2
    global points
    global difLevel
    x = turt.xcor()
    x1 = pole1.xcor()
    x2 = pole2.xcor()
    if x > (x1):
        if pointSet1 == True:
            pointSet1 = False
            points = points + 1
            difLevel = difLevel + 1
            score.clear()
    if x > (x2):
        if pointSet2 == True:
            pointSet2 = False
            points = points + 1
            difLevel = difLevel + 1
            score.clear()


display = turtle.Turtle()
display.hideturtle()
display.penup()
display.goto(0, 0)
display.color("white")
display.write(
    "press space or click to swim", font=("Source Code Pro", 14, "bold"), align="center"
)


# high score for the session
def highScoreFunction():
    global highScore
    if points > highScore:
        highScore = points


# when you loose the game
looseSeq = False


def loose():
    global start
    global looseSeq
    global highScore
    global points
    global gamesPlayed
    global numGames
    global currentWindow
    global pointSum

    currentWindow = "game over"

    start = False
    looseSeq = True
    turt.hideturtle()
    pearl.hideturtle()

    # for the game list
    gamesList.append(points)
    gamesPlayed += 1

    if gamesPlayed >= 15:
        numGames += 1

    highScoreFunction()
    pointSum += points

    display.goto(0, -150)
    display.color("white")
    display.write(highScore, font=("Source Code Pro", 14, "bold"), align="center")

    display.goto(0, -175)
    display.color("white")
    display.write(
        "session high score", font=("Source Code Pro", 12, "bold"), align="center"
    )

    pole1.clear()
    pole2.clear()
    bg.clear()
    bg2.clear()
    fg.clear()
    fg2.clear()

    win.update()

    win.bgpic("Game_Over.png")

    time.sleep(1)
    looseSeq = False


score = turtle.Turtle()
score.hideturtle()
score.penup()
score.color("white")
score.goto(0, 175)


def scoreDisplay():
    # display points
    score.clear()
    score.write(
        "points - " + str(points), font=("Source Code Pro", 14, "bold"), align="center"
    )


poleGap = 75
poleGap = poleGap / 2

# define pearls
pearl = turtle.Turtle()
pearl.shape("pearl.png")
pearl.penup()
pearl.setx(350)

pearlPosList = [300, 500, 700]

# all things to do with pearls
def pearlMove():
    global s
    x = pearl.xcor()
    pearl.setx(x - s)

    # recycles pearl
    if x < -210:
        pearl.goto(
            pole1.xcor() + random.choice(pearlPosList), random.randint(-150, 150)
        )

    # collision
    global points
    turtX = turt.xcor()
    turtY = turt.ycor()
    y = pearl.ycor()
    cooldown = 0

    if (x - 10) < turtX < (x + 10) and (y + 10) > turtY > (y - 10):
        if not (cooldown):
            points += 1
            pearl.goto(
                pole1.xcor() + random.choice(pearlPosList), random.randint(-150, 150)
            )


s = 1
# moves poles
def pole():
    global start
    global s
    global pointSet1
    global pointSet2

    pole1.clear()
    pole2.clear()

    x = pole1.xcor()
    pole1.setx(x - s)
    x2 = pole2.xcor()
    pole2.setx(x2 - s)

    pole1.stamp()
    pole2.stamp()

    # recycles poles
    if x < -210:
        pole1.goto(200, random.randint(-150, 150))
        pointSet1 = True
    if x2 < -210:
        pole2.goto(200, random.randint(-150, 150))
        pointSet2 = True


# flap to make turtle go up
flapS = 30

# previous games window
numGames = 0


def previousGames():
    global gamesList
    global gamesPlayed
    global numGames

    display.clear()
    score.clear()
    win.bgcolor("black")
    win.update()
    display.penup()
    display.color("white")

    display.goto(0, -175)
    display.write(
        "<press space or click anywhere to continue>",
        font=("Source Code Pro", 10),
        align="center",
    )

    while len(gamesList) > 15:
        gamesList.pop(0)

    reps = 1

    for i in gamesList:

        display.goto(0, 175 - (reps * 20))
        display.write(
            "Game " + str(reps + numGames) + ": " + str(i),
            font=("Source Code Pro", 14, "bold"),
            align="center",
        )

        reps += 1


# customize settings

# lock for locked player skins
lock = turtle.Turtle()
lock.penup()
lock.left(90)
lock.hideturtle()
lock.shape("lock.png")


def customize():
    global currentWindow
    global pointSum

    currentWindow = "shop"

    display.clear()
    score.clear()
    win.update()
    win.bgpic("shop_bg.png")

    if pointSum < 10:
        lock.goto(0, -85)
        lock.stamp()

    if pointSum < 30:
        lock.goto(130, -85)
        lock.stamp()

    inShop = True

    # shop / customization while loop
    while inShop:
        win.update()


def options():
    global currentWindow

    currentWindow = "options"

    display.clear()
    score.clear()
    win.update()
    win.bgpic("comingsoon.png")


def flap():
    global grav
    global start
    if start == False:
        if looseSeq == False:
            reset()
            start = True
    else:
        y = turt.ycor()
        grav = 0
        turt.sety(y + flapS)


def flapClick(x, y):
    global grav
    global start
    global window

    if currentWindow == "game":
        y = turt.ycor()
        grav = 0
        turt.sety(y + flapS)
    elif currentWindow == "game over":
        # buttons for loose screen
        if (x > -78) and (y > -19) and (x < 79) and (y < 1):
            previousGames()  # see previous games

        elif (x > -72) and (y > -48) and (x < 74) and (y < -30):
            customize()  # customize turtle, bakcground, and more

        elif (x > -43) and (y > -83) and (x < 44) and (y < -56):
            options()
        elif (x > -29) and (y > -144) and (x < 28) and (y < -97):
            win.bye()
        else:
            if looseSeq == False:
                reset()
                start = True
    elif currentWindow == "shop":
        if (x > -189) and (y > -145) and (x < -70) and (y < -26):
            turt.shape("turtle")

        elif (x > -59) and (y > -146) and (x < 61) and (y < -26):
            if pointSum >= 10:
                turt.shape("rock.png")

        elif (x > 71) and (y > -144) and (x < 190) and (y < -26):
            if pointSum >= 30:
                turt.shape("sub.png")

        else:
            reset()
            lock.clear()
            start = True

    else:
        print("error")


# bounding box for first pole
def pole1Bound():
    x = pole1.xcor()
    y = pole1.ycor()
    x1 = turt.xcor()
    y1 = turt.ycor()
    if (y1 + 9) > (y + poleGap):
        if (x1 + 9) > (x - 15):
            if (x1 - 9) < (x + 15):
                loose()
    if (y1 - 9) < (y - poleGap):
        if (x1 + 9) > (x - 15):
            if (x1 - 9) < (x + 15):
                loose()


# bounding box for second pole
def pole2Bound():
    x = pole2.xcor()
    y = pole2.ycor()
    x1 = turt.xcor()
    y1 = turt.ycor()
    if (y1) > (y + 25):
        if (x1) > (x - 15):
            if (x1) < (x + 15):
                loose()
    if (y1) < (y - 25):
        if (x1) > (x - 15):
            if (x1) < (x + 15):
                loose()


# floor
def floorCheck():
    y = turt.ycor()
    if y < -190:
        loose()
    if y > 230:
        loose()


difLevel = 0
# increase difficulty level
def dif():
    global s
    global points
    global difLevel
    if difLevel >= 5:
        s = s + 0.1
        difLevel = 0


# keybinds

flapKey = "space"

win.listen()
win.onkey(flap, flapKey)
win.onscreenclick(flapClick)

# game loop
while running:
    if start == True:
        gravity()  # start by enacting gravity

        current()  # write in current patches

        bgMove()  # move the background

        pole()  # move the poles

        pearlMove()  # move the pearls

        fgMove()  # move the foreground

        pole1Bound()  # check the boundries of pole 1

        pole2Bound()  # check the boundries of pole 2

        floorCheck()  # check if player has hit floor, or reached height limit

        point()  # calculate points

        scoreDisplay()  # write the score

        dif()  # check if difficulty should be increased

    win.update()  # update the window
