# Напишите программу, которая получает целое число
# и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def hexadecimal(enter_number):
    result_16 = "0x"

    list_result_16 = []
    remains = None
    divisible = None
    list_result_16.append(str(enter_number % 16))
    remains = enter_number % 16
    divisible = enter_number // 16

    while divisible != 0:
        remains = divisible % 16
        divisible //= 16
        list_result_16.append(str(remains))

    list_result_16.reverse()

    for i in list_result_16:
        if i == "10":
            result_16 += "a"
        elif i == "11":
            result_16 += "b"
        elif i == "12":
            result_16 += "c"
        elif i == "13":
            result_16 += "d"
        elif i == "14":
            result_16 += "e"
        elif i == "15":
            result_16 += "f"
        else:
            result_16 += i
    return result_16

print(hexadecimal(1515))

print(hex(1515))
