from queue import Queue

# Create a queue of max size 3
q = Queue(maxsize=3)

print("Initial Queue Size:", q.qsize())

# Add elements to the queue
q.put('a')
q.put('b')
q.put('c')

print("\nFull:", q.full())  # Should print True

# Remove elements from the queue
print("\nElements dequeued from the queue:")
print(q.get())  # 'a'
print(q.get())  # 'b'
print(q.get())  # 'c'

print("\nEmpty:", q.empty())  # Should print True

# Add one more element
q.put(1)

print("\nAfter adding one item:")
print("Empty:", q.empty())   # Should print False
print("Full:", q.full())     # Should print False
