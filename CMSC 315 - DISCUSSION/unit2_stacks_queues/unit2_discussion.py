"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []
   
    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        
        #This is first item removed as it's being added just now
        self.items.append(value)
        
    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

         # This gets rid of and returns the most recently added value.
        # If the stack is empty, return None instead of error message
        if self.is_empty():
            return None

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        #Returns top integer without dismissing it, when empty stack, return none
        if self.is_empty():
            return None

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
         
        # Returns true when the stack doesn't have any values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        
        # deque helps with efficient additions
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        #FIFO because first item added will be first item dismissed.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        # If the queue is empty, return None instead of error message
        if self.is_empty():
            return None

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        # Returns front value without deleting data.
        # If the queue is empty, return None.
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")
print("TODO: Create a Stack object, demonstrate LIFO behavior,")
print("      test popping from an empty stack,")
print("      test peeking at an empty stack,")
print("      and verify a single-item stack becomes empty after removal.")

stack = Stack()

stack.push("1")
stack.push("2")
stack.push("3")
stack.push("4")

print("Added 1, 2, 3, and 4 to the stack.")
print("The stack uses LIFO: Last In, First Out.")
print("Top value before popping:", stack.peek())

# Pop values from the stack.
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Popped:", stack.pop())
print("Popped:", stack.pop())

# Check if the stack is empty.
print("Is the stack empty?", stack.is_empty())

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")
print("TODO: Create a Queue object, demonstrate FIFO behavior,")
print("      test dequeuing from an empty queue,")
print("      test viewing the front of an empty queue,")
print("      and verify a single-item queue becomes empty after removal.")

queue = Queue()

# 4 integers to queue.
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)

print("Added 10, 20, 30, and 40 to the queue.")
print("The queue uses FIFO: First In, First Out.")
print("Front value before dequeuing:", queue.front())

# FIFO behavior
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())
print("Dequeued:", queue.dequeue())

# The values come out in the same order they were added.
print("The values were removed in FIFO order: 10, 20, 30, 40.")

# Dequeue from an empty queue.
print("\nTrying to dequeue from an empty queue:")
print("Result:", queue.dequeue())

# Testing front of an empty queue.
print("\nTrying to view the front of an empty queue:")
print("Result:", queue.front())

# Testing queue containing only one item.
single_queue = Queue()
single_queue.enqueue(100)

print("\nSingle-item queue:")
print("The Front value:", single_queue.front())

# Remove the only item.
print("Removed:", single_queue.dequeue())

# Making sure queue is empty.
print("Single-item queue empty?", single_queue.is_empty())

if __name__ == "__main__":
    main()
