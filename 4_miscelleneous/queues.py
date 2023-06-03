# Queues (double ended queue)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
print(queue)
# >>> deque([1, 2])

queue.popleft()
print(queue)
# >>> deque([2])

queue.appendleft(1)
print(queue)
# >>> deque([1, 2])

queue.pop()
print(queue)
# >>> deque([1])