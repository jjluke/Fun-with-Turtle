import turtle
import random
wn = turtle.Screen()
wn.bgcolor("black")
snappy = turtle.Turtle()
snappy.speed(100)
snappy.color("white")
snappy.pensize(10)
degree = 144
length = 200
while True:
  snappy.speed(10)
  snappy.forward(length)
  snappy.right(degree)
  snappy.forward(length)
  snappy.right(degree)
  snappy.forward(length)
  snappy.right(degree)
  snappy.forward(length)
  snappy.right(degree)
  snappy.forward(length)
  length =- 100
  degree =- 100
wn.exitonclick()
