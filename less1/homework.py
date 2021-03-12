# 1
a = 'hello'
b = 'world'
print(a, b)
num_1 = int(input())
print('Ваше число: ', num_1)

# 2
time = int(input('Время в секундах: '))
hours = time // 3600
minutes = (time // 60) - (hours * 60)
seconds = time % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')

# 3
n = input('Введите число: ')
print(f'{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}')

# 4
num_user = int(input('Enter int: '))
current_max = 0
num = num_user  # отдельная переменная для хранения оставшейся части

while num > 0:
    digit = num % 10  # минус последнюя цифра
    if digit > current_max:
        current_max = digit
        if current_max == 9:  # Необязательно, максимальное число в любом случае 9
            break
    num = num // 10  # отсекаем от числа последнюю цифру

print(f'Наибольшая цифра у введенного числа {num_user}:', current_max)

# 5

revenue = float(input('Выручка: '))
costs = float(input('Издержки: '))

result = revenue - costs

if result > 0:
    print('Компания работает с прибылью:', result)
    print('Рентабельность:', result / revenue)
    people = int(input('Численность сотрудников: '))
    print(f'Прибыль на одного сотрудника: {result / people:.2f}')
elif result < 0:
    print('Компания работает с убытком:', result)
else:
    print('Комапния работает в 0')

# 6

while True:
    days = 1
    start_km = int(input('Стартовый результат: '))
    last_km = int(input('Желаемый результат: '))
    if start_km > last_km:
        print('Введены неверные данные')
    else:
        while start_km < last_km:
            start_km += start_km * 0.1  # start_km = start_km + (start_km * 0.1)  # start_km *= 1.1
            days += 1  # days = days + 1
        print('Результат будет через {} дней'.format(days))
        break
