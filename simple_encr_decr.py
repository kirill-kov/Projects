def encrypt(str,key):
    a=list(str)
    for i in range(len(a)):
        a[i]= chr(ord(a[i])+key)
    str=''.join(a)
    return str

def decrypt(str,key):
    a=list(str)
    for i in range(len(a)):
        a[i]= chr(ord(a[i])-key)
    str=''.join(a)
    return str

def main():
    str=input("Введите строку для шифрования:")
    token=int(input("Введите ключ:"))

    res1=encrypt(str,token)
    print(res1)

    res2=decrypt(res1,token)
    print(res2)

if __name__ == '__main__':
    main()
