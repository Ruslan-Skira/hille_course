# 1
a = int(input("Enter the number 1 : "))
b = int(input("Enter the number 2 : "))
c = int(input("Enter the number 3 : "))
def maximum(a: int, b: int, c: int):
    return max(a, b, c)
print(maximum(a, b, c))

# 2
x = int(input("Enter the number 1 : "))
y = int(input("Enter the number 2 : "))
z = int(input("Enter the number 3 : "))
def maximum(x, y):
    return max(x, y)

def maximum_2(x, y, z):
    middle = maximum(x, y)
    return maximum(middle, z)
print(maximum_2(x, y, z))

# 3-?

# 4
from datetime import date
today = date.today()
print(today.year)
print(today.month)
print(today.day)