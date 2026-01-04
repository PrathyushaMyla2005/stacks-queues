'''problem statement:
Implement a Stack using an Array (or List) in Python. The Stack should support the following operations:
1. push(item): Add an item to the top of the stack.
2. pop(): Remove and return the item from the top of the stack. If the stack is empty, return None.
3. peek(): Return the item at the top of the stack without removing it. If the stack is empty, return None.
4. is_empty(): Return True if the stack is empty; otherwise, return False.
Stack size = 5
push(10)
push(20)
push(30)
Stack: [10, 20, 30]
Top → 30
pop()
Output: 30
Stack: [10, 20]
Top → 20
'''
#brute force
class stack: #class stack
    def __init__(self, size): #constructor to initialize stack
        self.size = size #size of stack
        self.stack = [] #initialize empty stack
    
    def push(self, item):#push item onto stack
        if len(self.stack) < self.size: #check if stack is not full
            self.stack.append(item) #add item to stack
        else:
            print("Stack Overflow") #if stack is full, print overflow message
    
    def pop(self): #pop item from stack
        if not self.is_empty():#check if stack is not empty
            return self.stack.pop() #remove and return top item
        else:
            return None #print None if stack is empty
    
    def peek(self): #peek at top item of stack
        if not self.is_empty():#check if stack is not empty
            return self.stack[-1] #return top item without removing it
        else:
            return None #print None if stack is empty
    
    def is_empty(self): #check if stack is empty
        return len(self.stack) == 0 #return True if stack is empty, else False
# Example usage:
s = stack(5) #create stack of size 5
s.push(10) #push 10 onto stack
s.push(20) #push 20 onto stack
s.push(30) #push 30 onto stack
print("Stack:", s.stack) #print current stack
print("Top →", s.peek()) #print top item
print("pop()")
print("Output:", s.pop()) #pop top item and print it
print("Stack:", s.stack) #print current stack
'''tc: O(1) for push, pop, peek, is_empty ehy 0(1) because we are using list which supports append and pop operations in constant time
sc: O(n) for stack storage where n is the size of the stack because we are using list to store stack elements
'''
