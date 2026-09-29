import turtle

turtle.speed(0)     #fastest drawing

#Outer loop, it has 4 sides of the shape
for sides in range(4):
    #inner loop, it has 3 "steps" per side
    for steps in range(3):
        turtle.right(90)     #turns down
        turtle.forward(30)   #steps
        turtle.left(90)      #turns forward again
        turtle.forward(30)   #moves across
    #at the end of the side, turn the corner to redo everything again
    turtle.left(90) #turns left
    turtle.forward(30)  #moves forward and positions the turtle to draw the steps again

'''Reflection    
Why writing a for loop makes sense to use in each case.
    Using a loop here makes sense since the pattern repeats multiple times
    and instead of writing it over and over you can loop to make it more efficient.
    Nested loops makes sense since the inner loop does the steps in the shape
    and the outer loop makes it do multiple times to make it that shape. Hard to explain

What is the iterator variable? 
    The "sides" counts the 4 sides of the shape
    the "steps" counts the steps for each side
'''
