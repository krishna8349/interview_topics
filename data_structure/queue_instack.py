from collections import deque
from inspect import stack
import re

class Queue:
    def __init__(self):
        self.data = deque()

    def enqueue(self,element):
        self.data.append(element)

    def isEmpty(self):
        if len(self.data) == 0:
            print('Queue Underflow')
        exit(-1)

    def dequeue(self):
        if self.isEmpty is not None:
            return self.data.pop()
    
    def peek(self):
        return self.data[-1]

if __name__ == '__main__':

    queue = Queue()

    value = [1,2,3,4]
    print(queue.peek())
    for i in value:
        queue.enqueue(value)
        # print(i)

    queue.dequeue()
    # queue.dequeue()
    queue.dequeue()

    print(queue.isEmpty())
    