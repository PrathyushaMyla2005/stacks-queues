'''Problem Statement:
You are given an integer array arr[].
For every element arr[i], find the Next Greater Element (NGE) on its right side.
✅ Next Greater Element (NGE) means
The first element that appears to the right of arr[i] and is strictly greater than arr[i].
If such an element exists → return that value
If no greater element exists on the right → return -1
✅ Example
Input:
arr = [4, 5, 2, 25]
Output:
[5, 25, 25, -1]
Explanation:
For 4 → next greater is 5
for 5 → next greater is 25
For 2 → next greater is 25
For 25 → no greater element on right → -1'''
#brute force approach
def next_greater_element(arr):  
    # This function finds the Next Greater Element for every element in the array

    n = len(arr)  
    # n stores the total number of elements in the array

    result = [-1] * n  
    # Create a result list of size n
    # Initially fill it with -1 because if no greater element exists, answer is -1

    for i in range(n):  
        # Outer loop: pick each element one by one (arr[i])

        for j in range(i + 1, n):  
            # Inner loop: check elements to the right side of arr[i]
            # Start from i+1 because we only look on the right

            if arr[j] > arr[i]:  
                # If we find a greater element than arr[i]

                result[i] = arr[j]  
                # Store that greater element in result for position i

                break  
                # Stop searching because we need the FIRST greater element only

    return result  
    # Finally return the result list containing next greater elements


# Example input array
arr = [4, 5, 2, 25]

# Calling the function and printing the output
print(next_greater_element(arr))
'''time complexity: O(n^2) because of nested loops
space complexity: O(1) as we are not using any extra space except for result array'''
#optimal approach
def next_greater_element(arr):
    n = len(arr)                 # size of array
    result = [-1] * n            # default answer is -1
    stack = []                   # stack will store elements (or indexes)

    for i in range(n - 1, -1, -1):   # traverse from right to left
        
        # Remove all elements from stack that are <= current element
        # because they cannot be the next greater for current element
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        # If stack is not empty, top element is the next greater element
        if stack:
            result[i] = stack[-1]

        # Push current element into stack for future elements (left side)
        stack.append(arr[i])

    return result                # return final next greater array


# Example
arr = [4, 5, 2, 25]
print(next_greater_element(arr))
'''time complexity: O(n) because each element is pushed and popped at most once
space complexity: O(n) for the stack in the worst case
'''
