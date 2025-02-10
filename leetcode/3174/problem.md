# Clear Digits

**Problem ID:** 3174

**Difficulty:** Easy

## Problem Description
You are given a string `s`. Your task is to remove all digits by doing this operation repeatedly:

- Delete the first digit and the closest non-digit character to its left.

Return the resulting string after removing all digits.

**Note:** The operation cannot be performed on a digit that does not have any non-digit character to its left.

## Examples

### Example 1
**Input:** `s = "abc"`

**Output:** `"abc"`

**Explanation:**
There is no digit in the string.

### Example 2
**Input:** `s = "cb34"`

**Output:** `""`

**Explanation:**
First, apply the operation on `s[2]`, and `s` becomes `"c4"`.
Then apply the operation on `s[1]`, and `s` becomes `""`.

## Constraints
- `1 <= s.length <= 100`
- `s` consists only of lowercase English letters and digits.
- The input is generated such that it is possible to delete all digits.

## Topic Tags
String, Stack, Simulation