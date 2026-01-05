'''problem statement:you are given a string s that consists of:
Lowercase English letters (a to z)
Opening parentheses '('Closing parentheses ')'
The string is valid, meaning:Every '(' has a matching ')'Parentheses are properly nested
Your task is to reverse the substrings enclosed within each pair of matching parentheses, starting from the innermost pair. The final result should not contain any parentheses.
Example 1:
Input: s = "(abcd)"
Output: "dcba"
Example 2:
Input: s = "(u(love)i)"
Output: "iloveu"
Example 3:
Input: s = "(ed(et(oc))el)"
Output: "leetcode"'''
#brute force approach using stack
def reverse_parentheses(s): # reverse substrings within parentheses
    stack = []          # step 1: create empty stack
    current_str = ""    # to store current substring

    for ch in s: # iterate through each character in string
        if ch == '(': # if opening parenthesis
            stack.append(current_str) # push current substring onto stack
            current_str = ""           # reset current substring
        elif ch == ')': # if closing parenthesis
            # pop from stack and reverse current substring
            current_str = stack.pop() + current_str[::-1] # concatenate reversed substring
        else:
            current_str += ch # add character to current substring

    return current_str # return the final processed string
# Example usage:
input_str = "(u(love)i)" # original string
reversed_str = reverse_parentheses(input_str) # reverse substrings within parentheses
print(f"Original String: {input_str}") # print original string
print(f"Reversed String: {reversed_str}") # print reversed string
'''TC: O(n^2) in worst case due to string concatenation inside loop, SC: O(n) for stack storage
'''
#optimized approach using list as stack
def reverse_parentheses_optimized(s): # reverse substrings within parentheses
    stack = []          # step 1: create empty stack
    current_str = []    # to store current substring as list

    for ch in s: # iterate through each character in string
        if ch == '(': # if opening parenthesis
            stack.append(current_str) # push current substring onto stack
            current_str = []           # reset current substring
        elif ch == ')': # if closing parenthesis
            # pop from stack and reverse current substring
            current_str = stack.pop() + current_str[::-1] # concatenate reversed substring
        else:
            current_str.append(ch) # add character to current substring

    return "".join(current_str) # return the final processed string
# Example usage:
input_str = "(ed(et(oc))el)" # original string
reversed_str = reverse_parentheses_optimized(input_str) # reverse substrings within parentheses
print(f"Original String: {input_str}") # print original string
print(f"Reversed String: {reversed_str}") # print reversed string
'''TC: O(n) for optimized approach, SC: O(n) for stack storage'''