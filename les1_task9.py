# 9 

# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

num1 = int(input("Введите первое число\n >>> "))
num2 = int(input("Введите второе число\n >>> "))
num3 = int(input("Введите третье число\n >>> "))

if num2 < num1 < num3 or num3 < num1 < num2:
    print('Среднее:', num1)
elif num1 < num2 < num3 or num3 < num2 < num1:
    print('Среднее:', num2)
else:
    print('Среднее:', num3)

