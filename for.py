# 1
text = input("Enter the string: ")
if len(text) <= 2:
    print("Ваша строка слишком короткая ", text)
else:
    print(text[0:2], text[-2:len(text)], sep="")

# 2


# 3
products = input("Enter the products: ").split(", ")
print(("Самое длинное название продукта {} длина {} символов").format(max(products), len(products)))


# 4
name = input("Enter your name: ")
print(("{}, {}").format(name.upper(), name.lower()))

# 5
word = list(input("Enter the colors or products: ").split(", "))
word.sort()
print(word)

# 6
tuple1 = tuple(input("Enter the the numbers: ").split(", "))
print(tuple1[:-1])

# 7


# 8
for i in range(-99, 99, 3):
    if i % 3 == 0:
        print(f"Это число {i} делется без остатка на 3")

# 9







