# 8
# Определить, является ли год, который ввел пользователь, високосным или не високосным

year = int(input("Введите год\n >>> "))
if ((year % 4 == 0) and not (year % 100 == 0)) or (year % 400 == 0):
    print('Високосный')
else:
    print('Не високосный')




