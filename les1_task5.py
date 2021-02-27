# 5

# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв

char1 = input("Введите первую букву:\n >>> ")
char2 = input("Введите вторую букву:\n >>> ")
ch_num1 = ord(char1)
ch_num2 = ord(char2)

print("Буква {} стоит на месте {}".format(char1, ch_num1 - 96))
print("Буква {} стоит на месте {}".format(char2, ch_num2 - 96))

ch_range = ch_num2 - ch_num1
print("Между ними: "+ str(ch_range))



