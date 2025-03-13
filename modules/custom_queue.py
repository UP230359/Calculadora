class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        
    def is_empty(self):
        return self.first is None
    
    def enqueue(self, value):
        new_node = Node(value)
        self.size += 1
        if self.is_empty():
            self.first = self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
                
    def dequeue(self):
        if self.is_empty():
            return None
        self.size -= 1
        value = self.first.value
        self.first = self.first.next
        if self.first is None:
            self.last = None
        return value
    
    def peek(self):
        return None if self.is_empty() else self.first.value

# stack.py
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None
    
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            return None
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value
    
    def peek(self):
        return None if self.is_empty() else self.top.value