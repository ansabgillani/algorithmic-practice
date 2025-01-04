# Unique Length-3 Palindromic Subsequences

**Problem ID:** 1930

**Difficulty:** Medium

## Content

Given a string `s`, return the number of **unique palindromes of length three** that are a **subsequence** of `s`.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted **once**.

A **palindrome** is a string that reads the same forwards and backwards.

A **subsequence** of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

- For example, `"ace"` is a subsequence of `"ab<u>c</u>d<u>e</u>"`.

## Example

### Example 1:

**Input:** s = "aabca"
**Output:** 3
**Explanation:** The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "a<u>a</u>b<u>c</u>a")
- "aaa" (subsequence of "aa<b>c</b>a")
- "aca" (subsequence of "a<u>ab</u>ca")


### Example 2:

**Input:** s = "adc"
**Output:** 0
**Explanation:** There are no palindromic subsequences of length 3 in "adc".


### Example 3:

**Input:** s = "bbcbaba"
**Output:** 4
**Explanation:** The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bb<u>c</u>b<u>a</u>ba")
- "bcb" (subsequence of "bb<u>cb</u>aba")
- "bab" (subsequence of "bb<b>cb</b>ab<a>")
- "aba" (subsequence of "bbc<b>aba</b>")


## Constraints

- `3 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.

## Topic Tags

- Hash Table
- String
- Bit Manipulation
- Prefix Sum