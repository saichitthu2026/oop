# # def myFun(name, /):
# #     print("Hello", name)
# # myFun(name="Hla")

# # def myFunn(name):
# #     print("hello", name)
# # myFunn(name="ma")


def myFun(*nums):

    total=0    
    
    for num in nums:
        total = total + num 
    
    return total


print(myFun(40,50,60,90,2,1))


def add(a,b):
    return a+b
print(add(3,5))
print(add(-2,7))

def greet(name):
    print("Hello", name)

# greet("aung")  
# greet("Su")

# def is_even(num):
#     if num%2 == 0:
#         print("True")
#     else:
#         print("False")

# is_even(8)
# is_even(7)
# is_even(0)

def is_even(numm):
    return numm%2==0


print(is_even(8))
print(is_even(7))

print(is_even(0))


