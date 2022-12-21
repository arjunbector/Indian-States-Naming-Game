import turtle
import pandas
screen = turtle.Screen()
t = turtle.Turtle()
screen.screensize(canvheight=1209, canvwidth=1026)
screen.title("India States Game")
image = "map.gif"
screen.addshape(image)
t.shape(image)

map_data = pandas.read_csv("states.csv")
states_list = map_data.state.to_list()
guessed_states = []

while len(guessed_states) < 28:
    # user_input = screen.textinput(title=f"States {len(guessed_states)}/28",prompt="Name an another state.").title()
    user_input = states_list[len(guessed_states)]
    if user_input in states_list and user_input not in guessed_states:
        guessed_states.append(user_input) # Appending the user input to guessed_states.
        t = turtle.Turtle() # New turtle object to write the name of correct states.
        t.hideturtle() # Hiding the turtle.
        t.penup()
        state_data = map_data[map_data.state == user_input] # Accessing the state and its co-ordinations.
        xcor = int(state_data.x)
        ycor = int(state_data.y)
        t.goto(xcor,ycor) # Sends the turtle to the position where to send the turtle.
        t.write(user_input)

screen.exitonclick() 