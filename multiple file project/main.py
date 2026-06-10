# import support 

# test = support.Test()
# print(test.a)
# test.some_method()

# print(support.var)
# print(support.add_2_numbers(2,2))


####next way
from support import Test, var, add_2_numbers

test = Test()
print(test.a)
test.some_method()

print(var)
print(add_2_numbers(2,3))