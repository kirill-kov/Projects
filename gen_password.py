import random

def greeting():
    print("""
Данная программа генерирует рандомный пароль
    """)

def gen_rand_password():
    str1 = '123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str1+str2+str3
    lt = list(str4)
    random.shuffle(lt)
    # psw = ''.join([random.choice(lt) for i in range(12)])

    psw = ''
    for i in range(12):
        psw = psw + random.choice(lt)

    print("Ваш пароль: ", psw)

def main():
    greeting()
    gen_rand_password()

if __name__ == '__main__':
    main()
