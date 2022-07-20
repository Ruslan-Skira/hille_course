# Базовый 40 баллов

# 1 задание
string1 = "Hello I'm python developer and I from Ukraine"
print("---STRING 1---")
print("h: ", string1.count('h'))
print("e: ", string1.count('e'))
print("el: ", string1.count('el'))

string2 = "Computers are popular in the World"
print("---STRING 2---")
print(string2.upper())
print(string2.lower())
print(string2.swapcase())

string3 = "The weather is sunny today"
print("---STRING 3---")
print("Position: ", string3.find('we'))
print("Position: ", string3.find('day'))
print("Position: ", string3[string3.find('sunny')::])
print("Position: ", string3[string3.find('The')::])

string4 = "My favourite animal is dog"
print("---STRING 4---")
print("True or False: ", string4.startswith('fav'))
print("True or False: ", string4.startswith('My'))
print("True or False: ", string4.endswith('it'))
print("True or False: ", string4.endswith('og'))

string5 = "I'm looking for coca-cola and pepsi"
print("---STRING 5---")
print("replace: ", string5.replace('coca-cola', 'pepsi'))
print("replace: ", string5.replace('pepsi', 'fanta'))

string6 = "integer data numbers python str types float"
print("---STRING 6---")
print(string6.split())
print(string6[-7].split())

string7 = "\t\n this is text \n\t"
print("---STRING 7---")
print(string7.strip())

# 2 задание
print("---string---")
str1 = 'hello world'
print(str1)
str2 = "hello world"
print(str2)
str3 = """hello world"""
print(str3)
print("---numbers---")

number = .5
print(number)
number1 = abs(-10)
print(number1)
number2 = round(34.57689)
print(number2)
number3 = round(23.1234, 2)
print(number3)

list1 = [0, 23, 34, 15]
list2 = ['a', 'b', 'c', 'd']
list3 = ['ab', 'hello', 17, 18]

car = {"Citroen": "France", "BMW": "Germany", "Tesla" : "USA", "Toyota" : "Japan"}
city = {"Kiev" : "capital", "square" : 840, "Street": "Khreshchatyk", "year_of_foundation" : 940}
languages = { 'europe' :
                  {"ukrainian" : "Ukraine",
                   "english" : "Uk",
                   "german" : "Germany",
                   "polish" : "Poland"
                   },
              'asia' :
                   { "сhinese" : "China",
                    "indian" : "India",
                    "japanes" : "Japan",
                    "singaporean" : "Singapore"
                   },
              "north America " :
                   {
                      "canadian" : "Canada",
                      "american" : "USA"
                   }
}

tuple0 = 5,
tuple1 = ("hello world", "fdd", 123)
tuple2 = ("word",)

# 3 задание
print("---MAX---MIN---")
print("max: ", max(-5, 12, 8, -30, 20))
print("min: ", min(15, 3, -2, 10, 26))

#5 задание
print("---IN---")
list = 5 in [3, 6, 8]
print(list)

list = 10 in [5, 10, -3]
print(list)

str = "I am python dev"
if "python" in str:
    print("you are developer")

#6 задание
print("--if--elif--else")
number = float(input("Введите число"))
if number % 2 == 0:
    print("число кратное 2")
elif number % 2 == 1:
    print("число не кратно 2")
else:
    print("вы ввели что то не то")

phone = input("Введите модель телефона")
if "Samsung" in phone:
    print("Телефон сделан в Ю.Корее")
elif "Iphone" in phone:
    print("Телефон сделан в США")
elif "Xiaomi" in phone:
    print("Телефон сделан в Китае")


