# Classes are a way to organize code
# Basic class

# class TestClass:
#     test_var = "hello"
#     next_var = [1,2,3,4,]

# # creating an instance by calling it
# test = TestClass() #test is instance 
# test.next_var = "only for this instance"  #creates an instance attribute that overrides the class attribute for that particular object.

# #another instance
# test2 = TestClass()
# print(test2.next_var)





#creating def function in class  /////////////////////////////////////////////////////////////////////// 
class IshaClass:
    my_name = 'Isha'
    my_age = 20

    def isha_fun(self): # self refers to any instance of the class and must be the first parameter for all methods
        print("isha function is called in class now")
        print(self.my_name)
        self.another_fun("here in isha funcction we call another fun")
    

    #calling function
    # print("lets call isha function in class")
    # isha_fun()

    def another_fun(self, para):
        print(para)

#creating an instance
my = IshaClass()
print(my.my_name)
print(my.my_age)    
my.isha_fun()
my.another_fun("This is another new function") #this is for another function


