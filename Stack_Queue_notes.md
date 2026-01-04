# 📚 Stack and Queue – DSA Notes (Beginner Friendly)

These notes cover the **Stack** and **Queue** data structures with:
- Simple definitions
- Real-life examples
- Operations
- Code (Python)
- Interview points

---

## 🧱 STACK (LIFO – Last In First Out)

### 🔹 What is a Stack?
A **Stack** is a linear data structure that follows the principle:

> **Last In, First Out (LIFO)**

👉 The element added last will be removed first.

### 🔹 Real-Life Example
- Stack of plates 🍽️
- Undo/Redo in text editors
- Browser back button

---

### 🔹 Stack Operations

| Operation | Description |
|---------|-------------|
| push(x) | Insert element at top |
| pop() | Remove top element |
| peek() | Get top element |
| isEmpty() | Check if stack is empty |

---

### 🔹 Stack Implementation (Using Python List)

```python
stack = []

stack.append(10)   # push
stack.append(20)
stack.append(30)

stack.pop()        # removes 30
top = stack[-1]    # peek element
🚶‍♂️ QUEUE (FIFO – First In First Out)
🔹 What is a Queue?

A Queue is a linear data structure that follows:

First In, First Out (FIFO)

👉 The element added first will be removed first.

🔹 Real-Life Example

People standing in a line 🧍‍♂️🧍‍♀️

Ticket booking counters

CPU scheduling

🔹 Queue Operations
Operation	Description
enqueue(x)	Insert element at rear
dequeue()	Remove element from front
front()	Get first element
isEmpty()	Check empty
🔹 Queue Implementation (Using deque)
from collections import deque

queue = deque()

queue.append(10)      # enqueue
queue.append(20)
queue.append(30)

queue.popleft()       # dequeue → removes 10
front = queue[0]      # front element

🎯 Interview Tips

Stack is used for expression evaluation, recursion, backtracking

Queue is used in BFS, task scheduling

Always mention time & space complexity