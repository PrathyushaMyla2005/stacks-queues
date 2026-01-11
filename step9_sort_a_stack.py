'''problem statement:Your task is to sort a stack such that the smallest elements are on the top.
A stack is a linear data structure that follows the Last In First Out (LIFO) principle, which means:
Elements can be inserted (push) only at the top
Elements can be removed (pop) only from the top
Because of this restriction, sorting must be done using only stack operations.
Definition of Sorted Stack: A stack is considered sorted if for every pair of adjacent elements, the top element is less than or equal to the element below it.
Example 1:
Input: Stack = [3, 1, 4, 2]
Output: Sorted Stack = [1, 2, 3, 4]
Example 2:
Input: Stack = [5, 2, 8, 1, 3]
Output: Sorted Stack = [1, 2, 3, 5, 8]'''
#brute force approach
def sortStack_bruteforce(stack):
    # Step 1: take elements out of stack
    temp = [] # temporary array to hold stack elements

    while stack: # while stack is not empty
        temp.append(stack.pop()) # pop elements from stack and add to temp array

    # Step 2: sort the array
    temp.sort()

    # Step 3: push elements back into stack
    for num in temp: # iterate through sorted array
        stack.append(num) # push elements back into stack

    return stack # return sorted stack
# Example usage:
stack = [3, 1, 4, 2] # example stack
sorted_stack = sortStack_bruteforce(stack) # sort the stack
print(f"Sorted Stack (Brute Force): {sorted_stack}") # print sorted stack
'''TC: O(n log n) for sorting the array, SC: O(n) for temporary array'''
#OPTIMIZED APPROACH
def sortStack_optimized(stack): # function to sort stack using another stack
    tempStack = [] # temporary stack to hold sorted elements

    # Step 1–4: Insert elements in sorted order
    while stack: # while original stack is not empty
        current = stack.pop() # pop top element from original stack

        # Move larger elements back to original stack
        while tempStack and tempStack[-1] > current: # while tempStack is not empty and top of tempStack is greater than current
            stack.append(tempStack.pop()) # pop from tempStack and push back to original stack

        tempStack.append(current) # push current element to tempStack

    # Step 5: Move back to original stack
    while tempStack: # while tempStack is not empty
        stack.append(tempStack.pop()) # pop from tempStack and push back to original stack

    return stack # return sorted stack
# Example usage:
stack = [5, 2, 8, 1, 3] # example stack
sorted_stack = sortStack_optimized(stack) # sort the stack
print(f"Sorted Stack (Optimized): {sorted_stack}") # print sorted stack
'''TC: O(n^2) in worst case for nested while loops, SC: O(n) for temporary stack'''
    