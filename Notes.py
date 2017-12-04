'''
# Devin

a = 4
b = 3

print(3 + 5)
print(5 -3)
print(3 * 5)
print(6 / 2)
print(3 ** 2)

print("Try to figure out how this works")
print(13 % 12)

car_name = "Wiebe Mobile"
car_type = "BMW"
car_cylinders = 8
car_mpg = 5000.9

print("I have a car called %s. It's pretty nice." % car_name)
print("I have a car called %s. It's a %s." % (car_name, car_type))
                                              # Watch the order!

print("What is your name?")
name = input(">_ ")
print("Hello %s" % name)

age = input("How old are you?")

print("%s?! That's really old. You belong in a retirement hom." % age)

def print_hw():
    print("Hello World.")
    print("Enjoy the day.")



def say_hi(name):
    print("Hello %s" % name)
    print("Coding is great!")



def print_age(name, age):
    print("%s is %d years old" % (name, age))
    age = age + 1
    print("Next year, %s will be %d years old" % (name, age)

def algebra_hw(x):
    return x ** 3 + 4 + x + +2 + 7 * x - 4

def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "F"

print(grade_calc(90))

def happy_bday(name):
    print("Happy Birthday to you! \nHappy Birthday to you! \nHappy Birthday dear %s! \nHappy Birthday to you!" % name)


happy_bday("Devin")

# Loops

for i in range(0, 11):
    print(i)

a = 1
while a < 10:
    print(a)
    a += 1


# Random Numbers
import random #This should be on line 1
print(random.randint(0, 1000))

c = '1'
print(c == 1) # False: comparing different strings; string ≠ integer
print(int(c) == 1)
print(c == str(1))
'''

# Comparisons
print(1 == 1) # Use a double equal sign (==)
print(1 != 2) # 1 is not equal to 2