import turtle
s = turtle.Shape("compound")

wn=turtle.Screen()
#wn.setup(900,900)
def car_design():
    #Car Roof
    roof=turtle.Turtle()
    roof.hideturtle()
    roof.penup()
    roof.goto(-20,30)
    roof.begin_poly()
    roof.fd(40)
    roof.right(90)
    roof.fd(20)
    roof.right(90)
    roof.fd(40)
    roof.end_poly()
    m1=roof.get_poly()
    s.addcomponent(m1,'navy')

    #Car Body
    body=turtle.Turtle()
    body.hideturtle()
    body.penup()
    body.goto(-50,10)
    
    body.begin_poly()
    body.fd(100)
    body.right(90)
    body.fd(15)
    body.right(90)
    body.fd(100)
    body.end_poly()
    m2=body.get_poly()
    s.addcomponent(m2,'navy')

    #Car first Wheel
    leg1=turtle.Turtle()
    leg1.hideturtle()
    leg1.penup()
    leg1.goto(-35,-10) 
    leg1.begin_poly()
    leg1.circle(10)
    leg1.end_poly()
    m3=leg1.get_poly()
    s.addcomponent(m3,'tan','black')

    #Car second Wheel
    leg2=turtle.Turtle()
    leg2.hideturtle()
    leg2.penup()
    leg2.goto(35,-10) 
    leg2.begin_poly()
    leg2.circle(10)
    leg2.end_poly()
    m4=leg2.get_poly()
    s.addcomponent(m4,'tan','black')
    wn.addshape('car',s)
    
    
