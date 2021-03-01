# Data Structures

Data structures are code structures for storing and organizing data that make it
easier to modify, navigate, and access information. Data structures determine
how data is collected, the functionality we can implement, and the
relationships between data.

## Goals

- Manage and utilize large datasets
- Quickly search for particular data from a database
- Build clear hierarchical or relational connections between data points
- Simplify and speed up data processing

## Queues

### Advantages

- Automatically orders data chronologically
- Scales to meet size requirements
- Time-efficient with deque class

### Disadvantages

- Can only access data on the ends

## Linked List

### Advantages

- Efficient insertion and deletion of new elements
- Simpler to reorganize than arrays
- Useful as a starting point for advanced data structures like graphs or trees

### Disadvantages

- Storage of pointers with each data point increases memory usage
- Must always traverse the linked list from Head node to find a specific element

## Binary Tree

### Advantages

- Good for representing hierarchical relationships
- Dynamic size, great at scale
- Quick insert and delete operations
- In a binary search tree, inserted nodes are sequenced immediately.
- Binary search trees are efficient at searches; length is only O(height).

### Disadvantages

- Time expensive, O(logn), to modify or “balance” trees or retrieve elements
from a known location
- Child nodes hold no information on their parent node and can be hard to
traverse backward
- Only works for lists that are sorted. Unsorted data degrades into linear search.
