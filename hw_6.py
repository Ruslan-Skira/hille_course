# 1
first = {1: 10, 2 : 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
lst = [first, second, third, fourth, fifth]
dictionary = {}
for i in range(len(lst)):
    dictionary.update(lst[i])
print(f"цикл for: {dictionary}" )

lst2 = {**first, **second, **third, **fourth, **fifth}
print(f"метод: {lst2}")

# 2
dictionary = {}
for i in range(11, 21):
    dictionary[i] = i ** 2
print(dictionary)

a = dictionary.values()
print(sum(a))

# 3
print(sorted(dictionary.keys()))

# 4 - ?

# 5
lst = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
uniqueV = set()
for i in lst:
    for val in i.values():
        uniqueV.add(val)
print(uniqueV)

# 6
shedule = {'monday': ['clean house', 'drive car', 'meet with freands'], 'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']}
key_list = list(shedule)
count = 0
for key in range(len(shedule)):
    if shedule[key_list[key]] is None:
        continue
    count += len(shedule[key_list[key]])
print(count)






