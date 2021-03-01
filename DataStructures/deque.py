"""
The .append and .pop methods make a list usable as a stack or a queue
(if you use .append and .pop(0), you get FIFO behavior).
But inserting and removing from the head of a list (the 0-index end)
is costly because the entire list must be shifted in memory.

The class collections.deque is a thread-safe double-ended
queue designed for fast inserting and removing from both ends.

Note that deque implements most of the list methods,
and adds a few specific to its design, like `popleft`
and `rotate`. But there is a hidden cost: removing items
from the middle of a deque is not as fast. It is really
optimized for appending and popping from the ends.

The append and popleft operations are atomic, so deque is safe
to use as a FIFO queue in multithreaded applications
without the need for using locks.
"""
from collections import deque


dq = deque(range(10), maxlen=10)
print(dq)

# Rotating with n > 0 takes items from the right end and prepends them to the left.
# When n < 0 items are taken from left and appended to the right.
dq.rotate(3)
print(dq)

dq.rotate(-4)
print(dq)

# Appending to a deque that is full (len(d) == d.maxlen) discards items from the other end;
# note in the next line that the 0 is dropped.
dq.appendleft(-1)
print(dq)

# Adding three items to the right pushes out the leftmost -1, 1, and 2.
dq.extend([11, 22, 33])
print(dq)
