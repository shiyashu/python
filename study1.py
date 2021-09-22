#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print("shiyashu！！！welcome 中文！！！")
print('I\'m ok.')
print('\\\t\\')
print(r'\\\t\\')
print('''line1
... line2
... line3''')
print(10 / 3)
print(10 // 3)
print(10 % 3)
# Python内置的一种数据类型： 列表list。list是一种有序的集合，可以随时添加和删除其中的元素。
nameList = ['Michael', 'Bob', 'Tracy']
len(nameList)
nameList.append("shiyashu")
nameList.pop()
print(nameList)
# Python内置的一种数据类型： 有序列表 元组tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
numberTuple = (1,)
numberTuple.count
numberTuple = ('a', 'b', ['A', 'B'])
numberTuple[2][0] = 'X'
numberTuple[2][1] = 'Y'
# age = int(input('age: '))
# if age < 3:
#     print('baby')
# elif age <= 18:
#     print('teen')
# elif age <= 50:
#     print('adult')
# else:
#     print('older12')
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print("for循环：" + str(sum))
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print("while循环：" + str(sum))
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        print("while循环break语句会结束当前循环")
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        print("while循环continue语句会直接继续下一轮循环")
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)
# Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
nameDict = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
nameDict['Michael']
print(nameDict)
nameDict['Michael'] = 12
nameDict['Michael']
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
myabs = my_abs(-19)
print(myabs)
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)