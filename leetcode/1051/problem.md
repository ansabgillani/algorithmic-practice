# Height Checker

**Problem ID:** 1051  
**Difficulty:** Easy

## Content

Given an integer array `heights` representing the current order of students in line and an integer array `expected` representing the non-decreasing order by height, return the number of indices where `heights[i] != expected[i]`.

### Example 1
**Input:** heights = [1,1,4,2,1,3]
**Output:** 3
**Explanation:** 
heights:  [1,1,4,2,1,3]
expected: [1,1,1,2,3,4]
Indices 2, 4, and 5 do not match.


### Example 2
**Input:** heights = [5,1,2,3,4]
**Output:** 5
**Explanation:** 
heights:  [5,1,2,3,4]
expected: [1,2,3,4,5]
All indices do not match.


### Example 3
**Input:** heights = [1,2,3,4,5]
**Output:** 0
**Explanation:** 
heights:  [1,2,3,4,5]
expected: [1,2,3,4,5]
All indices match.


### Constraints
- `1 <= heights.length <= 100`
- `1 <= heights[i] <= 100`

## Topic Tags
Array, Sorting, Counting Sort