#Ask the user for a number
number = int(input("Enter a number: "))

#Initialize the factorial
factorial = 1

#For loop to calculate the factorial
for i in range(1, number + 1):
    factorial *= i

#Print out the result
print(factorial)

'''Reflectino
Why writing a for loop makes sense to use in each case. 
    Again, like the last question using a loop makes sense here because
    you don't know the user input and it counts from 1 to number without
    you having to write too much code. Makes it much more efficient and
    cleaner

What is the iterator variable? 
    The iterator variable in here is i and it shows the numbers from 1 to
    number
'''
