# Grumpy Bookstore Owner

**Problem ID:** 1052  
**Difficulty:** Medium  

## Content
Given a bookstore owner who is grumpy for some minutes and not grumpy for others, and knowing they can be non-grumpy for `minutes` consecutive minutes exactly once, determine the maximum number of satisfied customers.

### Problem Description
You are provided with two arrays:
- `customers`: An array of integers where `customers[i]` represents the number of customers entering the store at the start of the `i-th` minute and all those customers leave after the end of that minute.
- `grumpy`: A binary array where `grumpy[i]` is 1 if the bookstore owner is grumpy during the `i-th` minute, and 0 otherwise.

When the bookstore owner is not grumpy, all customers entering during that minute are satisfied. When they are grumpy, those customers are not satisfied.

### Example
**Example 1:**
- **Input:** `customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3`
- **Output:** `16`

**Explanation:**
The bookstore owner keeps themselves not grumpy for the last 3 minutes.
Maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.

**Example 2:**
- **Input:** `customers = [1], grumpy = [0], minutes = 1`
- **Output:** `1`

### Constraints
- `n == customers.length == grumpy.length`
- `1 <= n <= 2 * 10^4`
- `0 <= customers[i] <= 1000`
- `grumpy[i]` is either `0` or `1`.

## Topic Tags
Array, Sliding Window