# Minimum Number of Moves to Seat Everyone

**Problem ID:** 2037

**Difficulty:** Easy

## Problem Description

Given `n` available seats and `n` students standing in a room, you are provided with two arrays: `seats` and `students`. Each array has length `n`, where `seats[i]` is the position of the `i-th` seat and `students[j]` is the position of the `j-th` student.

You can move each student by 1 unit to the left or right. Your goal is to find the minimum number of moves required so that no two students are in the same seat.

### Example 1

**Input:** seats = [3, 1, 5], students = [2, 7, 4]

**Output:** 4

**Explanation:**
- Move the first student from position 2 to position 1 (1 move).
- Move the second student from position 7 to position 5 (2 moves).
- Move the third student from position 4 to position 3 (1 move).

### Example 2

**Input:** seats = [4, 1, 5, 9], students = [1, 3, 2, 6]

**Output:** 7

**Explanation:**
- The first student is not moved.
- Move the second student from position 3 to position 4 (1 move).
- Move the third student from position 2 to position 5 (3 moves).
- Move the fourth student from position 6 to position 9 (3 moves).

### Example 3

**Input:** seats = [2, 2, 6, 6], students = [1, 3, 2, 6]

**Output:** 4

**Explanation:**
- Move the first student from position 1 to position 2 (1 move).
- Move the second student from position 3 to position 6 (3 moves).
- The third student is not moved.
- The fourth student is not moved.

## Constraints

- `n == seats.length == students.length`
- `1 <= n <= 100`
- `1 <= seats[i], students[j] <= 100`

## Topic Tags

Array, Greedy, Sorting, Counting Sort