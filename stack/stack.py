from dataclasses import dataclass

@dataclass
class Stack:
    stack: list
    max_size: int # this is the user defined max length of self.stack

    def is_empty(self):
        return "stack is empty" if len(self.stack) == 0 else "stack is not empty"
    
    def is_full(self):
        return "stack is full" if len(self.stack) == self.max_size else "stack is not full"

    def peek(self):
        return self.stack[-1]
    
    def push_to_stack(self, data):
        if len(self.stack) < self.max_size:
            self.stack.append(data)
            print(f"{data} has been pushed to the stack!")
        else:
            print("Stack is at its maximum size. You cannot add any more elements")

    def pop_from_stack(self):
        self.stack.pop() # this will remove the top item in the stack and print it

my_stack = Stack([], 5)

# can use object's class and method and pass object as parameter 
# print(Stack.is_empty(my_stack))
# print()

# can also use object and parameter together directly
print(my_stack.is_empty())
print()

# perform method on my_stack
my_stack.push_to_stack("first")
print(my_stack.stack) # use dot syntax to see my_stack personal stack value
print()

print(my_stack.is_full())
print()

my_stack.push_to_stack("second")
print(my_stack.stack)
print()

my_stack.push_to_stack("third")
print(my_stack.stack)
print()

my_stack.push_to_stack("fourth")
print(my_stack.stack)
print()

my_stack.push_to_stack("fifth")
print(my_stack.stack)
print()

my_stack.push_to_stack("sixth")
print(my_stack.stack)
print()

print(my_stack.is_full())
print()

my_stack.pop_from_stack()
print("pop!\n")

print(my_stack.peek())
