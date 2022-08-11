# 1
password = input("Enter your password: ")
password2 = input("Repeat your password: ")
while password != password2:
    password = input("Enter your password: ")
    password2 = input("Repeat your password: ")
else:
    print("Уour passwords matched")

# 2
products = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']
while 'eg' in products:
    products.remove('eg')
print(products)

# 3
numbers = [11, 23, 65, 44, 76, 533]
amount = len(numbers) - 1
n = 0

while n < amount:
    if numbers[n] % 2 == 0:
        n += 1
        if n == amount and numbers[n] % 2 == 0:
            print("all numbers are even")
    else:
        print("NO")
        break

# 6
set1 = {1, 2, 3}
set1.add(4)
print(set1)

set2 = {3, 4, 5}
set2.discard(4)
print(set2)

set3 = {6, 7, 8}
set3.clear()
print(set3)

set4 = {8, 9, 10}
set4.update([11, 12])
print(set4)