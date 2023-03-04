from itertools import count


def vowel_count(str):
    count = 0

    vowel = set("aeiouAEIOU")

    for alpha in str:
        if alpha in vowel:
            count+= 1
    print("No of vowel :",count)

str = "GeeksforGeeks"
vowel_count(str)