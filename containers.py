# This is about Tuple (), List[], Dictionary {}, Set {}
# Tuple : it is a collection of items which is ordered and unchnageable. 
# List: it is a collection of items which is ordered and chnagebale.
# Dictionary: it is a collection of items which is unordered and changebale and indexed.
# Set: it is a collection of items which is unordered and unchangebale and unindexed with uique elemnets.


a_tuple = (1,2,3,4,5)
a_list = [1,2,3,4,5,4]
a_list.append('isha') # this is append method which is used to add an element to the end of the list
a_set = {1,2,3,4,5,5,6,6}
a_dictionary = {'name':'isha', 'age':20, 'city':'dharan'}
a_dictionary['country'] = 'Nepal' # this is how we can add a new key 

print(a_tuple)
print(a_list)
print(set(a_list)) # this set function is used to convert a list to a set and it will remove dupilacte elements
print(a_set) # this will print only unique elements of the set
print(a_dictionary)



# Learning indexing and slicing 

user_list = ['isha','lisa','nisha','misha']
print(user_list[0:2:1]) # this is slicing 
print(user_list[1]) # this is indexing 

# Excercise: creating a list and new list : 8,6,4,2
n_list = [1,2,3,4,5,6,7,8,9,10]
print(n_list[7::-2])