#  adding value into string with f strings
# user_name = 'Isha Suchcha Rai'
# user_age = 20
# user_info = "This is isha she is 20 years old"
# bad_approach = "This is "+user_name+ ". She is "+ str(user_age)+ " years old" # this is concat 
# simple_approach = f"This is {user_age}. She is {user_age} years old" # this is f string 
# print(simple_approach)



# Single line if statement
user_name = str(input("Enter your name : "))
user_age = int(input("Enter the age of isha: "))
# user_status = "Adult" if user_age>=18 else"minor" #this is single line

# # if isha_age < 18:
# #     isha_status = "minor"
# # else:
# #     isha_status = "adult"

# print(f"{user_name} is {user_status}")      
print(f"{user_name} is {user_age} years old. The person is a {"adult" if user_age >=18 else "minor"}.")  