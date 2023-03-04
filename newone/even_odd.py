from turtle import right


value = int(input("Enter a value "))

def check_value(value):
    for i in range(1,value+1):
        if i%2 != 0:
            print(i,end=" ")

check_value(value)