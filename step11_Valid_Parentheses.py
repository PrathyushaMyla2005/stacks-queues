'''problem statement: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false
'''
#optimal force approach using stack
def isvalid(str): #function to check valid parentheses
    stack = []   #initialize empty stack
    mapping = {')': '(', '}': '{', ']': '['} #mapping of closing and opening brackets
    for char in str:  #iterate through each character in the string
        if char in mapping:  #if character is a closing bracket
            top_element = stack.pop() if stack else '#'  #pop the top element from stack or assign '#' if stack is empty
            if mapping[char] != top_element:  #check if the popped element matches the corresponding opening bracket
                return False  #if not matching, return False
        else:
            stack.append(char)  #if character is an opening bracket, push it onto the stack
    return not stack  #if stack is empty, all brackets are matched, return True
#test cases
print(isvalid("()"))        #True
print(isvalid("()[]{}"))    #True
print(isvalid("(]"))       #False   
'''time complexity: O(n) where n is the length of the string
space complexity: O(n) in the worst case when all characters are opening brackets'''
#brute force approach using stack
def isValid(str): #function to check valid parentheses
    s = str #copy input string to s
    prev = "" #initialize previous string as empty

    # Keep removing valid pairs until no more changes
    while prev != str: #loop until no more valid pairs can be removed
        prev = str #update previous string
        s = s.replace("()", "")#remove all occurrences of valid parentheses pairs
        s = s.replace("{}", "")#   remove all occurrences of valid curly braces pairs
        s = s.replace("[]", "")#    remove all occurrences of valid square brackets pairs

    # If empty, parentheses are valid
    return s == "" #return True if string is empty, else False
#test cases
print(isValid("()"))        #True
'''time complexity: O(n^2) in the worst case due to repeated string replacements
space complexity: O(n) for storing the modified string'''
