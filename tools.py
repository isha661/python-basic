#  adding value into string with f strings
user_name = 'Isha Suchcha Rai'
user_age = 20
user_info = "This is isha she is 20 years old"
bad_approach = "This is "+user_name+ ". She is "+ str(user_age)+ " years old" # this is concat 
simple_approach = f"This is {user_age}. She is {user_age} years old" # this is f string 
print(simple_approach)



# # Single line if statement
user_name = str(input("Enter your name : "))
user_age = int(input("Enter the age of isha: "))
user_status = "Adult" if user_age>=18 else"minor" #this is single line

# if isha_age < 18:
#     isha_status = "minor"
# else:
#     isha_status = "adult"

print(f"{user_name} is {user_status}")      
print(f"{user_name} is {user_age} years old. The person is a {"adult" if user_age >=18 else "minor"}.")  





# List Comprehension
#this is long
simple_list = []
for i in range(1,11,1):
    simple_list.append(i)
print(simple_list)

#actual list comprehension
simple_list = [i for i in range(1,11,1)]
simple_list = [f'{j}{i}' for i in range(0,11,1) for j in ('a','d','c') if j == 'a']
print(simple_list)


# learning lambda functions

double_value = lambda num: num * 2
print(double_value(10))


#some function want a funcitons as an argument
random_list = [0,5,2,7,90]
sorted_list = sorted(random_list) # this function sort the list by lower to higher value
print(sorted_list)

# random_list = [('yashika', 25),('smriti',25),('isha',20)]
# sorted_list = sorted(random_list, key= lambda user_tuple: user_tuple[1])
# print(sorted_list)


#exercise: create a list comprehension for a battleship board
#[a1,a2.......e5] and remove c3
battle_ship = [f'{i}{j}' for i in ('A','B','C','D','E') for j in range(1,6,1) if f'{i}{j}' != 'C3']

print(battle_ship)