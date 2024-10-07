# Minimum String Length After Removing Substrings

**Problem ID:** 2696

**Difficulty:** Easy

## Content
Given a string `s` consisting only of **uppercase** English letters, you can apply operations to remove any occurrence of the substrings `"AB"` or `"CD"` from `s`. Return the minimum possible length of the resulting string.

**Note**: The string concatenates after removing the substring and could produce new `"AB"` or `"CD"` substrings.

## Example

**Example 1:**


Input: s = "ABFCACDB"
Output: 2
Explanation: We can do the following operations:
- Remove the substring "ABFCACDB", so s = "FCACDB".
- Remove the substring "FCACD", so s = "FCAB".
- Remove the substring "FCAB", so s = "FC".
So the resulting length of the string is 2.
It can be shown that it is the minimum length that we can obtain.


**Example 2:**


Input: s = "ACBBD"
Output: 5
Explanation: We cannot do any operations on the string so the length remains the same.


## Constraints

- `1 <= s.length <= 100`
- `s` consists only of uppercase English letters.

## Topic Tags

- String
- Stack
- Simulation