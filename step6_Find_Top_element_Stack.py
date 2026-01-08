'''problem statement:Problem Statement
You are given a stack data structure that stores elements.
Your task is to find the top element of the stack.
The top element is defined as the element that was most recently inserted into the stack.
You must return the top element without removing it from the stack.
Special Condition:If the stack is empty, there is no top element.In such a case, return -1.
example 1:
Input: stack = [5, 10, 15]
Output: 15'''
#brute force approach
def find_top_element(stack): # function to find top element of stack
    if not stack: # check if stack is empty
        return -1 # return -1 if empty
    return stack[-1] # return the last element as top element
# Example usage:
stack = [5, 10, 15] # example stack
top_element = find_top_element(stack) # find top element
print(f"Top Element: {top_element}") # print top element
'''TC: O(1) for accessing last element, SC: O(1)'''
