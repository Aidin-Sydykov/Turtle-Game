import turtle

turtle.speed(0)       #fastest drawing speed
turtle.width(12)      #thick pen width like in the photo

#Draw each circle manually (no loop I was told it wasn't necessary)
turtle.teleport(-280, 0)
turtle.color("blue")
turtle.circle(120)

turtle.teleport(0, 0)
turtle.color("black")
turtle.circle(120)

turtle.teleport(280, 0)
turtle.color("red")
turtle.circle(120)

turtle.teleport(-140, -120)
turtle.color("yellow")
turtle.circle(120)

turtle.teleport(140, -120)
turtle.color("green")
turtle.circle(120)


'''reflection
For this program, you clarified that I don't have to use for loops
since we haven't learned lists yet, and there isn't too much rings.
Writing them this was keeps the code simple and clear.
Once I learn lists it would be useful to use for loops to not write
as much repetative code.
No loops so theres no iterator variable in here.
'''
