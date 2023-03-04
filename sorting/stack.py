from collections import deque
from select import select
from turtle import st


class Stack:
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def add(self,value):
        self.item.insert(0,value)

    def pop(self):
        return self.pop(0)

    def peek(self):
        return self.item[0]
    
    def size(self):
        return len(self.item)

stack = Stack()
print(stack.add(5))
print(stack.add(6))
print(stack.isEmpty())
print(stack.peek())
print(stack.size())
# stack.isEmpty()