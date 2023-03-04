from re import I


value = int(input("Enter a value = "))
sum = 0
for i in range(0,value,1):
    sum +=value
    value-=1
    
print(sum)