
# Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не 
# завершается, а запрашивает новые данные для вычислений. Завершение программы должно выполняться 
# при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак 
# (не '0', '+', '-', '*', '/'), программа должна сообщать об ошибке и снова запрашивать знак операции. 
# Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя

while True:
    first_num = int(input("Введите первое число: "))
    simvol = input("Введите знак операции: ")
    second_num = int(input("Введите второе число: "))

    if simvol == '+':
        result = first_num + second_num
        print("Result = {}".format(result))
    elif simvol == '-':
        result = first_num - second_num
        print("Result = {}".format(result))
    elif simvol == '*':
        result = first_num * second_num
        print("Result = {}".format(result))
    elif simvol == '/':
        if second_num != 0:
            result = first_num / second_num
            print("Result = {}".format(result))
        else:
            print("Ошибка: Деление на ноль!!!")
    elif simvol == '0':
        break

print("End of program!")