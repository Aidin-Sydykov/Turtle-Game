'''I didn't use the turtle module here since it seemed unnecessary.
It didn't ask me to draw anything'''

#Get a number from the user
number = int(input("Enter a number: "))

#Initialize sum
total = 0

#For loop to calculate sum
for i in range(1, number + 1):
    total += i

#Print the result
print(total)

'''reflection
Why writing a for loop makes sense to use in each case.
    Here a loop makes sense because I need to add each number from 1 to
    number, and I couldn't do that without a loop because I wouldn't know
    what the user would input

What is the iterator variable? 
    The iterator variable here is i because I was taught by my java teacher
    that i is the default iterator variable name. It represents the numbers
    from 1 to "number"
'''
