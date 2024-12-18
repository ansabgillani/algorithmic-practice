# Maximum Length of Pair Chain

## Difficulty: 
Medium

## Description: 
You are given an array of pairs `pairs` where `pairs[i] = [left_i, right_i]` and `left_i < right_i`.

A pair `p2 = [c, d]` **follows** a pair `p1 = [a, b]` if `b < c`. A **chain** of pairs can be formed in this fashion.

Return the length of the longest chain which can be formed. You do not need to use up all the given intervals; you can select pairs in any order.

## Example 1:

```plaintext
Input:
pairs = [[1,2],[2,3],[3,4]]

Output: 
2

Explanation: The longest chain is [1,2] -> [3,4].
```

## Example 2:

```plaintext
Input:
pairs = [[1,2],[7,8],[4,5]]

Output: 
3

Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].
```

## Constraints:

- `n == pairs.length`
- `1 <= n <= 1000`
- `-1000 <= left_i < right_i <= 1000`