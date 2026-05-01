#Control Structures & Looping

print("i.)Check if a number entered by the user is positive, negative, or zero")

print("\n")

num = float(input("Enter a number:-- "))
 
if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")

print("="*80)


print("ii.)Build a simple grade calculator: A (90+), B (75+), C (60+), D (below 60) using ladder if-else")

print("\n")

marks = float(input("Enter your marks:-- "))


if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: D")

print("="*80)

print("iii.)Use match-case to print the day name based on a number (1=Monday, 2=Tuesday...)")

print("\n")


day = int(input("Enter a number (1-7):-- "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input! Please enter a number between 1 and 7.")

print("="*80)



print("iv.) multiplication table of any number using a while loop")

print("\n")

num = int(input("Enter number: "))
i = 1

while i <= 10:
    print(num, "x", i, "=", num * i); i += 1

print("="*80)


print("v.)Print all even numbers from 1 to 100 using a for loop and range")

print("\n")

for i in range(1,100):
     if i % 2 == 0:
      print("Even number",i)

print("="*80)


print("vi.)Use nested loop to print a star pyramid pattern")

print("="*80)

rows=5

for i in range(1,rows+1):
     print("*"*i)

print("="*80)



print("vii.)Create a number guessing game: user gets 3 tries to guess a fixed number using break/continue")

print("\n")

Number = 7

for i in range(1, 10):
    guess = int(input("Enter a number in 1 to 10: "))

    if guess == Number:
        print("Nice guessed!!")
        print("Game over")
        break
    else:
        print("Try to guess again")

print("="*80)

print("viii.)Find and print all prime numbers between 1 and 50")

print("\n")

for num in range(2, 51):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

print("="*80)




