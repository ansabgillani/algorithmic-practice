# Number of Wonderful Substrings

**Problem ID:** 1915

**Difficulty:** Medium

## Description
A **wonderful** string is a string where at most one letter appears an odd number of times.

- For example, `"ccjjc"` and `"abab"` are wonderful, but `"ab"` is not.

Given a string `word` that consists of the first ten lowercase English letters (`'a'` through `'j'`), return the **number of wonderful non-empty substrings** in `word`. If the same substring appears multiple times in `word`, then count **each occurrence** separately.

A **substring** is a contiguous sequence of characters in a string.

## Examples

**Example 1:**

```plaintext
Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "a<b>a</b>"
- "a<b>b</b>a"
- "ab<b>a</b>"
- "aba"


**Example 2:**

```plaintext
Input: word = "aabb"
Output: 9
Explanation: The nine wonderful substrings are underlined below:
- "a<a>b</b>b"
- "aa<b>b</b>"
- "aab<b>b</b>"
- "aabb"
- "a<a>bb</b>"
- "a<b>abb</b>"
- "aa<b>b</b>"
- "aab<b>b</b>"
- "a<b>ab</b>"


**Example 3:**

```plaintext
Input: word = "he"
Output: 2
Explanation: The two wonderful substrings are underlined below:
- "<b>h</b>e"
- "h<strong><u>e</u></strong>"


## Constraints

- `1 <= word.length <= 10^5`
- `word` consists of lowercase English letters from `'a'` to `'j'`.

## Topic Tags
Hash Table, String, Bit Manipulation, Prefix Sum