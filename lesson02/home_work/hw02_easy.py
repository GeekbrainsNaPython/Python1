# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз

# Подсказка: воспользоваться методом .format()

print("Задача-1")

a = ["яблоко", "банан", "киви", "арбуз"]
j = 1
for i in a:
    print("{0}. {1}".format(j,'{:>6}'.format(i)))
    j += 1

# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
a = list()
b = list()

""" for i in a:
    j = 0
    while j <= a.count():
        if i == b[j]:
            b.

 """
# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

print("Задача-3")

a = [1,23,4,64,2,47,8,32,76,4,7]
b = list()

for i in a:
    if i % 2 == 0:
        b.append(i / 4)
    else:     
        b.append(i*2)

print(a,"\n",b)