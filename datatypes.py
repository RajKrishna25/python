name=input("Enter your name:") #string
age=int(input("Enter your age:"))#string
gender=input("Enter your gender:")#string
weight=float(input("Enter your weight:"))#string


print("Your name is :",name,type(name))
print("Your age is :",age,type(age))
print("Your gender is :",gender,type(gender))
print("Your weight is :",weight,type(weight))#45.45
weight=int(weight)
print("Your weight is :",weight,type(weight))
#float>int

# # single line comment
# """
# multi line comment
# """

# write a program to get user input of their age and height and weight and calculate their bmi

# 
a=20
b=6
# arithmetic
print("sum",a+b)
print("sub",a-b)
print("multiply",a*b)
print("exponentiation",a**b)
print("floor division",a//b)
print("modulus",a%b)

# comparison
print("greater than" ,a>b)
print("less than" ,a<b)
# print("geater than" ,a>b)
# print("geater than" ,a>b)
print("equal " ,a==b)
print("not equal " ,a!=b)

# logical
x = 2

print(x > 3 and x < 10)
x = 5

print(x > 3 or x < 4)
x = 5

print(not(x > 3 and x < 10))
# exp= a>b and a==b #true and true -> true
