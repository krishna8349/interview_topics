from errno import ECHILD
from platform import node
from tkinter import S
from turtle import pu


class Node:
    def __init__(self, key,next=None):
        self.key = key
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.nodeCount = 0

    def push(self,x):

        node = Node(x)

        if node is None:
            print("Stack Overflow")
            return
        
        node.data = x

        node.next = self.top

        self.top = node

        self.nodeCount += 1

    def isEmpty(self):
        return self.top is None

    def size(self):
        return self.nodeCount

    def pop(self):
        if self.top is None:
            print('Stack Underflow')
            exit(-1)

        top = self.top.data

        self.top = self.top.next

        self.nodeCount -= 1

        return top


if __name__ == '__main__':

    stack = Stack()

    stack.push(1)
    stack.push(2)

    print(stack.isEmpty())
    print(stack.size())

    stack.pop()
    stack.pop()

    if stack.isEmpty():
        print('The stack is empty')
    else:
        print('The stack is not empty')