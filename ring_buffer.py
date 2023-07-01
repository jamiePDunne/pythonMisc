class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def enqueue(self, item):
        if self.is_full():
            self.dequeue()
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Buffer is empty")
        item = self.buffer[self.tail]
        self.buffer[self.tail] = None
        self.tail = (self.tail + 1) % self.capacity
        self.size -= 1
        return item

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.buffer[(self.tail + index) % self.capacity]
        raise IndexError("Index out of range")


buffer = RingBuffer(5)
buffer.enqueue(1)
buffer.enqueue(2)
buffer.enqueue(3)
print(len(buffer))  # Output: 3
print(buffer[0])  # Output: 1
print(buffer[2])  # Output: 3
print(buffer.dequeue())  # Output: 1
buffer.enqueue(4)
buffer.enqueue(5)
buffer.enqueue(6)
print(len(buffer))  # Output: 5
print(buffer.dequeue())  # Output: 2
print(buffer.dequeue())  # Output: 3
print(buffer.dequeue())  # Output: 4
print(buffer.dequeue())  # Output: 5
print(buffer.dequeue())  # Output: 6
