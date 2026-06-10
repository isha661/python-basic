# # FUNCTIONS

print('a value')
print(input("enter a value:"))
print()

# #Method

print('isha'.upper()) # upper method it change all lower case letter to upper case letter
print('ISHA'.lower()) # lower method it chnage all upper case letter to lower casse letter
print('isha'.replace('s','2')) # replace the character 's' with '2'
print()

# #other built in functions

print(abs(-5)) # this is absoulte function which make negative num positive 
print(max(10,20,30,40)) # this is max function this give out put which is maximum among the given numbers
print(min(10,40,35)) # this is min function this give out put which is minimium among the given numbers
print(len('isha')) # this is len function it count the number of characters in the string 
print()

#Excercise: creating a pythagoras theorem calculator once it run it should ask the user for 2 num that are hight and width of a traingle it should output the length of the hypotenuse.

side_a = int(input("Enter the width of the triangle: "))
side_b = int(input("Enter the height of the triangle: "))

hypotenuse = pow(side_a**2 + side_b**2, 0.5) #pow is a built in function which is used to calculate the power of a number
print("The hypotenuse of the triangle is: ",round(hypotenuse, 2)) # round is a built in function which is used to round the number to the specified number of decimal places, in this case it is 2 decimal places
