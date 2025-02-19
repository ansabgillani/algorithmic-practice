# The k-th Lexicographical String of All Happy Strings of Length n

**Problem ID:** 1415

**Difficulty:** Medium

## Description
A **happy string** is a string that:

- Consists only of letters from the set `['a', 'b', 'c']`.
- Does not have any two consecutive characters that are the same.

For example, strings "abc", "ac", "b" and "abcbabcbcb" are all happy strings, while "aa", "baa" and "ababbc" are not.

Given two integers `n` and `k`, consider a list of all happy strings of length `n` sorted in lexicographical order. Return the k-th string in this list. If there are fewer than `k` happy strings of length `n`, return an empty string.

## Examples

**Example 1:**


Input: n = 1, k = 3
Output: "c"
Explanation: The list ["a", "b", "c"] contains all happy strings of length 1. The third string is "c".


**Example 2:**


Input: n = 1, k = 4
Output: ""
Explanation: There are only 3 happy strings of length 1.


**Example 3:**


Input: n = 3, k = 9
Output: "cab"
Explanation: There are 12 different happy strings of length 3 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]. You will find the 9th string = "cab".


## Constraints
- `1 <= n <= 10`
- `1 <= k <= 100`

## Topic Tags
- String
- Backtracking