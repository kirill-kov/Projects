#18 http://acmp.ru/index.asp?main=bstatus&id_t=18
#Требуется вычислить факториал целого числа N.
#Нужно вывести одно целое число — значение N!.
#топ 20 - 40 символов
n=int(input())
r=1
while n:
  r*=n
  n-=1
print(r)

#324 http://acmp.ru/index.asp?main=bstatus&id_t=324
#Требуется написать программу, определяющую, 
#является ли натуральное число N или слово палиндромом
#топ 20 - 38 символов
s=input()
print('YNEOS'[s!=s[::-1]::2])

#550 http://acmp.ru/index.asp?main=task&id_task=550
#вывести дату Дня программиста в формате DD/MM/YYYY, 
#где DD — число, 
#MM — номер месяца (01 — январь, 02 — февраль, ..., 12 — декабрь), 
#YYYY — год в десятичной записи.
#топ 20 - 81 символ
a=int(input())
print(['13/09/%04d'%a,'12/09/%04d'%a][a%400==0 or a%4==0 and a%100!=0])

#970 http://acmp.ru/index.asp?main=task&id_task=970
#Задача – по заданным трем числам определить: 
#можно ли их переставить так, чтобы сумма первых двух равнялась третьему.
#топ 20 - 73 символов
a,b,c = map(int,input().split())
print(['NO','YES'][a+b==c or b+c==a or a+c==b])
