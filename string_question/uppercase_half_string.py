test_str = "geeksforgeeks"

print("The orignal string is :" + test_str)

helf_len = len(test_str)//2

res = ""

for idx in range(len(test_str)):
    if idx >=helf_len:
        res += test_str[idx].upper()
    else:
        res += test_str[idx]

print("The result string :"+str(res))