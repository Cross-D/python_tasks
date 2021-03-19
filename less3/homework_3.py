# 1
def my_div(num_1, num_2):
    try:
        num_1, num_2 = float(num_1), float(num_2)
        answer = num_1 / num_2
    except ValueError:
        return 'error', 'Ошибка числа'
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    return answer
my_div(input(), input())


# 2
def personal_info(**text_info):
    return text_info
print(personal_info(
    name=input('Имя: '),
    surname=input('Фамилия: '),
    bitrhday=input('Дата рождения: '),
    city=input('Город: '),
    email=input('Почта: '),
    phone=input('Телефон: '),
))


# 3
def my_func(num_1, nim_2, num_3):
    my_list = [num_1, nim_2, num_3]
    try:
        answer = sum(my_list) - min(my_list)
    except TypeError:
        return 'Check number'
    return answer
print(my_func(1, 2, 3))


# 4
def my_pow_func(x, y):
    try:
        ans = x ** y
    except TypeError:
        return 'Enter float'
    return ans
print(my_pow_func(10, -4))


# 5
def summary():
    ex = False
    result = 0
    while ex == False:
        numbers = input('Enter numbers or q to exit: ').split()
        res_line = 0
        for num in numbers:
            if 'q' in num:
                ex = True
                break
            res_line += int(num)
        result += res_line
    return result


# 6
def int_func(text):
    return text.title()

print(int_func('слово'))
res_int_func = int_func('несколько слов')
print(res_int_func)
