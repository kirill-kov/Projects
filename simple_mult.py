#Программа определяет и выводит простые множители заданного пользователем числа

import os

def greeting():
    print(
"""
Программа находит простые множители заданного Вами числа.
Введите число
""")
    num = int(input())

    return num

def simp_mult(num):
    arr = []
    m = 2
    i = 0
    while (m <= num):
        if (num % m == 0):
            num /= m
            new_elem = m
            arr.append(new_elem)
            i+=1
        else: m+=1
    return arr


def main():
    numb = greeting()
    res = simp_mult(numb)
    print("Простые множители числа", numb, "=", res)
    os.system("pause")


if __name__ == '__main__':
    main()
