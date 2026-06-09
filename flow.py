#Flow Control in Python 

#checking gretaer value using if statement
a = 10
b = 27
c = 15
if a > b and a > c:
    print("a is greater than b and c")
    
elif b > a and b > c:
    print("b is greater than a and  c")

else:
    print("c is greater than a and b")
    print()


#haha ////////////////////////////////////////////////////////////////////////////////////////////
isha_motivation = int(input("enter your motivation level to learn python (0-10):"))
if isha_motivation > 0:
    print("i am motivated to learn python")
else:
    print("playing games is more fun than learning python")    



#learning simple ////////////////////////////////////////////////////////////////////////////////
product_list = ['facewash','sunscreen','toner']
print(product_list)
print()

buy_product = input("enter the product you want: ")

if buy_product == "facewash":
    print("this is facewash ")
    quantity_product = int(input("enter the quantity of product : "))
    print(f"you have your {quantity_product} facewash product successfully")

elif buy_product == 'toner':
    print("this is toner ")
    quantity_product = int(input("enter the quantity of product : "))
    print(f"you have your {quantity_product} toner product successfully")

elif buy_product == 'sunscreen':
    print("this is sunscreen ")
    quantity_product = int(input("enter the quantity of product : "))
    print(f"you have your {quantity_product} sunscreen product successfully")

else:
    print("product not available")



# While loop /////////////////////////////////////////////////////////////////////////

i = 0
while i <= 10:
    print(i)
    i += 1     #this is incrementing the value of i by 1 in each iteration 
print("while loop is over")  


    

# for loop in list/////////////////////////////////////////////////////////////////////////

test_list = [1,2,3,4,5]
for i in test_list:
    print(i)

print()

# # foor loop in tuple //////////////////////////////////////////////////////////////////////////
test_tuple = ('isha', 'nisa', 'pisa')
for i in test_tuple:
    print(i)
print()

# #for loop in dictionary //////////////////////////////////////////////////////////////////////
test_dictionary = {'name': 'isha', 'age': 20}
for i in test_dictionary:  # test_dictionary.keys() will give key value
    print(i)               # test_dictionary.items() will give key and value 




# while loop  ////////////////////////////////////////////////////////////////////////////////////////
my_motivation = int(input(" enter the motivation level to make isha learn python (0-10): "))
print()
while my_motivation < 5:
    print(" i am not motivated to learn python ")
    print(" please enter higher num to motivated isha to learn python")
    print()

    my_motivation = int(input(" again enter the num to motivate isha : "))
    print()
    
print("-"*60)    
print(" now i am motivated to learn python yahuuu !!")
