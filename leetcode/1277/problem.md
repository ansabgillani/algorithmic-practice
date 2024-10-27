# Count Square Submatrices with All Ones

**Problem ID:** 1277

**Difficulty:** Medium

## Description

Given an `m * n` matrix of ones and zeros, return how many **square** submatrices have all ones.

&nbsp;

### Example 1:

**Input:**
```plaintext
matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]

**Output:** 15

**Explanation:**
There are **10** squares of side 1.
There are **4** squares of side 2.
There is  **1** square of side 3.
Total number of squares = 10 + 4 + 1 = **15**.

&nbsp;

### Example 2:

**Input:**
```plaintext
matrix =
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]

**Output:** 7

**Explanation:**
There are **6** squares of side 1.  
There is **1** square of side 2. 
Total number of squares = 6 + 1 = **7**.

&nbsp;

## Constraints

- `1 <= arr.length <= 300`
- `1 <= arr[0].length <= 300`
- `0 <= arr[i][j] <= 1`

&nbsp;

## Topic Tags

- Array
- Dynamic Programming
- Matrix