'''problem statement: Implement a correctly balanced parentheses checker using a stack data structure.
A string containing various types of parentheses is considered balanced if:
1. Every opening parenthesis has a corresponding closing parenthesis of the same type.
2. Parentheses are closed in the correct order.
Example 1:
Input: s = "{[()]}"
Output: True
Example 2:
Input: s = "{[(])}"
Output: False'''
#brute force approach using stack
def is_balanced_parentheses(s): # function to check balanced parentheses
    changed = True # flag to track changes why we use changed: to keep removing pairs until no more can be removed
    while changed: # continue until no more changes
        changed = False # reset flag
        if '()' in s: # check for ()
            s = s.replace('()', '') # remove ()
            changed = True # set flag
        if '{}' in s: # check for {}
            s = s.replace('{}', '') # remove {}
            changed = True # set flag
        if '[]' in s: # check for []
            s = s.replace('[]', '') # remove []
            changed = True # set flag
    return s == '' # if string is empty, parentheses are balanced
# Example usage:
input_str = "{[()]}" # example input
balanced = is_balanced_parentheses(input_str) # check if balanced
print(f"Is Balanced: {balanced}") # print result
'''TC: O(n^2) in worst case due to repeated string replacements, SC: O(1)'''
def checkBalancedParentheses(s):
    while True: # keep removing pairs until no more can be removed
        new_s = s.replace("()", "").replace("{}", "").replace("[]", "") # remove all pairs
        
        if new_s == s:   # no change happened
            break # exit loop
        
        s = new_s # update string

    return s == "" # if string is empty, parentheses are balanced
# Example usage:
input_str = "{[(])}" # example input
balanced = checkBalancedParentheses(input_str) # check if balanced
print(f"Is Balanced: {balanced}") # print result
'''TC: O(n^2) in worst case due to repeated string replacements, SC: O(1)'''
#optimized approach using stack
def is_balanced_parentheses_optimized(s): # function to check balanced parentheses
    stack = [] # initialize empty stack
    mapping = {')': '(', '}': '{', ']': '['} # mapping of closing to opening parentheses
    for char in s: # iterate through each character in string
        if char in mapping.values(): # if it's an opening parenthesis
            stack.append(char) # push onto stack
        elif char in mapping.keys(): # if it's a closing parenthesis
            if not stack or stack[-1] != mapping[char]: # check for matching opening parenthesis example: for '}', check if top of stack is '{' without removing it

                return False # not balanced 
            stack.pop() # pop the matching opening parenthesis

    return len(stack) == 0 # if stack is empty, parentheses are balanced
# Example usage:
input_str = "{[()]}" # example input
balanced = is_balanced_parentheses_optimized(input_str) # check if balanced
print(f"Is Balanced: {balanced}") # print result
'''TC: O(n) for single pass through string, SC: O(n) for stack storage'''

