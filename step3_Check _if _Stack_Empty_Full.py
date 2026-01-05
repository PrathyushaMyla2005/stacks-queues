class Stack:# Stack implementation with isEmpty and isFull methods
    def __init__(self, capacity):# initialize stack with given capacity
        self.stack = []          # list to store stack elements
        self.capacity = capacity # fixed maximum size

    def isEmpty(self):# check if stack is empty
        # stack is empty if length is 0
        return len(self.stack) == 0 # return True if empty, False otherwise

    def isFull(self): # check if stack is full
        # stack is full if length equals capacity
        return len(self.stack) == self.capacity # return True if full, False otherwise

    def push(self, x):# push element onto stack
        if self.isFull():# check for overflow
            print("Stack is FULL (Overflow)") #print overflow message 
            return # exit function
        self.stack.append(x) # add element to stack
        print(f"Pushed {x}") # print pushed element

    def pop(self): # pop element from stack
        if self.isEmpty(): # check for underflow
            print("Stack is EMPTY (Underflow)") # print underflow message
            return # exit function
        removed = self.stack.pop() # remove and return top element
        print(f"Popped {removed}") # print popped element

    def peek(self):# return top element without removing it
        if self.isEmpty(): # check if stack is empty
            print("Stack is EMPTY") # print empty message
            return None # return None if empty 
        return self.stack[-1] # return top element
# Example usage:
s = Stack(3) # create stack with capacity 3
s.pop()       # attempt to pop from empty stack
s.push(10)   # push 10 onto stack
s.push(20)   # push 20 onto stack
s.push(30)   # push 30 onto stack
s.push(40)   # attempt to push onto full stack
print(s.peek()) # peek at top element
s.pop()       # pop top element
s.pop()       # pop top element
s.pop()       # pop top element
s.pop()       # attempt to pop from empty stack
print(s.isEmpty()) # check if stack is empty
print(s.isFull())  # check if stack is full
