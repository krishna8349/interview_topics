from collections import deque


class Stack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def add(self, data):
        while len(self.q1):
            self.q2.append(self.q1.pop())
        
        self.q1.append(data)

        while len(self.q2):
            self.q1.append(self.q2.pop())
        
    def pop(self):
        if not self.q1:
            print('Stack Underflow')
            exit(0)
        
        front = self.q1.popleft()
        return front


if __name__ == '__main__':

    keys = [1,3,4,5,6]

    s = Stack()
    for key in keys:
        s.add(key)

    while s:
        print(s.pop())
    
    print(s.pop())