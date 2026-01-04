# Push Operation in Stack

## What is Push?
**Push** is the operation used to **insert an element into a stack**.

- The element is always added at the **top of the stack**.
- Stack follows **LIFO (Last In First Out)**.

---

## Rules of Push Operation
- Insertion is allowed **only at the top**.
- Insertion in the middle or bottom is **not allowed**.
- If the stack is full, push cannot be performed.

---

## Steps Involved in Push
1. Check whether the stack is full (**overflow condition**).
2. If space is available, insert the element at the top.
3. Update the top pointer to the new element.

---

## Example

Initial Stack:

---

## Push Operation Code (Python)

```python
stack = []

stack.append(10)   # push
stack.append(20)
stack.append(30)

print(stack)
# Pop Operation in Stack

## What is Pop?
**Pop** is the operation used to **remove the top element from the stack**.

- Removal happens **only from the top**.
- Stack follows **LIFO (Last In First Out)**.

---

## Rules of Pop Operation
- Deletion is allowed **only at the top**.
- If the stack is empty, pop cannot be performed.
- Removing from middle or bottom is **not allowed**.

---

## Steps Involved in Pop
1. Check whether the stack is empty (**underflow condition**).
2. If not empty, remove the top element.
3. Update the top pointer to the next element.

---

## Example

Initial Stack:

---

## Pop Operation Code (Python)

```python
stack = [10, 20, 30]

stack.pop()   # removes 30
stack.pop()   # removes 20

print(stack)  # [10]
# Peek (Top) Operation in Stack

## What is Peek?
**Peek** (also called **Top**) is the operation used to **view the top element of the stack without removing it**.

- The stack remains **unchanged**.
- Only the value at the top is returned.

---

## Rules of Peek Operation
- Peek accesses **only the top element**.
- If the stack is empty, peek cannot be performed.
- No insertion or deletion happens.

---

## Steps Involved in Peek
1. Check whether the stack is empty.
2. If not empty, return the top element.
3. Do not remove the element.

---

## Example

Stack:
(Stack remains the same)

---

## Peek Operation Code (Python)

```python
stack = [10, 20, 30]

top = stack[-1]   # peek
print(top)        # 30
# isEmpty and isFull Operations in Stack

---

## isEmpty Operation

### What is isEmpty?
**isEmpty** checks whether the stack has **no elements**.

- Returns **true** if stack is empty
- Returns **false** if stack has at least one element

---

### Why is isEmpty Needed?
- To avoid **stack underflow**
- Used before performing **pop** or **peek**

---

### Example

Empty Stack:

isEmpty → **true**

---

### Python Code

```python
stack = []

if not stack:
    print("Stack is empty")
