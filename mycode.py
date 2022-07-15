# Задание 1
user_name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
if age > 121:
    print("You are not real", user_name)
elif age >= 70 and age <= 90:
    print("You are lucky", user_name, "and welcome.")
elif age == 16:
    print("Dear", user_name, "need to wait one year.")
elif age > 16:
    print("Welcome", user_name, "on our website.")
else:
    print("I'm sorry", user_name, "you are too young.")

# Задание 2
a1 = 8+4
a2 = 10-6
a3 = 3*2
a4 = 4 / 2
a5 = 5 % 3
a6 = 20 // 3
a7 = 5**3

a8 = 9 > 6
a9 = 5 < 10
a10 = 3 == 3
a11 = 8 != 3
a12 = 15 >= 7
a13 = 18 <= 20

a14 = 3 > 2 and 5 < 10
a15 = 8 == 8 or 11 < 17
a16 = not False

a17 = 8
a17 += 5
a17 -= 3
a17 *= 9
a17 /= 4
a17 %= 3
a17 //= 5
a17 **= 3

a >>= 4
a <<= 4




