import turtle
import car_module
import time
wn=turtle.Screen()
wn.bgcolor('pink')
s=turtle.Shape("compound")
turtle.tracer(2)
t1=turtle.Turtle()
t1.setheading(0)
t1.shapesize(1)
t1.pensize(100)
t1.color('green')
t1.hideturtle()
t1.up()
R=100
t2=turtle.Turtle()
t2.setheading(0)
t2.shapesize(1)
t2.pensize(100)
t2.color('green')
t2.hideturtle()
t2.up()

def road1():
    t1.setheading(0)
    t1.circle(R)
t1.down()
road1()

def road2():
    t1.setheading(0)
    t1.circle(-R)
t2.down()
road2()

#call function car_design() from module car_module
car_module.car_design()

car=turtle.Turtle(shape='car')
car.up()
car.tilt(90)
car.goto(0,-2*R)
car.showturtle()
#a.circle(R)
car.shapesize(1)

#----------------------
def cars(q,angle):
    
    for i in range (angle):
        car.fd(1.7)
        car.left(q)
        time.sleep(0.008)
        
for j in range(50):
        cars(1,180)
        cars(-1,360)
        cars(1,180)


