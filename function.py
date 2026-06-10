# # creating a function 
def print_5_times():
    print("Today i am learning about function and how to call the function")
    print()
# call 
print('Good morning everyone this is isha third day of learning python')
print()
print_5_times()


# #next example ///////////////////////////////////////////////////////////////////////////////////////////////// 
def print_6_times():
    icount = 0
    while count <= 6:
        print("isha")
        count += 1

# call 
print('lets print the isha 6 times')
print()
print_6_times()


#example of function with loop ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
def print_y_times(paramter, loop_amount = 2):
    count = 0
    while count <= loop_amount:
     print(count, paramter)
     count += 1
     return loop_amount
print('isha')
print_y_times('exam')    # we can add loop amount here to ('exma', 2)



# specifiying and returning value ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#example of function with loop  and returing loop value count
def print_x_times(paramter, loop_amount = 5):
    count = 0
    print(global_var)
    while count <= loop_amount:
     print(count, paramter)
     count += 1
    return f'the loop amount is {loop_amount}'
print('isha')
global_var = 'global variable'
print(print_x_times('exam'))  # we can add loop amount here to ('exma', 2)
#global varaibale : this should be avaiable for every  function




#creaating function ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Excercise: creating a pythagoras theorem calculator once it run it should ask the user for 2 num that are hight and width of a traingle it should output the length of the hypotenuse.
def hypotenuse_calculator(side_a, side_b):
 hypotenuse = pow(side_a**2 + side_b**2, 0.5) #pow is a built in function which is used to calculate the power of a number
 return f"the hypotenuse of triangle is {round(hypotenuse, 2)}"

#calling 
print("See the answer")
print(hypotenuse_calculator(1,1))


#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Exercise: create a shouter fun that take 2 arguments , a string and a number
#the function should print the string mutiple times whatever is specified in the num arg. 
#capitalise every letter that is printed 
#if the num is greater than 10 dont print the input string instead print "you are too loud"
# function should return the string 'done' and have default value
def shouter_fun(str_1 = "chup", num_2 = 5):
    if num_2 <= 10:
      for i in range (num_2):
         print(str_1.upper())
    else:
        print("you are to loud")
    return "done"   

      

#call
print(shouter_fun('isha', 4))