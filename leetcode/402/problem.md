# Remove K Digits

**Problem ID:** 402

**Difficulty:** Medium

## Description
Given a non-negative integer `num` represented as a string and an integer `k`, the task is to remove `k` digits from `num` such that the resulting number is the smallest possible integer.

## Example 1
**Input:** num = "1432219", k = 3  
**Output:** "1219"  
**Explanation:** By removing the digits '4', '3', and '2', the smallest possible number is '1219'.

## Example 2
**Input:** num = "10200", k = 1  
**Output:** "200"  
**Explanation:** Removing the leading '1' results in '200'. The output must not contain any leading zeroes.

## Example 3
**Input:** num = "10", k = 2  
**Output:** "0"  
**Explanation:** Removing all digits leaves an empty number, which is represented as '0'.

## Constraints
- `1 <= k <= num.length <= 10^5`
- `num` consists of only digits.
- `num` does not have any leading zeros except for the zero itself.

## Topic Tags
- String
- Stack
- Greedy
- Monotonic Stack