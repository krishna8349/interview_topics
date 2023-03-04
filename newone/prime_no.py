start = int(input("Enter a start number = "))
end = int(input("Enter a end number = "))

for i in range(start, end+1):
    if i > 1:
        for val in range(2,i):
            if (i % val) == 0:
                break
        else:
            print(i, end=" ")