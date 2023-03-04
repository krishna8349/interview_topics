from collections import deque
from re import S
from typing import Deque


class Stack:
    def __init__(self):
        self.data = deque()
        self.aux = deque()

    def add(self, value):
        self.data.append(value)

        if not self.aux:
            self.aux.append(value)
        else:
            if self.aux[-1] >= value:
                self.aux.append(value)
    
    def pop(self):
        if self.isEmpty():
            print("stack underflow")
            exit(-1)
        
        top = self.data.pop()

        if top == self.aux[-1]:
            self.aux.pop()

    def isEmpty(self):
        return not self.data
    
    def size(self):
        return len(self.data)

    def getMIn(self):
        if not self.aux:
            print("stack underflow")
            exit(-1)
        return 'Mininmun element is:',self.aux[-1]

if __name__ == '__main__':
    stack = Stack()

    # stack.add(1)
    stack.add(3)
    stack.add(4)
    # print(stack.add)
    print(stack.getMIn())
    stack.pop()

    # print(stack.isEmppty())
    print(stack.size())