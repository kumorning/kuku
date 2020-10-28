import turtle

turtle.screensize(320, 320)
turtle.colormode(255)
turtle.bgcolor(250, 100, 0) 
turtle.speed(50)
turtle.pensize(5)
sides=24

for i in range(80):
  turtle.circle(3*i)
  turtle.circle(-4*i)
  
  b=i
  if b > 51:
    b = 51
 
  turtle.color(255, 255,255) 
  turtle.circle(5*i)
  turtle.circle(-6*b)
  turtle.left(180)
  turtle.color(i, i, 5*b)
  turtle.home
  turtle.right(60)

  turtle.left(180)
