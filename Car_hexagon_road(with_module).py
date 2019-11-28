#CAR TRACK, hexagon
import turtle
import car_module
import time
import math
wn=turtle.Screen()
wn.bgcolor('orange')
s=turtle.Shape("compound")
turtle.tracer(2)
t1=turtle.Turtle('turtle')
t1.setheading(0)
t1.shapesize(1)
t1.pensize(120)
t1.color('green')
t1.hideturtle()
t1.down
t1.goto(0,0)
L=200
N=6
for j in range (N):
    t1.fd(L)
    t1.right(360/N)
#t1.up()
t2=turtle.Turtle()
t2.setheading(0)
t2.shapesize(1)
t2.pensize(40)
t2.color('green')
t2.hideturtle()
#t2.up()

def road1(m):
     for j in range (L):
        car.fd(m*1)
        time.sleep(0.01)
     car.right(360/N)

#call function car_design() from module car_module
car_module.car_design()

car=turtle.Turtle(shape='car')
car.up()
car.tilt(90)
car.goto(0,0)
car.setheading(0)
b=car.heading()
#print(b)
#car.showturtle()
car.shapesize(1)

q=-1
while True:
    q=q+1
    q1=q%6
    #print('q1=',q1)
    if q1!=3:
        road1(1)
    if q1==3:
        car.setheading(0)
        road1(-1)
        car.rt(180)



