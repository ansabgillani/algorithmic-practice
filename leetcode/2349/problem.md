# Design a Number Container System

**Problem ID:** 2349

**Difficulty:** Medium

## Description
Design a number container system that can do the following:

- **Insert/Replace**: Insert or replace a number at the given index in the system.
- **Find**: Return the smallest index for the given number in the system.

## Class Implementation
Implement the `NumberContainers` class:
- `NumberContainers()`: Initializes the number container system.
- `void change(int index, int number)`: Fills the container at `index` with the `number`. If there is already a number at that `index`, replace it.
- `int find(int number)`: Returns the smallest index for the given `number`, or `-1` if no index is filled by `number`.

## Example
nc = NumberContainers()
print(nc.find(10))  # Output: -1
nc.change(2, 10)
nc.change(1, 10)
nc.change(3, 10)
nc.change(5, 10)
print(nc.find(10))  # Output: 1
nc.change(1, 20)
print(nc.find(10))  # Output: 2


## Constraints
- `1 <= index, number <= 10^9`
- At most `10^5` calls will be made to `change` and `find`.

## Topic Tags
Hash Table, Design, Heap (Priority Queue), Ordered Set