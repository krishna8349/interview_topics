n = int(input('Enter a number = '))

def fibonacci(n):
    a=0
    b=1

    for i in range(0,n):
        temp = a+b
        a=b
        b=temp
        print(b)

fibonacci(n)