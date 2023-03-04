from audioop import reverse
from xml.sax.saxutils import prepare_input_source


name = "my name is krishna"


# sv =  rev.split()
new = ''.join(reversed(name))
print(new)
sp = new.split()
# print(sp)

temp = ""
for i in sp:
    temp+= i[::-1]+','
    
print(temp) 