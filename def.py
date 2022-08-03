# 1
from math import sqrt
def square(sd):
    return f"perimeter: ",{4 * sd}, "square: ", {sd**2}, "diagonal: ", {round(sqrt(2)*sd)}
side = square(int(input("Enter side length of square: ")))
print(side)

# 2
month = int(input("Enter the number of month: "))
def number_of_month(m):
    if m == 1:
        print("January")
    elif m == 2:
        print("February")
    elif m == 3:
        print("March")
    elif m == 4:
        print("April")
    elif m == 5:
        print("May")
    elif m == 6:
        print("June")
    elif m == 7:
        print("July")
    elif m == 8:
       print("August")
    elif m == 9:
        print("September")
    elif m == 10:
        print("October")
    elif m == 11:
        print("November")
    elif m == 12:
        print("December")
    else:
        print("you entered something wrong")
print(number_of_month(month))

# 3

# 4

text = input("Enter the text: ") #не работает, но я попробовал
def palindrom():
    if text == text[::-1]:
        return True
    else:
        return False



