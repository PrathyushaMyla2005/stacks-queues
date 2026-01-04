# 🎯 Stack & Queue – Interview Questions and Answers

This section covers **common interview questions** asked on **Stacks and Queues**, with **clear and beginner-friendly answers**.

---

## 🧱 STACK – Interview Questions

### Q1. What is a Stack?
**Answer:**  
A Stack is a linear data structure that follows the **Last In First Out (LIFO)** principle.  
The element inserted last is removed first.

---

### Q2. Give real-life examples of Stack.
**Answer:**
- Stack of plates  
- Undo / Redo operations  
- Browser back button  
- Function calls (Call Stack)

---

### Q3. What are the basic operations of a Stack?
**Answer:**
- **push(x)** – Insert element  
- **pop()** – Remove top element  
- **peek()** – View top element  
- **isEmpty()** – Check if empty  

---

### Q4. How do you implement a Stack?
**Answer:**
A Stack can be implemented using:
- Array / List  
- Linked List  

In Python, we commonly use a **list** with `append()` and `pop()`.

---

### Q5. What is stack overflow and stack underflow?
**Answer:**
- **Stack Overflow:** Trying to push an element when the stack is full.  
- **Stack Underflow:** Trying to pop an element from an empty stack.

---

### Q6. Where are stacks used in real applications?
**Answer:**
- Expression evaluation  
- Function calls (Recursion)  
- Backtracking (DFS)  
- Parenthesis checking  

---

### Q7. Explain the Valid Parentheses problem.
**Answer:**  
We use a stack to store opening brackets.  
For every closing bracket, we check whether the top of the stack has a matching opening bracket.  
If mismatch occurs or stack is empty, the string is invalid.

---

### Q8. What is the time complexity of stack operations?
**Answer:**
- Push → **O(1)**  
- Pop → **O(1)**  
- Peek → **O(1)**  

---

## 🚶‍♂️ QUEUE – Interview Questions

### Q9. What is a Queue?
**Answer:**  
A Queue is a linear data structure that follows the **First In First Out (FIFO)** principle.  
The element inserted first is removed first.

---

### Q10. Give real-life examples of Queue.
**Answer:**
- People standing in a line  
- Ticket booking systems  
- CPU scheduling  
- Printer queue  

---

### Q11. What are the basic operations of a Queue?
**Answer:**
- **enqueue(x)** – Insert element at rear  
- **dequeue()** – Remove element from front  
- **front()** – View front element  
- **isEmpty()** – Check if empty  

---

### Q12. How do you implement a Queue?
**Answer:**
A Queue can be implemented using:
- Array  
- Linked List  
- **Deque (recommended in Python)**

---

### Q13. Why is deque preferred over list for Queue?
**Answer:**  
In Python, removing from the front of a list takes **O(n)** time,  
whereas `deque.popleft()` works in **O(1)** time.

---

### Q14. Where are queues used?
**Answer:**
- Breadth First Search (BFS)  
- Scheduling algorithms  
- Task processing systems  

---

### Q15. Difference between Stack and Queue.

| Stack | Queue |
|-----|------|
| LIFO | FIFO |
| Insert & delete at same end | Insert at rear, delete at front |
| Used in DFS, recursion | Used in BFS, scheduling |

---

## 🔥 Tricky Interview Questions

### Q16. Can you implement Stack using Queue?
**Answer:**  
Yes. We can implement Stack using one or two Queues by adjusting the order of insertion so that the last inserted element comes out first.

---

### Q17. Can you implement Queue using Stack?
**Answer:**  
Yes. By using two stacks:
- One for input  
- One for output  
This helps maintain FIFO order.

---

## ✅ Final Interview Tip
Always explain:
1. **Definition**
2. **Logic**
3. **Time & Space Complexity**
4. **Real-life use case**

---

✨ End of Interview Notes ✨
