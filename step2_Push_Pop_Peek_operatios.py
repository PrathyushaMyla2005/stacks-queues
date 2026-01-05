'''problem: Implement a stack using a list in Python, with push, pop, and peek operations.
input
A sequence of stack operations, which can be:
push(x) → insert integer x into the stack
pop() → remove the top element of the stack
top() → return the top element
getMin() → return the minimum element in the stack
output
For each pop, top, and getMin operation, output the result on a new line.
push(5)
push(3)
push(7)
getMin()
pop()
top()
getMin()
Expected Output:
getMin() → 3
top()    → 7
getMin() → 5'''
#brute force
# create empty stack
stack = [] #initialize empty stack

def push(x):# 
    # add element to top of stack
    stack.append(x) #add element to stack

def pop():
    # remove top element
    if stack:
        stack.pop()#remove top element

def peek():
    # return top element
    if stack: #check if stack is not empty
        return stack[-1]#return top element
    return None#return None if stack is empty

def getMin():
    # return minimum element (brute force)
    if stack: #check if stack is not empty
        return min(stack)#return minimum element
    return None#return None if stack is empty
# Example usage:
push(5) #push 5 onto stack
push(3) #push 3 onto stack
push(7) #push 7 onto stack
print("getMin() →", getMin()) #print minimum element
pop() #pop top element
print("top()    →", peek()) #print top element
print("getMin() →", getMin()) #print minimum element
'''tc: O(1) for push, pop, peek operations because we are using list
O(n) for getMin operation because we are using min() function which takes linear time to find minimum element in the list
sc: O(n) for stack storage where n is the number of elements in the stack because we are using list to store
stack elements
'''
#optimized approach
class MinStack: #class MinStack
    def __init__(self):#constructor to initialize stack
        self.stack = []  # main stack to store elements
        self.min_stack = []  # auxiliary stack to store minimum elements

    def push(self, x):
        self.stack.append(x)  # push element onto main stack
        # push onto min_stack if it's empty or the new element is smaller or equal to the current minimum
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x) #push element onto min_stack

    def pop(self):#pop element from stack
        if self.stack:#check if stack is not empty
            top = self.stack.pop()  # pop element from main stack
            # if popped element is the current minimum, pop it from min_stack as well
            if top == self.min_stack[-1]:#check if popped element is minimum
                self.min_stack.pop() #pop from min_stack

    def peek(self): #peek at top element of stack
        if self.stack: #check if stack is not empty 
            return self.stack[-1]  # return top element of main stack
        return None  # return None if stack is empty

    def getMin(self):# get minimum element from stack
        if self.min_stack:#check if min_stack is not empty
            return self.min_stack[-1]  # return top element of min_stack (current minimum)
        return None  # return None if stack is empty
# Example usage:
min_stack = MinStack()  # create instance of MinStack
min_stack.push(5)  # push 5 onto stack
min_stack.push(3)  # push 3 onto stack
min_stack.push(7)  # push 7 onto stack
print("getMin() →", min_stack.getMin())  # print minimum element
min_stack.pop()  # pop top element
print("top()    →", min_stack.peek())  # print top element
print("getMin() →", min_stack.getMin())  # print minimum element
'''tc: O(1) for push, pop, peek, getMin operations because we are using list which supports append and pop operations in constant time
sc: O(n) for stack storage where n is the number of elements in the stack because we are using two lists to
store stack elements and minimum elements
'''
