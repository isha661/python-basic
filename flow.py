# #Flow Control in Python 

# #checking gretaer value using if statement
# a = 10
# b = 27
# c = 15
# if a > b and a > c:
#     print("a is greater than b and c")
    
# elif b > a and b > c:
#     print("b is greater than a and  c")

# else:
#     print("c is greater than a and b")
#     print()


# #haha ////////////////////////////////////////////////////////////////////////////////////////////
# isha_motivation = int(input("enter your motivation level to learn python (0-10):"))
# if isha_motivation > 0:
#     print("i am motivated to learn python")
# else:
#     print("playing games is more fun than learning python")    



# #learning simple ////////////////////////////////////////////////////////////////////////////////
# product_list = ['facewash','sunscreen','toner']
# print(product_list)
# print()

# buy_product = input("enter the product you want: ")

# if buy_product == "facewash":
#     print("this is facewash ")
#     quantity_product = int(input("enter the quantity of product : "))
#     print(f"you have your {quantity_product} facewash product successfully")

# elif buy_product == 'toner':
#     print("this is toner ")
#     quantity_product = int(input("enter the quantity of product : "))
#     print(f"you have your {quantity_product} toner product successfully")

# elif buy_product == 'sunscreen':
#     print("this is sunscreen ")
#     quantity_product = int(input("enter the quantity of product : "))
#     print(f"you have your {quantity_product} sunscreen product successfully")

# else:
#     print("product not available")


# #loops
# # While loop /////////////////////////////////////////////////////////////////////////

# i = 0
# while i <= 10:
#     print(i)
#     i += 1     #this is incrementing the value of i by 1 in each iteration 
# print("while loop is over")  


    

# # for loop in list/////////////////////////////////////////////////////////////////////////

# test_list = [1,2,3,4,5]
# for i in test_list:
#     print(i)

# print()

# # # foor loop in tuple //////////////////////////////////////////////////////////////////////////
# test_tuple = ('isha', 'nisa', 'pisa')
# for i in test_tuple:
#     print(i)
# print()

# # #for loop in dictionary //////////////////////////////////////////////////////////////////////
# test_dictionary = {'name': 'isha', 'age': 20}
# for i in test_dictionary:  # test_dictionary.keys() will give key value
#     print(i)               # test_dictionary.items() will give key and value 




# # while loop  ////////////////////////////////////////////////////////////////////////////////////////
# my_motivation = int(input(" enter the motivation level to make isha learn python (0-10): "))
# print()
# while my_motivation < 5:
#     print(" i am not motivated to learn python ")
#     print(" please enter higher num to motivated isha to learn python")
#     print()

#     my_motivation = int(input(" again enter the num to motivate isha : "))
#     print()
    
# print("-"*60)    
# print(" now i am motivated to learn python yahuuu !!")


# # truthy and falsy: Automatic conversion to boolean. empty container, string without letter and 0 are false everything else is truthy 
# if 1:
#     print('something')
# else:
#     print('falsy')    


#Exercise: Create a list 1-5 and run code for every item if the value is 2 print "the value is 2"
# if it isn't print the value is not 2
# if the value is 5 run a while loop to print 'last item' 6 times

i_list = [1,2,3,4,5]
i_counter = 0
for i in i_list:
    if i == 2:
        print("the value is 2")
    else:
        print("the value is not 2")    
while i_counter <= 6:
    print('last item')
    i_counter += 1