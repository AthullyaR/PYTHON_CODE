from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def isempty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
    def display(self):
        return list(self.container)

def reverse(st):
    sta=Stack()

    for i in st:
        sta.push(i)

    rstr=" "
    while sta.size()!=0:
        rstr+=sta.pop()

    print(rstr)


s=Stack()
s.push(2)
s.push(1)
s.push(5)
s.push(7)
a=s.peek()
print(a)
print(s.isempty())
print(s.size())
reverse('love')
all=s.display()
print(all)