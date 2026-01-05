'''reverse a string using a stack
explanation: push each character of the string onto the stack,
then pop characters off to get them in reverse order.
example: "hello" -> "olleh"
'''
#brute force approach using list as stack
def reverse_string(s): #reverse string s using stack
    stack = []          # step 1: create empty stack
    reversed_str = ""   # to store reversed string

    # step 2: push each character into stack
    for ch in s:# iterate through each character in string
        stack.append(ch)# push character onto stack

    # step 3: pop characters from stack and build reversed string
    while stack: # while stack is not empty
        reversed_str += stack.pop() # pop from stack and append to reversed_str

    return reversed_str # return the reversed string
# Example usage:
input_str = "hello" # original string
reversed_str = reverse_string(input_str) # reverse the string
print(f"Original String: {input_str}") # print original string
print(f"Reversed String: {reversed_str}") # print reversed string
# Output:
# Original String: hello
# Reversed String: olleh

def reverse_string(s): # reverse string s in place using two-pointer technique
    # convert string to list (strings are immutable in Python)
    chars = list(s) # convert string to list of characters

    left = 0 # left pointer
    right = len(chars) - 1 # right pointer with last index

    while left < right: # continue until pointers meet
        # swap characters
        chars[left], chars[right] = chars[right], chars[left] # swap characters at left and right pointers
        left += 1 # move left pointer right
        right -= 1 # move right pointer left
    return "".join(chars) # convert list back to string and return
# Example usage:
input_str = "world" # original string
reversed_str = reverse_string(input_str) # reverse the string
print(f"Original String: {input_str}") # print original string
print(f"Reversed String: {reversed_str}") # print reversed stri
'''TC: O(n) for both approaches, SC: O(n) for first approach, O(1) for second approach
'''
