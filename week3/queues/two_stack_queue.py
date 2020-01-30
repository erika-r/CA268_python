
from stack import Stack

class Queue:
    def __init__(self):
    	self.stack1 = Stack()
    	self.stack2 = Stack()
    	self.size = 0

    def isempty(self):
        return self.stack1.is_empty() and self.stack2.is_empty()

    def enqueue(self, item):
        self.size += 1
        self.stack1.push(item)

    def dequeue(self):
    	self.size -= 1
    	if not self.stack2.is_empty():
    		return self.stack2.pop()
    	while not self.stack1.isempty():
    		self.stack2.push(self.stack1.pop())
    	return self.stack2.pop()