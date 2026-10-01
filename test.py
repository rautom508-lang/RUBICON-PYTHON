#lst=(10,20,30)
#print(dir(lst))
#print(type(lst))
#t1=(100,200,300)
#a,*b=t1
#print(a)
#print(b)
#d1={'name':"om"}
#rint(d1)
#print(dir(d1)
#def  funtion_name(para1,para2):
#    print(f"testing funtion called.....{para1} {para2}")
#x= "om"
#l="marathi"
#funtion_name("om","marathi")
#funtion_name("radha")

# def addtion(a,b):
#     answer=a
#     answer=b
    
#     return answer
    
# s=addtion()
# result=addtion(b=20,a=30)
# print(result)
# print(help(*args))
# arbitary postion argument 
# (*)<-this need for the for arbiatry constant )
# altimate arbitary based arugument 
# when i want  to save the multiple arguent in the def funtion that we dose use the the ->(**)

# def testing():
   
#     def fuc():
#         print("testing function called..")

# testing
# def testing():
#     print("testing function called....")


# def my_fuction(func):
#     func()
#     print("fuction called.....")

# my_fuction(testing)
# def getsqr(num):
#     return num*num
# def my_fuction(num,func):

#     if num>10:
#         result = func(num)
#         return result
#     else:
#         print("plesas enter nuym greater thean 10")
#         return 
# x=int(input("enter a number here "))
# result = my_fuction(x,getsqr)
# print(result)
# def testing():
#     print("testing fuction called ....")

#     def inner():
#         print("testing inner function...")
#     return inner 

# result= testing
# print(type(result))
# result ()
# def my_function(num):
#     print("my_fuction is called..")
#     def getSqr():
#         print("getSqr called...")
#         return num*num
#     return getSqr
# the inner function creates a closeure for itself and outer fuction variables,
# so even when outer function is done executing i.e terminated . it's variables are preserved in
#   the closure of nested / inner fuction. theis behaviour is called closures.

# result = my_function(10)
# print(result())
# print(result)
# def addition(a,b):
#     print("Testing fuction called..")
#     return a+b
    

# def my_function(func):
    
#     def wrapped(a,b):
#         print("Before function called..")
#         result=func(a,b)
#         print(f"{result}")
#         print("After function called....")
#         return result
#     return wrapped

# addition = my_function(addition)
# print(addition(10,20))

# def safeDecorator(func):
#     def wrapper(*args):
#         first_num=args[0]
#         second_num=args[1]
#         if first_num >10 and second_num > 10:
#             result=func(*args)
#             return result
#         return "First 2 number should be more than 10"
#     return wrapper 
# def addition(a,b):
#     return a+b
# addition = safeDecorator(addition)
# print(addition (15,14))

                                            #   OOP     #     

                    
# class Employee:
#     pass
# e1 = Employee()
# e1.name="Om raut"
# e1.designation="Full stack developer"
# e1.salary = 90_000
# e1.age=21
# print(e1.name)
# print(e1.designation)
# print(e1.salary )
# print(e1.age)
# constructor 


# class Person:
#     def __init__(self):
#         print("Constructor is called....")
    
#     def testing(self,a):
#         print(f"testing fuction called....a={a}")
    
# p1=Person()
# p1.testing(100)


# Abstraction
# Absttaction is achieved by using abstract classes.
# An abstract class cannot be instratiated .we cannot create object of an abstract class.
#  AN ABSTRACT CLASS CAN ONLY BE INGERITED

# POLIMORPHISUM








