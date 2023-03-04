from tkinter.messagebox import RETRY


def checkstring(str):
    flag_1 = False
    flag_2 = False

    for i in str:
        if i.isalpha():
            flag_1 = True
        
        if i.isdigit():
            flag_2 = True

    return flag_1 and flag_2

print(checkstring('ksisodiya196'))
print(checkstring('ksisodiya'))
