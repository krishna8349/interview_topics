from re import I


elements = [45,5,89,19,20]

for i in range(len(elements)):
    min_indx = i
    for j in range(i+1, len(elements)):
        if elements[min_indx] > elements[j]:
            min_indx = j

    elements[i], elements[min_indx] = elements[min_indx], elements[i]

print("sorting elements")
for k in range(len(elements)):
    print(elements[k], end= " ")