# Minimum Number of Changes to Make Binary String Beautiful

**Problem ID:** 2914

**Difficulty:** Medium

## Description
Given a `0-indexed` binary string `s` having an even length, return the minimum number of changes required to make the string `s` beautiful. A string is considered beautiful if it's possible to partition it into one or more substrings such that each substring has an even length and contains only `1`s or only `0`s.

## Examples

### Example 1
**Input:** s = "1001"
**Output:** 2
**Explanation:** Change `s[1]` to `1` and `s[3]` to `0` to get string "1100". This partitioning into "11|00" makes the string beautiful.

### Example 2
**Input:** s = "10"
**Output:** 1
**Explanation:** Change `s[1]` to `1` to get string "11". Partitioning it as "11" makes the string beautiful.

### Example 3
**Input:** s = "0000"
**Output:** 0
**Explanation:** No changes are needed as the string "0000" is already beautiful.

## Constraints
- `2 <= s.length <= 10^5`
- `s` has an even length.
- `s[i]` is either `'0'` or `'1'`.

## Topic Tags
String