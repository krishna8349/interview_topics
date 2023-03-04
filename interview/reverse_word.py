string = "Python is a language"

split_value = []
temp = ""
for i in string:
    if i == " ":
        split_value.append(temp)
        temp = ""
    else:
        temp += i
if temp:
    split_value.append(temp)

print(split_value)
s = "".join(reversed(string))
a=[]
a=s.split()
print(a)

new = []
for i in split_value:
    new.append(i[::-1])

print(new)
