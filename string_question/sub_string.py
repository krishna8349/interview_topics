def sub_string(str, subStr):
    arr = []

    for i in range(len(str)):
        for j in range(i+1, len(str) + 1):
            subst = str[i:j]
            arr.append(subst)
    if subStr in arr:
        return True
    return False
    
str = "geeksforgeeks"
substring = "forg"
print(sub_string(str, substring))