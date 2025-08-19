from stack import Stack

stacks = Stack()
for i in range(10):
    stacks.push(i)
print(stacks)
print(stacks.pop())
print(stacks)
print(stacks.is_empty())
