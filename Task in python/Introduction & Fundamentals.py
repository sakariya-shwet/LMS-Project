#<<<< TASK IN PYTHON >>>>

#<<<< INTRODUCTIONS AND FUNDAMENTALS  >>>>

print("="*80)


print("i.) Write a program that prints your name, age, and city using print()")

print("\n")

name=input("Enter your Name:--")
age=input("Enter your Age:--")
city=input("Enter your City:--")

print(f"Your name is:- {name}  ,And your age is:-- {age}  , Your city is:-- {city}")

print("="*80)


print("ii.)Take user's name as input and greet them: 'Hello, [name]! Welcome to Python!")

print("\n")

name=input("Enter your name")

print(f"Hello,"+name+ "!","welcome to python")

print("="*80)


print("iii.)Create variables of each datatype (int, float, str, bool) and print them with type()")

print("\n")

a = 10
b = 3.99
c = "Python"
d = True

print("value of int:-", a, type(a))
print("value of float:-", b, type(b))
print("value of str:-", c, type(c))
print("value of bool:-", d, type(d))

print("="*80)

print("iv.)Use id() to compare two variables and check if they point to the same memory")

print("\n")

a = int(input("Enter a number:--"))
b = int(input("Enter a same number:--"))

print("id of a:", id(a))
print("id of b:", id(b))

if id(a) == id(b):
    print("a and b point to the same memory location")
else:
    print("a and b point to different memory locations")

print("="*80)

print("v.)Take two numbers as input, perform all arithmetic operators, and display results")

print("\n")

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))

print ("addition", a+b)
print ("substraction", a-b)
print ("multiplication", a*b)
print ("division", a/b)
print ("modulus",a%b)
print ("floor division",a//b)
print ("Exponentiantion",a**b)

print("="*80)

print("vi.)Convert a float to int, int to string, and string to float using type casting")

print("\n")

num_float = float(input("Enter a number in float:-- "))
num_int = int(num_float)

num_int_input = int(input("Enter a number in int:-- "))
num_str = str(num_int_input)

num_str_input = input("Enter a number in string:-- ")
num_float2 = float(num_str_input)

print("Float to int:", num_int)
print("Int to string:", num_str)
print("String to float:", num_float2)

print("="*80)

print("vii.)Take a temperature in Celsius as input and convert it to Fahrenheit")

print("\n")


celsius = float(input("Enter temperature in Celsius:-- "))
fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:--", fahrenheit)




















