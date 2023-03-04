main_str = "my name is krishna"

print("This is normal string :"+ main_str)

remove_str = ""

for i in range(len(main_str)):
    if i != 4:
        remove_str = remove_str+main_str[i]

print("String after removing i,th string :"+remove_str)