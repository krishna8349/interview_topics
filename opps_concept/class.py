# from unicodedata import name  


from multiprocessing.sharedctypes import Value


class Test:
    def __init__(self, name):
        self.name = name

    def add_name(self ):
        return self.name

    
# if __name__ == '__main__':
emp =[ 'Krishna', 'abhi']

test = Test(emp)

# test.add_name()
print(test.add_name())