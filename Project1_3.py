import turtle

#Gets user input
number_of_sides = int(input("Enter the number of sides: "))
side_length = int(input("Enter the length of each side: "))

#Setup turtle
turtle.speed(7)       #I edited drawing speed to make it quicker

#Draw the polygon
angle = (360/number_of_sides)     #Finding the angle
for sides in range(number_of_sides):
    turtle.forward(side_length) #Uses the side_length input to move forward
    turtle.left(angle) #Turns left by the angle which I found earlier

'''Reflection
Why writing a for loop makes sense to use in each case.
    I am drawing a polygon which has a lot of repetition and its
    easier to use loop to avoid writing same lines lots of times

What is the iterator variable?
    The iterator is "sides" and it tracks the number of sides
    Goes from 0 to number_of_sides - 1
'''
