# Напишите программу, которая принимает две строки вида
# “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

print("Запишите два числа в такой форме 'a/b' и вам вернется \nсумма и произведение данных чисел")

first_number = input("")
second_number = input("")
index = 0
a_1 = ""
a_2 = ""
b_1 = ""
b_2 = ""

while index < len(first_number):
    a_1 += first_number[index]
    index += 1
    if first_number[index] == "/":
        index += 1
        while index < len(first_number):
            a_2 += first_number[index]
            index += 1
index = 0

while index < len(second_number):
    b_1 += second_number[index]
    index += 1
    if second_number[index] == "/":
        index += 1
        while index < len(second_number):
            b_2 += second_number[index]
            index += 1

print("Произведение дробей равно :", int(a_1)*int(b_2), "/", int(a_2)*int(b_1))

a1 = ""
b1 = ""
a2 = ""
b2 = ""
if a_2 != b_2:
    a1 = int(a_1)*int(b_2)
    b1 = int(b_1)*int(a_2)
    a2 = int(a_2)*int(b_2)
    b2 = int(b_2)*int(a_2)
    print("Сумма дробей равна :", a1 + b1, "/", a2)

if a_2 == b_2:
    if int(a_1) + int(b_1) == int(a_2):
        print("сумма дробей равна единице")
    else:
        print("сумма дробей равна :", int(a_1) + int(b_1), "/", int(a_2))