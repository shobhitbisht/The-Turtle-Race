from turtle import Turtle, Screen
import random

is_race_on = False
start = Turtle(shape="circle")
screen = Screen()
screen.title("Welcome To Turtle Race")
screen.bgcolor("Black")
screen.bgpic("t.gif")
screen.setup(500, 400)

start.penup()
start.color("black")
start.pensize(5)
start.goto(-230, -120)
start.left(90)
start.pendown()
start.forward(240)

y_pos = [100, 50, 0, -50, -100]
colors = ["purple", "pink", "green", "blue", "red"]
all_turtle = []
for tur_ind in range(5):

  tim = Turtle(shape="turtle")
  tim.penup()
  tim.color(colors[tur_ind])
  tim.goto(-250, y_pos[tur_ind])
  all_turtle.append(tim)

user_bet = screen.textinput(
  title="Make your bet",
  prompt="Which tutle will win the race? Enter a color: ")

if user_bet:
  is_race_on = True

while is_race_on:

  for turtle in all_turtle:
    if turtle.xcor() > 230:

      wincolor = turtle.pencolor()

      if user_bet == wincolor:

        print(f"{wincolor} turtle is winner, Huraah!!")
        print("You win, Game over")
      else:
        print(f"{wincolor} turtle is winner, shittt!!")
        print("You lose, Game Over")
      print("Thanks for Playing The Turtle Race created By Shobhit Aka TKD")
      is_race_on = False
      break
    rand_dist = random.randint(0, 10)
    turtle.forward(rand_dist)
