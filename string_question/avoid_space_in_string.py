main_str = "Lets go to visite    somewhere"

print("Normal code of my string : "+main_str)

new_str =sum(not chr.isspace() for chr in main_str)

print("After count of string :" +  str(new_str))