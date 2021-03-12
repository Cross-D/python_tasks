# 1
some_var = ['123', 123, [123], 123.0, False]
for i in some_var:
    print(type(i))

# 2
my_list = list(input('Enter text'))
for i in range(1, len(my_list), 2):
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
print(my_list)

# 3
seasons_dict = {
    1: 'Зима',
    2: 'Зима',
    3: 'Весна',
    4: 'Весна',
    5: 'Весна',
    6: 'Лето',
    7: 'Лето',
    8: 'Лето',
    9: 'Осень',
    10: 'Осень',
    11: 'Осень',
    12: 'Зима',
}
month = int(input('Веедите номер месяца: '))
print(seasons_dict[month])

# 4
line = input()
words = line.split()
for i, word in enumerate(words, start=1):
    print(i, word[:10])

# 5
my_list = [7, 5, 3, 3, 2]
request = int(input('Введите число: '))
for index, number in enumerate(my_list):
    if request <= number:
        continue
    my_list.insert(index, request)
    break
else:
    my_list.append(request)
print(my_list)

# 6
goods = []
features = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    if input('Выход - Q, \nЛюбая клавиша - продолжить: ').upper() == 'Q':
        break
    num += 1
    for f in features.keys():
        user_data = input(f'{f}: ')
        features[f] = int(user_data) if (f == 'цена' or f == 'количество') else user_data
        analitics[f].append(features[f])
    goods.append((num, features.copy()))
    print('Текущая аналитика по товарам:\n')
    for key, value in analitics.items():
        print(key, value)
print(goods)