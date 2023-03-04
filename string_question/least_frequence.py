# def least_frequence(str):
text_str = "GeekforGeeks"
lfreq = {}
for i in text_str:
    if i in lfreq:
        lfreq[i] += 1
    else:
        lfreq[i] = 1
res = min(lfreq, key=lfreq.get)

print("least frequence : " +str(res))