# Programming Assignment 3: Heaps, Priority Queues, and Hashing

**Name:** Erica Cepeda

## Description

In this project, both heap-based priority queue and hash table have been developed in Python. In the implementation of the priority queue, min-heap has been used, in which the smaller numbers denote the tasks with higher priority.

Both programs contain test cases to check their proper working, as well as for runtime testing with various input sizes. Analysis of the heap, priority queue efficiency, hash table performance, collision handling, and load factors has been performed.

## How to Run

Ensure that Python 3 is installed.

Run the priority queue program by using:

`python3 priority_queue.py`

or:

`python priority_queue.py`

Run the hash table program by using:

`python3 hash_table.py`

or:

`python hash_table.py`

## Files Included

- `priority_queue.py` - Python implementation of a min-heap priority queue, required test cases, and runtime testing
- `hash_table.py` - Python implementation of a hash table using separate chaining, required test cases, collision testing, and runtime testing
- `priority_queue_basic_tests.png` - Screenshot showing successful priority queue insertion, peek, and extraction behavior
- `priority_queue_runtime.png` - Screenshot showing priority queue runtime testing
- `hash_table_basic_tests.png` - Screenshot showing successful hash table insertion, search, and deletion
- `hash_table_collision_test.png` - Screenshot showing successful collision handling using separate chaining
- `hash_table_runtime.png` - Screenshot showing hash table runtime testing
- `report.md` - Written analysis of heap-based priority queues, hash tables, runtime behavior, test results, and reflection
- `README.md` - Project overview and instructions

## Priority Queue Implementation

The priority queue is implemented as a min-heap using a Python list.

The program includes:

- Insert operation
- Peek operation
- Extract minimum operation
- Heapify-up operation
- Heapify-down operation
- Method for displaying the heap contents

The lower the numerical value, the higher the priority of the task. In the test case, we will work with tasks relating to students' support and administrative tasks of different priorities.

Built-in Python `heapq` library is not used.

## Priority Queue Test Cases

The program will be tested in terms of:

- Inserting several items successfully
- Peeking the highest-priority item
- Removing items according to priority
- Proper functioning after multiple insertions and deletions
- Runtime for input sizes 100, 1,000, and 10,000
- All priority queue runtime tests have resulted in the correct output

## Hash Table Implementation

For the implementation of hash table, the following techniques are employed: a custom hash function and separate chaining collision handling technique.

For the program:

- Hash function
- Insertion
- Getting/search
- Deletion
- Collision resolution by means of separate chaining

The test case consists of inserting student ID as a key and academic program as a value.

## Hash Table Test Cases

The program will be tested in terms of:

- Successful insertion of keys and values
- Searching existing keys
- Returning proper message when searching non-existing key
- Successful deletion of keys
- Proper handling of collisions
- Retrieval of collided keys
- Runtime for input sizes 100, 1,000, and 10,000
- All hash table runtime tests have resulted in the correct output

## Runtime Results

### Priority Queue

| Input Size | Operation | Runtime | Correct |
|---|---|---:|---|
| 100 | Insert | 0.000044 seconds | True |
| 100 | Extract All | 0.000205 seconds | True |
| 1,000 | Insert | 0.000476 seconds | True |
| 1,000 | Extract All | 0.003247 seconds | True |
| 10,000 | Insert | 0.005682 seconds | True |
| 10,000 | Extract All | 0.133236 seconds | True |

### Hash Table

| Input Size | Operation | Runtime | Correct |
|---|---|---:|---|
| 100 | Insert | 0.000055 seconds | True |
| 100 | Search | 0.000045 seconds | True |
| 1,000 | Insert | 0.001154 seconds | True |
| 1,000 | Search | 0.000780 seconds | True |
| 10,000 | Insert | 0.085783 seconds | True |
| 10,000 | Search | 0.060464 seconds | True |

## Program Output

See the following screenshots for evidence of successful execution in Visual Studio Code:

- `priority_queue_basic_tests.png`
- `priority_queue_runtime.png`
- `hash_table_basic_tests.png`
- `hash_table_collision_test.png`
- `hash_table_runtime.png`
