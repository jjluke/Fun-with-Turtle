import turtle
import random
wn = turtle.Screen()
wn.bgcolor("black")
snappy = turtle.Turtle()
snappy.speed(100)
snappy.color("white")
snappy.pensize(5)
degree = 144
length = 200
snappy.speed(5)
while True:
  snappy.forward(length)
  snappy.color("red")
  snappy.right(degree)
  snappy.forward(length)
  snappy.color("yellow")
  snappy.right(degree)
  snappy.forward(length)
  snappy.color("green")
  snappy.right(degree)
  snappy.forward(length)
  snappy.color("pink")
  snappy.right(degree)
  snappy.forward(length)
  snappy.color("white")
  wn.exitonclick()
