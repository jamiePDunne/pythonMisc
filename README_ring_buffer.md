# Ring Buffer (Circular Buffer) 

## What is a Ring Buffer?

A ring buffer, also known as a circular buffer, is a data structure that efficiently manages a fixed-size buffer. It stores a stream of data elements in a cyclic manner, overwriting the oldest data with the newest data when the buffer is full. Ring buffers are commonly used in scenarios where you need to store a continuous flow of data.

## Implementation Details

The provided Python code implements a ring buffer using a class called `RingBuffer`. Here's how it works:

1. Creating a Ring Buffer: To create a ring buffer, you need to specify the capacity, which determines the maximum number of elements the buffer can hold. For example, to create a ring buffer with a capacity of 5, use the following code:

   ```python
   buffer = RingBuffer(5)
   ```

2. Enqueuing Elements: To add elements to the ring buffer, use the `enqueue(item)` method. It adds the `item` to the buffer, and if the buffer is already full, it automatically removes the oldest item before adding the new item. For example:

   ```python
   buffer.enqueue(1)
   buffer.enqueue(2)
   buffer.enqueue(3)
   ```

3. Dequeuing Elements: To retrieve and remove the oldest item from the ring buffer, use the `dequeue()` method. It returns the oldest item and adjusts the buffer accordingly. If the buffer is empty, an `IndexError` will be raised. For example:

   ```python
   item = buffer.dequeue()
   ```

4. Checking Buffer Status: You can use the `is_empty()` and `is_full()` methods to check if the buffer is empty or full, respectively. These methods return a Boolean value (`True` or `False`). For example:

   ```python
   if buffer.is_empty():
       print("Buffer is empty")
   if buffer.is_full():
       print("Buffer is full")
   ```

5. Accessing Elements: You can access elements in the buffer using index notation. The `__getitem__(index)` method allows you to retrieve the item at the specified `index`. The index can range from `0` to `size - 1`, where `size` is the current number of elements in the buffer. If the index is out of range, an `IndexError` will be raised. For example:

   ```python
   item = buffer[0]
   ```

6. Getting Buffer Size: You can retrieve the current size of the buffer using the `__len__()` method, which returns the number of elements in the buffer. For example:

   ```python
   size = len(buffer)
   ```

## Example Usage

Here's an example that demonstrates the usage of the ring buffer:

```python
# Create a ring buffer with a capacity of 5
buffer = RingBuffer(5)

# Enqueue elements
buffer.enqueue(1)
buffer.enqueue(2)
buffer.enqueue(3)

# Print the buffer size
print(len(buffer))  # Output: 3

# Access elements using index notation
print(buffer[0])  # Output: 1
print(buffer[2])  # Output: 3

# Dequeue the oldest item
print(buffer.dequeue())  # Output: 1

# Enqueue more elements
buffer.enqueue(4)
buffer.enqueue(5)
buffer.enqueue(6)

# Print the buffer size
print(len(buffer))  # Output: 5

# Dequeue elements
print(buffer.dequeue())  # Output: 2


print(buffer.dequeue())  # Output: 3
print(buffer.dequeue())  # Output: 4
print(buffer.dequeue())  # Output: 5
print(buffer.dequeue())  # Output: 6
```

This example demonstrates how to create a ring buffer, enqueue and dequeue elements, check the buffer status, access elements using index notation, and get the buffer size.

