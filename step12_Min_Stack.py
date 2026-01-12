'''problem statement:min stack problem is to design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example 1:
Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]
Output
[null,null,null,null,-3,null,0,-2]
Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
example 2:
input :[10,20,5,15,2]
minstack.push(10)
minstack.push(20)
minstack.push(5)
minstack.push(15)
minstack.push(2)
minstack.getMin() -> 2
minstack.pop()
minstack.getMin() -> 5
'''
#brute force approach using stack
class MinStack:#class to implement min stack
    def __init__(self): #constructor to initialize stack
        self.stack = [] #initialize empty stack

    def push(self, x): #function to push element onto stack
        self.stack.append(x) #append element to stack

    def pop(self): #function to pop element from stack
        if self.stack: #check if stack is not empty
            self.stack.pop() #pop the top element from stack

    def top(self): #function to get top element of stack
        if self.stack: #check if stack is not empty
            return self.stack[-1] #return the top element of stack

    def getMin(self): #function to get minimum element from stack
        if self.stack: #check if stack is not empty
            return min(self.stack) #return the minimum element in the stack
#test cases
minstack = MinStack() #create an instance of MinStack
minstack.push(-2) #push -2 onto stack
minstack.push(0)  #push 0 onto stack
minstack.push(-3) #push -3 onto stack
print(minstack.getMin()) #return minimum element -> -3
minstack.pop() #pop the top element from stack
print(minstack.top())    #return top element -> 0
print(minstack.getMin()) #return minimum element -> -2
'''time complexity: O(n) for getMin() due to min() function, O(1) for all other operations'''
#optimal force approach using stack
class MinStackOpt:#class to implement optimal min stack
    def __init__(self): #constructor to initialize stack
        self.stack = [] #initialize empty stack
        self.min_stack = [] #initialize empty min stack to keep track of minimum elements

    def push(self, x): #function to push element onto stack
        self.stack.append(x) #append element to stack
        #push onto min_stack if it's empty or the new element is smaller or equal to the current minimum
        if not self.min_stack or x <= self.min_stack[-1]: 
            self.min_stack.append(x) #append element to min stack

    def pop(self): #function to pop element from stack
        if self.stack: #check if stack is not empty
            top_element = self.stack.pop() #pop the top element from stack
            #if the popped element is the current minimum, pop it from min_stack as well
            if top_element == self.min_stack[-1]: 
                self.min_stack.pop() 

    def top(self): #function to get top element of stack
        if self.stack: #check if stack is not empty
            return self.stack[-1] #return the top element of stack

    def getMin(self): #function to get minimum element from stack
        if self.min_stack: #check if min_stack is not empty
            return self.min_stack[-1] #return the top element of min_stack which is the minimum element
#test cases
minstack_opt = MinStackOpt() #create an instance of MinStackOpt
minstack_opt.push(-2) #push -2 onto stack
minstack_opt.push(0)  #push 0 onto stack
minstack_opt.push(-3) #push -3 onto stack
print(minstack_opt.getMin()) #return minimum element -> -3
minstack_opt.pop() #pop the top element from stack
print(minstack_opt.top())    #return top element -> 0
print(minstack_opt.getMin()) #return minimum element -> -2
'''time complexity: O(1) for all operations
space complexity: O(n) in the worst case when all elements are pushed onto min_stack'''
