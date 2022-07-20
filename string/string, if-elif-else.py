# 1 задача - ???



# 2 задача
print("HELLO USER")
nickname = str(input("Enter your nickname: "))
sex = str(input("Enter your sex: "))
age = int(input("Enter your age: "))
if nickname == "admin":
    print("Привет, повелитель!")
elif nickname == "Guido":
    print("Огромное спасибо")
elif 10 < age < 14 and sex == "M" or age > 30 and sex == "M":
    print("Советую Вам посмотреть 'StarWars' или 'Мандалорец'")
elif 22 < age < 33 and sex == "F":
    print("Рекомендация, советую вам посмотреть 'Трансформеры'")
elif age < 16 and sex == "F":
    print("Советую посмотреть вам 'Инсургент'")
elif nickname == "Женя":
    print("Советую вам посмотреть 'TENET'")
elif age < 11 and sex == "M":
    print("Советую Вам посмотреть 'TMNT'")
else:
    print("Вы ввели что то не то")

# 3 задача
character_set = '(etnfづzxfk｡12dt◕`1ad‿6hns‿1zQY◕Cd$y｡FtSq)Ze6?づ#2)$'
print(character_set[5:50:5])

# 4 задача - ???

# 5 задача
text = input("Введите текст: ")
print(text.replace("черт", "####"))



