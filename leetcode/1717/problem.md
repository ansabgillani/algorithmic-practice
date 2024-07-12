# Maximum Score From Removing Substrings

**Problem ID:** 1717

**Difficulty:** Medium

## Content

You are given a string `s` and two integers `x` and `y`. You can perform two types of operations any number of times.

- Remove substring `"ab"` and gain `x` points.
- Remove substring `"ba"` and gain `y` points.

Return the maximum points you can gain after applying the above operations on `s`.

## Examples

**Example 1:**

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaa<u>ba</u>b". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaa<u>ab</u>". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcb<u>ba</u>a". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbc<u>ba</u>". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.


**Example 2:**

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20


## Constraints

- `1 <= s.length <= 10^5`
- `1 <= x, y <= 10^4`
- `s` consists of lowercase English letters.

## Topic Tags

String, Stack, Greedy