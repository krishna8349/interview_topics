from posixpath import split


def word_cap(str):

    return  ' '.join(map(lambda s: s[:-1]+s[-1].upper() , s.title().split()))

s="hello world"
print("string before :"+s)
print("string after :" + word_cap(str))