from dataclasses import dataclass

@dataclass
class Stack:
    stack: list
    max_size: int  # this is the user defined max length of self.stack

    def is_empty(self):
        return "stack is empty" if len(self.stack) == 0 else "stack is not empty"
    
    def is_full(self):
        return "stack is full" if len(self.stack) == self.max_size else "stack is not full"

    def peek(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            print("cannot peek from an empty stack")

    def push_to_stack(self, data):
        if len(self.stack) < self.max_size:
            self.stack.append(data)
            print(f"{data} has been pushed to the stack!")
        else:
            print("Stack is at its maximum size. You cannot add any more elements")

    def pop_from_stack(self):
        if len(self.stack) > 0:
            last_item = self.stack[-1]
            self.stack.pop()  # this will remove the top item in the stack and print it
            print("popped " + last_item)
        else:
            print("Cannot pop from an empty stack. would cause an underflow")

def main():
    my_stack = Stack([], 5)

    # can use object's class and method and pass object as parameter
    # print(Stack.is_empty(my_stack))
    # print()

    # can also use object and parameter together directly
    print(my_stack.is_empty())
    print()

    # perform method on my_stack

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

    print("trying to add 'sixth' to stack.")
    my_stack.push_to_stack("sixth")
    print(my_stack.stack)
    print()

    print("stack is full?")
    print(my_stack.is_full())
    print()

    print("aobut to pop")
    my_stack.pop_from_stack()
    print("stack now: ", my_stack)

    print()
    print("about to peek the stack")
    print("top item in the stack:")
    print(my_stack.peek())


    for i in range(len(my_stack.stack)):
        my_stack.pop_from_stack()
    print("stack now: " + str(my_stack.stack))

    print("trying to pop from stack now")
    my_stack.pop_from_stack()

    print("\ntrying to peek the stack")
    my_stack.peek()

    print("\nis stack empty?")
    print(my_stack.is_empty())


if __name__ == '__main__':
    main()
