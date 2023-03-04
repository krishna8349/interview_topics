from audioop import reverse
import re
from unittest import removeResult


def sentence_word(sentence):

    str = sentence.split()

    for i in str:
        str1= str[::-1]

    # return(i)
    return str1

sentence = "krishna is my"

print(sentence_word(sentence))

