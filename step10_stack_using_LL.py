'''problem statement :The task is to implement a Stack data structure using a Linked List.
A stack is a linear data structure that follows the LIFO (Last In, First Out) principle, where elements are added and removed only from one end, called the top.
Instead of using an array, you must use a linked list to perform all stack operations.
push(10)
push(20)
push(30)
pop()
Before pop:
30 → 20 → 10 → NULL
After pop:
20 → 10 → NULL
'''
#brute force 
# Node of Linked List
class Node:#node class to create new nodes
    def __init__(self, data):#constructor to initialize node 
        self.data = data # data part of node
        self.next = None # pointer to next node


# Stack using Linked List
class Stack: #stack class to implement stack operations using linked list
    def __init__(self):#constructor to initialize stack
        self.top = None   # top of stack (head of linked list)

    # Push operation
    def push(self, x):# push element x onto stack
        new_node = Node(x)     # create new node
        new_node.next = self.top # link new node to previous top
        self.top = new_node  # update top to new node
    # Pop operation
    def pop(self):# remove and return top element of stack
        if self.top is None:# check if stack is empty
            print("Stack is empty")  
            return -1

        value = self.top.data # get top element's value
        self.top = self.top.next # update top to next node
        return value # return popped value

    # Peek operation
    def peek(self): # return top element without removing it
        if self.top is None: # check if stack is empty
            return -1 # stack is empty
        return self.top.data # return top element's value
    # Check if stack is empty
    def isEmpty(self): # return True if stack is empty, else False
        return self.top is None # check if top is None
    # Print stack elements
    def printStack(self): # print all elements in stack
        current = self.top # start from top
        while current: # traverse linked list
            print(current.data, end=" → ") # print current node's data
            current = current.next # move to next node
        print("NULL") # indicate end of stack
# Example usage:
if __name__ == "__main__":
    stack = Stack() # create a new stack

    stack.push(10) # push 10 onto stack
    stack.push(20) # push 20 onto stack
    stack.push(30) # push 30 onto stack

    print("Before pop:") 
    stack.printStack() # print stack before pop

    popped_value = stack.pop() # pop top element
    print(f"Popped value: {popped_value}") # print popped value

    print("After pop:") 
    stack.printStack() # print stack after pop
    
