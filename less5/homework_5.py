# 1
with open('test.txt', 'w') as f:
    while True:
        line = input('Введите строку: ')
        if line == '':
            break
        f.write(line + '\n')


# 2
with open('test.txt') as f:
    lines = f.readlines()
print('Количество строк:', len(lines))
for num_line, line in enumerate(lines, start=1):
    print('{} В строке содержится - {} слов'.format(num_line, len(line.split())))


# 3
with open('salaries.txt') as f:
    lines = f.readlines()

salaries = []
for line in lines:
    name, salary = line.split(' - ')
    salaries.append(int(salary))
    if int(salary) < 20000:
        print(line, end='')
print('\nСредняя зарплата:', sum(salaries) / len(salaries))


# 4
with open('eng.txt', encoding='utf-8') as f:
    lines = f.readlines()

with open('rus.txt', 'w', encoding='utf-8') as f:
    for line in lines:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        f.write(line)


# 5
with open('5.txt', 'w') as f:
    nums = input('Введите целые числа через пробел: ')
    f.write('Введенные числа: ' + nums + '\n')
    nums = map(int, nums.split())  # without list
    sum_nums = sum(nums)
    f.write('Сумма чисел: ' + str(sum_nums))
print('Сумма введенных чисел:', sum_nums)
print('Все записано в файл')


# 6
my_dict = dict()
with open('6.txt') as f:
    lines = f.readlines()

for line in lines:
    splitted_line = line.split()
    subject = splitted_line[0]
    sum_lessons = sum([int(x[:x.find('(')]) for x in splitted_line[1:] if '(' in x])
    my_dict[subject[:-1]] = sum_lessons
print(my_dict)


# 7
import json

firm_dict = {}
average_profit = []
with open('7.txt') as f:
    lines = f.readlines()

for line in lines:
    name, form, revenue, costs = line.split()
    profit = int(revenue) - int(costs)
    firm_dict[name] = profit
    if profit > 0:
        average_profit.append(profit)

average_profit = sum(average_profit) / len(average_profit)
out_info = [firm_dict, {'average_profit': average_profit}]

with open('7.json', 'w') as f_json:
    json.dump(out_info, f_json)

with open('7.json') as f_json:
    print(json.load(f_json))

