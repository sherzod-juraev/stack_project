# Python Stack Implementation

A simple and fully functional **Stack** data structure implemented in Python using a **singly linked list**.  
This project demonstrates object-oriented programming, exception handling, and Pythonic features.

---

## Features

- **Push**: Add a new element to the top of the stack.
- **Pop**: Remove and return the top element of the stack.
- **Peek**: View the top element without removing it.
- **is_empty**: Check if the stack is empty.
- **clear**: Remove all elements from the stack.
- **to_list**: Convert the stack to a Python list.
- **Pythonic support**:
  - Iteration with `for` loops
  - Index access (`stack[i]`)
  - Membership check (`value in stack`)
  - `len(stack)` returns the number of elements
  - Pretty-print stack with `print(stack)`

---

## Installation

No external libraries required. Just clone this repository:
```bash
git clone https://github.com/your-username/python-stack.git

```
#Then, import the Stack class in your Python code:

from stack import Stack, StackIsEmpty

## Usage
```python
# Create a new stack
stack = Stack()

# Add elements
stack.push(10)
stack.push(20)
stack.push(30)

print(stack)  # Output: 30->20->10

# Peek the top element
print(stack.peek())  # Output: 30

# Pop elements
print(stack.pop())   # Output: 30
print(stack.pop())   # Output: 20

# Check if stack is empty
print(stack.is_empty())  # Output: False

# Convert to list
print(stack.to_list())  # Output: [10]

# Membership check
print(10 in stack)  # Output: True

# Clear the stack
stack.clear()
print(stack.is_empty())  # Output: True
```
License

This project is open-source and available under the MIT License.
