# 1
import sys
hours, salary_per_hour, bonus = map(float, sys.argv[1:])
print('Salary - {}'.format(hours * salary_per_hour + bonus))



# 2
my_list = [1, 9, 1, 72, 3, 4, 5, 6, 3]
new_list = [num for i, num in enumerate(my_list) if num > my_list[i - 1] and i != 0]
print(new_list)



# 3
print([x for x in range(20, 241) if x % 20 == 0 or x % 21 == 0])



# 4
my_list = [1, 1, 2, 2, 3, 4, 5, 6, 8, 3, 1, 4, 10, 11, 1]
new_list = [x for x in my_list if my_list.count(x) == 1]



# 5
from functools import reduce
def mul_list(n1, n2):
    return n1 * n2
my_list = [x for x in range(100, 1001) if x % 2 == 0]
print(reduce(mul_list, my_list))



# 6
# a
from itertools import count, cycle

for i in count(int(input('Введите стартовое число: '))):
    print(i)


# b
my_list = [1, 1, 2, 2, 3, 4, 5, 6, 8, 3, 1, 4, 10, 11, 1]

iter = cycle(my_list)
stop = ''
while stop != 'q':
    print(next(iter), end='')
    stop = input()



# 7
from math import factorial
from itertools import count

def fibo_gen():
    for el in count(1):  # бесконечный цикл, который начинается с 1
        yield factorial(el)

for step, i in enumerate(fibo_gen(), start=1):
    print('Factorial {} - {}'.format(step, i))
    if step == 15:
        break
