class StackIsEmpty(Exception):
    def __init__(self, *args):
        self.args = list(args)
    
    def __str__(self):
        return f'{" | ".join(str(info) for info in self.args)}'

class Stack:
    
    class __Node:
        
        def __init__(self, value):
            self.value = value
            self.next = None
            
    def __init__(self, head = None, /):
        
        self.__head = None
        self.__length = 0
        if head:
            self.__head = Stack.__Node(head)
            self.__length += 1
    
    def __len__(self):
        """stack length"""
        return self.__length
    
    def __repr__(self):
        
        if self.__length == 0:
            return 'Stack is empty'
        current = self.__head
        result = ''
        while current:
            result += f'{current.value:^3}'
            if current.next:
                result += '->'
            current = current.next
        return result
    
    def __iter__(self):
        """
        for use in the for operator
        """
        self.__current = self.__head
        return self
    
    def __next__(self):
        
        if self.__current:
            value, self.__current = self.__current.value, self.__current.next
            return value
        else:
            raise StopIteration
    
    def __getitem__(self, index):
        
        index = self.__normalize_index(index)
        for i, value in enumerate(self):
            if index == i:
                return value
    
    def __setitem__(self, index, value):
        
        index = self.__normalize_index(index)
        current = self.__head
        for i in range(self.__length):
            if index == i:
                current.value = value
                break
            current = current.next
    
    def __contains__(self, value):
        
        for stack_value in self:
            if stack_value == value:
                return True
        return False
    
    def __normalize_index(self, index, /) -> int:
        """index normalization"""
        if not isinstance(index, int):
            raise ValueError(f'index must be of type int not {type(index)}')
        index = (self.__length + index) if index < 0 else index
        if index >= self.__length:
            raise IndexError('reference beyond stack length')
        return index
    
    def is_empty(self):
        """
        Checks whether the stack is empty. True if empty, False otherwise.
        """
        if self.__length:
            return False
        return True
    
    def push(self, value, /):
        """
        adds a new element
        takes a new element as the last element of the stack
        """
        new_node = Stack.__Node(value)
        new_node.next = self.__head
        self.__head = new_node
        self.__length += 1
    
    def pop(self):
        """
        Removes and returns the last element from the stack
        """
        if self.is_empty():
            raise StackIsEmpty('Stack is empty')
        current = self.__head
        self.__head = self.__head.next
        self.__length -= 1
        return current.value
    
    def peek(self):
        """
        Returns the top element of the stack, but does not remove it
        """
        if self.is_empty():
            raise StackIsEmpty('Stack is empty')
        return self.__head.value
    
    def clear(self):
        """Completely empty the stack"""
        self.__head = None
        self.__length = 0
    
    def to_list(self):
        """convert stack to list"""
        return [value for value in self]