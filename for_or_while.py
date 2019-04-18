from datetime import datetime

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

@timeit
def summa_while(n):
    sum=0
    while n:
        sum+=n
        n-=1
    return sum

@timeit
def summa_for(n):
    sum=0
    for i in range(1, n+1):
        sum+=i
    return sum

def main():

    n=int(input())
    t1=summa_while(n)
    t2=summa_for(n)

if __name__ == '__main__':
    main()
