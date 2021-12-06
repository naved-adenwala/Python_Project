from turtle import *
state = {"turn":0}

def spinner():
    clear()
    # setting angle
    angle = state["turn"]/ 10
    left(angle)
    #forward
    forward(100)
    #creating dot and setting color
    dot(120,"orange")
    back(100)

    left(120)
    forward(100)
    dot(120,"blue")
    back(100)

    left(120)
    forward(100)
    dot(120,"red")
    back(100)
    left(120)
    width(20) #linewidth
    update()


def animate():
    if state["turn"] > 0:
        state["turn"] -=1

    spinner() #spinner structure
    ontimer(animate,20)#stop slowly


def flick():
    state["turn"] +=50 #speed of a spinner

onkey(flick,"space")
listen()

hideturtle() #hide turtle
tracer(False) #it will not trace
animate()
done() #it will run continuously

