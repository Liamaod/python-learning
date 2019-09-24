# Simple Pong Game for Beginners
# Youtube: https://www.youtube.com/watch?v=C6jJg9Zan7w
# Part of Stellarios by ACORD - http://acord.tech/stellarios

import turtle # module that lets you do basic graphics in Python

wn = turtle.Screen() # creates a variable called "wn" that is the game windows
wn.title("Pong by ACORD") # sets the title that would appear on the window
wn.bgcolor("black") # sets the game window bg color
wn.setup(width=800, height=600) # sets the game window size
wn.tracer(0) # stops the window from updating

# Paddle A
paddle_a = turtle.Turtle() # creates a game object. "turtle" = module, Turtle = class
paddle_a.speed(0) # Speed of animation - maximum possible speed
paddle_a.shape("square") # default - 20px*20px
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) # Stretches the width and length of "paddle_a"
paddle_a.penup()
paddle_a.goto(-350, 0) # Sets the initial coordinates for the Paddle_A


# Paddle B
paddle_b = turtle.Turtle() # creates a game object. "turtle" = module, Turtle = class
paddle_b.speed(0) # Speed of animation - maximum possible speed
paddle_b.shape("square") # default - 20px*20px
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) # Stretches the width and length of "paddle_a"
paddle_b.penup()
paddle_b.goto(350, 0) # Sets the initial coordinates for the Paddle_A

# Ball
ball = turtle.Turtle() # creates a game object. "turtle" = module, Turtle = class
ball.speed(0) # Speed of animation - maximum possible speed
ball.shape("square") # default - 20px*20px
ball.color("white")
ball.penup()
ball.goto(0, 0) # Sets the initial coordinates for the Paddle_A

# Functions
def paddle_a_up(): # Defining the function
    y = paddle_a.ycor() # sets the y value to the current y-coord value of the object "paddle_a"
    y += 20
    paddle_a.sety(y)

def paddle_a_down(): # Defining the function
    y = paddle_a.ycor() # sets the y value to the current y-coord value of the object "paddle_a"
    y -= 20
    paddle_a.sety(y)    

def paddle_b_up(): # Defining the function
    y = paddle_a.ycor() # sets the y value to the current y-coord value of the object "paddle_a"
    y += 20
    paddle_a.sety(y)

def paddle_b_down(): # Defining the function
    y = paddle_a.ycor() # sets the y value to the current y-coord value of the object "paddle_a"
    y -= 20
    paddle_a.sety(y)        

# Keyboard Binding
wn.listen() # listen for keyboard input
wn.onkeypress(paddle_a_up, "w")

wn.listen() # listen for keyboard input
wn.onkeypress(paddle_a_down, "s")

wn.listen() # listen for keyboard input
wn.onkeypress(paddle_b_up, "Up") # up arrow key

wn.listen() # listen for keyboard input
wn.onkeypress(paddle_b_down, "Down") # down arrow key


# Main Game Loop
while True:
    wn.update() # every time the loop runs, it updates the screen