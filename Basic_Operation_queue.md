# Enqueue Operation in Queue

## What is Enqueue?
**Enqueue** is the operation used to **insert an element into a queue**.

- The element is always added at the **rear (end)** of the queue.
- Queue follows **FIFO (First In First Out)**.

---

## Rules of Enqueue Operation
- Insertion is allowed **only at the rear**.
- Insertion at the front or middle is **not allowed**.
- If the queue is full (fixed size), enqueue cannot be performed.

---

## Steps Involved in Enqueue
1. Check whether the queue is full (**overflow condition**).
2. If space is available, insert the element at the **rear**.
3. Move the rear pointer forward.

---

## Example

Initial Queue:
---

## Enqueue Operation Code (Python using deque)

```python
from collections import deque

queue = deque()

queue.append(10)   # enqueue
queue.append(20)
queue.append(30)

print(queue)
# Dequeue Operation in Queue

## What is Dequeue?
**Dequeue** is the operation used to **remove an element from a queue**.

- The element is always removed from the **front** of the queue.
- Queue follows **FIFO (First In First Out)**.

---

## Rules of Dequeue Operation
- Deletion is allowed **only at the front**.
- Removal from rear or middle is **not allowed**.
- If the queue is empty, dequeue cannot be performed.

---

## Steps Involved in Dequeue
1. Check whether the queue is empty (**underflow condition**).
2. If not empty, remove the element from the **front**.
3. Move the front pointer forward.

---

## Example

Initial Queue:

---

## Dequeue Operation Code (Python using deque)

```python
from collections import deque

queue = deque([10, 20, 30])

queue.popleft()   # removes 10
queue.popleft()   # removes 20

print(queue)      # deque([30])

# Front (Peek) Operation in Queue

## What is Front / Peek?
**Front (Peek)** is the operation used to **view the first element of the queue without removing it**.

- The queue remains **unchanged**.
- Only the element at the **front** is accessed.

---

## Rules of Front Operation
- Front operation accesses **only the front element**.
- No insertion or deletion happens.
- If the queue is empty, front cannot be performed.

---

## Steps Involved in Front
1. Check whether the queue is empty.
2. If not empty, return the front element.
3. Do not remove the element.

---

## Example

Queue:
(Queue remains the same)

---

## Front Operation Code (Python using deque)

```python
from collections import deque

queue = deque([10, 20, 30])

front_element = queue[0]
print(front_element)   # 10
# isEmpty and isFull Operations in Queue

---

## isEmpty Operation

### What is isEmpty?
**isEmpty** checks whether the queue has **no elements**.

- Returns **true** if queue is empty  
- Returns **false** if queue has elements  

---

### Why is isEmpty Needed?
- To avoid **queue underflow**
- Used before performing **dequeue** or **front**

---

### Example

Empty Queue:

isEmpty → **true**

---

### Python Code

```python
from collections import deque

queue = deque()

if not queue:
    print("Queue is empty")

