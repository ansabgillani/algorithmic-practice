# Maximum Odd Binary Number

**Problem ID:** 2864

**Difficulty:** Easy

## Description
Given a binary string `s` that contains at least one '1', rearrange the bits to form the maximum odd binary number.

Return a string representing the maximum odd binary number.

Note: The resulting string can have leading zeros.

## Example
### Example 1:
**Input:** s = "010"
**Output:** "001"
**Explanation:** The only '1' must be in the last position. So the answer is "001".

### Example 2:
**Input:** s = "0101"
**Output:** "1001"
**Explanation:** One of the '1's must be in the last position. The maximum number that can be made with the remaining digits is "100". So the answer is "1001".

## Constraints
- 1 <= s.length <= 100
- `s` consists only of '0' and '1'.
- `s` contains at least one '1'.

## Topic Tags
Math, String, Greedy