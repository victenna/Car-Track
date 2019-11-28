import turtle
import car_module
import time
#import math

wn=turtle.Screen()
wn.setup(1400,900)
wn.bgcolor('lightgreen')
       
s=turtle.Shape("compound")
turtle.tracer(2)

t1=turtle.Turtle('turtle')
t1.setheading(0)
t1.shapesize(1)
t1.pensize(120)
t1.color('gray')
t1.hideturtle()
t1.down
t1.goto(-300,0)
for j in range (2):
    t1.fd(500)
    t1.right(90)
    t1.fd(200)
    t1.right(90)

t1.up()

#call function car_design() from module car_module
car_module.car_design()

car=turtle.Turtle(shape='car')
car.up()
car.tilt(90)
car.goto(-300,0)
car.setheading(0)
b=car.heading()
print(b)
car.showturtle()
car.shapesize(1)
car.shapesize(outline=3)

def road1():
    for j in range (500):
        car.fd(1)
        time.sleep(0.005)
    car.right(90)
    for j in range (200):
        car.fd(1)
        time.sleep(0.005)
    car.left(90)
    for j in range (500):
        car.fd(-1)
        time.sleep(0.005)
    car.lt(90)
    for j in range (200):
        car.fd(1)
        time.sleep(0.005)
    car.right(90)

while True:
    road1()
