'''problem statement:Your task is to delete the middle element of the stack while preserving the order of the remaining elements.
A stack is a linear data structure that follows the Last In First Out (LIFO) principle, which means:
Elements can be inserted (push) only at the top
Elements can be removed (pop) only from the top
Because of this restriction, the middle element cannot be accessed directly.
Definition of Middle Element:Let N be the total number of elements in the stack.
If N is odd, the middle element is at position N / 2
If N is even, the element at position N / 2 (0-based indexing) is considered the middle
Example 1:
Input: Stack = [1, 2, 3, 4, 5]
Output: Stack after deleting middle element = [1, 2, 4, 5]
Example 2:
Input: Stack = [1, 2, 3, 4, 5, 6]
Output: Stack after deleting middle element = [1, 2, 4, 5, 6]'''
def deleteMiddle(stack, n):# function to delete middle element of stack
    """
    Deletes the middle element of the stack.
    stack : list (used as stack)
    n     : total number of elements in stack
    """

    # Helper recursive function
    def solve(stack, current, middle):
        # Base case: when we reach the middle
        if current == middle:# if current index is middle index
            stack.pop()   # remove middle element
            return # return to previous call

        # Store top element
        top = stack.pop()

        # Recursive call
        solve(stack, current + 1, middle)

        # Push back the element (except middle)
        stack.append(top)

    middle = n // 2 # calculate middle index
    solve(stack, 0, middle)# call helper function to delete middle element
    return stack # return modified stack
# Example usage:
stack = [1, 2, 3, 4, 5] # example stack
n = len(stack) # get number of elements in stack
modified_stack = deleteMiddle(stack, n) # delete middle element
print(f"Stack after deleting middle element: {modified_stack}") # print modified stack
'''TC: O(n) for traversing the stack once, SC: O(n) for recursion stack in worst case'''
#OPTIMIZED APPROACH
def deleteMiddle(stack, n):
    # Helper recursive function
    def removeMiddle(stack, count):
        # Base case: middle reached
        if count == n // 2: # if current index is middle index
            stack.pop() # remove middle element
            return # return to previous call
        
        # Remove top element
        temp = stack.pop()
        
        # Recursive call
        removeMiddle(stack, count + 1)
        
        # Push element back
        stack.append(temp)

    removeMiddle(stack, 0)# call helper function to delete middle element
    return stack # return modified stack
# Example usage:
stack = [1, 2, 3, 4, 5, 6] # example stack
n = len(stack) # get number of elements in stack
modified_stack = deleteMiddle(stack, n) # delete middle element
print(f"Stack after deleting middle element: {modified_stack}") # print modified stack
'''TC: O(n) for traversing the stack once, SC: O(n) for recursion stack in worst case'''
