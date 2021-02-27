# 9
# Среди натуральных чисел, которые были введены, найти наибольшее 
# по сумме цифр. Вывести на экран это число и сумму его цифр

num1 = input("Введите первое число: ")
num2 = input("Введите второе число: ")
num3 = input("Введите третье число: ")

nn1 = num1.split()
nn2 = num2.split()
nn3 = num3.split()

num1summ = 0
num2summ = 0
num3summ = 0

for n1 in nn1:
    num1summ = num1summ + int(n1)

for n2 in nn2:
    num2summ = num2summ + int(n2)
for n3 in nn3:
    num3summ = num3summ + int(n3)

if num1summ > num2summ and num1summ > num3summ:
    print("Наибольшая сумма {}, число {}".format(num1summ, num1))

if num2summ > num1summ and num2summ > num3summ:
    print("Наибольшая сумма {}, число {}".format(num2summ, num2))

if num3summ > num2summ and num3summ > num1summ:
    print("Наибольшая сумма {}, число {}".format(num3summ, num3))

