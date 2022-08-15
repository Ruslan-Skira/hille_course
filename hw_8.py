# 1 a
laptop = ["asus", "acer", "hp",]
print("1", all(laptop))

number = [1, 2, 3, []]
print("2", all(number))

# b
print("3", all([bool([]), bool(''), bool(0)]))

# 2
laptop2 = ["", "lenovo", "xiaomi"]
print("4", any(laptop2))

laptop3 = ["", "", ""]
print("5", any(laptop3))

# 3
marks = [60, 88, 90, 99]
print("6", isinstance(marks, list))

marks = (2, 3, 5, 4)
c = isinstance(marks, tuple)
print("7", c)

a = 12
b = isinstance(a, int)
print("8", b)

word = "i am python dev"
k = isinstance(word, str)
print("9", k)

num = 12.4
print("10", isinstance(num, float))

dictionary = {"alex" : 178, "andrew" : 190, "max" : 187}
print("11", isinstance(dictionary, dict))


