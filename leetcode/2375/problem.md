# Construct Smallest Number From DI String

**Problem ID:** 2375  
**Difficulty:** Medium

## Problem Description

You are given a **0-indexed** string `pattern` of length `n` consisting of the characters `'I'` meaning **increasing** and `'D'` meaning **decreasing**.

A **0-indexed** string `num` of length `n + 1` is created using the following conditions:

- `num` consists of the digits `'1'` to `'9'`, where each digit is used **at most** once.
- If `pattern[i] == 'I'`, then `num[i] < num[i + 1]`.
- If `pattern[i] == 'D'`, then `num[i] > num[i + 1]`.

Return the lexicographically **smallest** possible string `num` that meets the conditions.

## Examples

### Example 1
**Input:** pattern = "IIIDIDDD"  
**Output:** "123549876"

### Example 2
**Input:** pattern = "DDD"  
**Output:** "4321"

## Constraints
- `1 <= pattern.length <= 8`
- `pattern` consists of only the letters `'I'` and `'D'`.

## Topic Tags
String, Backtracking, Stack, Greedy