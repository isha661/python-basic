# # creating a function 
# def print_5_times():
#     print("Today i am learning about function and how to call the function")
#     print()
# # call 
# print('Good morning everyone this is isha third day of learning python')
# print()
# print_5_times()


# #next example  
# def print_6_times():
#     isha = 0
#     while isha <= 6:
#         print("isha")
#         isha += 1

# # call 
# print('lets print the isha 6 times')
# print()
# print_6_times()

#example of function with loop 
def print_x_times(paramter, loop_amount):
    count = 0
    while count <= loop_amount:
     print(count, paramter)
     count += 1
#call
print('isha')
print_x_times('exam',2)    