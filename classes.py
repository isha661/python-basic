# Classes are a way to organize code
# Basic class

class TestClass:
    test_var = "hello"
    next_var = [1,2,3,4,]

# creating an instance by calling it
test = TestClass() #test is instance 
test.next_var = "only for this instance"  #creates an instance attribute that overrides the class attribute for that particular object.

#another instance
test2 = TestClass()
print(test2.next_var)





#creating def function in class  /////////////////////////////////////////////////////////////////////// 
# varaibales in class is attribute
#functions in a class are methods

class IshaClass:
    my_name = 'Isha'
    my_age = 20

    def isha_fun(self): # self refers to any instance of the class and must be the first parameter for all methods
        print("isha function is called in class now")
        print(self.my_name)
        self.another_fun("here in isha funcction we call another fun")
    

    def another_fun(self, para):
        print(para)

#creating an instance
my = IshaClass()
print(my.my_name)
print(my.my_age)    
my.isha_fun()
my.another_fun("This is another new function") #this is for another function



#Dunder (double underscore) method are special methods of a class
# __int __is run when an instance of the class is created
# __len__ gets called when the instance is passed into the len function 

#Mage class
# class Mage:
#     def __init__(self, health, mana):
#         self.health = health
#         self.mana = mana
#         print("the mage class was created")
#         print(self.health)
#     def __len__(self):
#         return self.mana    
       

# mage = Mage(100, 200)
# print(len(mage))



class Mage:
    def __init__(self, health, mana):
        self.health = health
        self.mana = mana
        print("the mage class was created")
        print(self.health)
    def attack(self, target):
        target.health -= 10

class Monster:
    health = 40
       

mage = Mage(100, 200)
monster = Monster()

print(monster.health)
mage.attack(monster)
print(monster.health)



#///////////////////////////////////////////////////////////////////
#Inheritance (one class can get the method and attributes of another class)
class Human:
     
     def __init__(self, health):
          self.health = health
          
     def attack(self):
          print("attack")


class Warrior(Human):
    def __init__(self, health, defense):
          super().__init__(health) #super this one call parent class
          self.defense = defense
      
class Barbarian(Human):
    def __init__(self, health, damage):
          super().__init__(health)
          self.damage = damage

warrior = Warrior(50,5.5)
barbarian = Barbarian(100, 8.1)
warrior.attack()
barbarian.attack()
print(warrior.health)
print(warrior.defense)


#exercise : Create a monster class where you can set a health and damage attribute on creation
# it should also inherit from a entity calss to get attack method that print attack and damge amount
# 

class Entity:
    #  def __init__(self, attack):
    #       self.attack = attack

     def attack(self):
          print(f"attack with {self.damage} damge")    


class Monster(Entity):
     def __init__(self, health, damage):
          
          self.health = health
          self.damage = damage  

     def __repr__(self):
           return f'A monster with {self.health} hp'          

monster = Monster(100, 30)
print(monster.health)
monster.attack()

print(monster)