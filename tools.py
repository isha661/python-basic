#  adding value into string with f strings
user_name = 'Isha Suchcha Rai'
user_age = 20
user_info = "This is isha she is 20 years old"
bad_approach = "This is "+user_name+ ". She is "+ str(user_age)+ " years old" # this is concat 
simple_approach = f"This is {user_age}. She is {user_age} years old" # this is f string 
print(simple_approach)