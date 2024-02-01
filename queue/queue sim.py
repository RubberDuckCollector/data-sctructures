from dataclasses import dataclass

class Queue:
    def __init__(self, queue, max_length):
        self.__queue = []
        self.__max_length = max_length

    def get_queue(self):
        return self.__queue
    
    def get_max_length(self):
        return self.__max_length
    
    def set_max_length(self, x):
        self.__max_length = x
    
    def en_queue(self, x):
        if len(self.__queue) < self.__max_length:
            self.__queue.append(x)
            print(f"{x} added to end of queue")
        else:
            print(f"Queue is at max capacity, cannot add '{x}'")
    
    def de_queue(self):
        if len(self.__queue) != 0:
            first_element = self.__queue[0]
            self.__queue.remove(self.__queue[0])
            print(f"{first_element} removed!")
        else:
            print("This would cause an underflow error")
    
    def is_empty(self):
        return "Queue is empty" if len(self.__queue) == 0 else "Queue is not empty"
    
    def is_full(self):
        return "Qqueue is full" if len(self.__queue) == self.__max_length else "Queue is not full"

my_queue = Queue([], 5)

print()
print(my_queue.is_empty())
print(my_queue.is_full())
print()

my_queue.en_queue(1)
print(my_queue.get_queue())

my_queue.en_queue(2)
print(my_queue.get_queue())

my_queue.en_queue(3)
print(my_queue.get_queue())

my_queue.en_queue(4)
print(my_queue.get_queue())

my_queue.en_queue(5)
print(my_queue.get_queue())

print()
print(my_queue.is_empty())
print(my_queue.is_full())
print()

my_queue.en_queue(6)
print(my_queue.get_queue())

my_queue.de_queue()
print(my_queue.get_queue())

print()
print(my_queue.is_empty())
print(my_queue.is_full())
print()

my_queue.de_queue()
print(my_queue.get_queue())
my_queue.de_queue()
print(my_queue.get_queue())
my_queue.de_queue()
print(my_queue.get_queue())
my_queue.de_queue()
print(my_queue.get_queue())
my_queue.de_queue()

print(my_queue.__max_length) # protected therefore signs of encapsulation
