# Remove All Occurrences of a Substring

**Problem ID:** 1910  
**Difficulty:** Medium

## Content

Given two strings `s` and `part`, perform the following operation on `s` until all occurrences of the substring `part` are removed:

- Find the **leftmost** occurrence of the substring `part` and **remove** it from `s`.

Return `s` after removing all occurrences of `part`.

A **substring** is a contiguous sequence of characters in a string.

### Example 1

**Input:** `s = "daabcbaabcbc"`, `part = "abc"`

**Output:** `"dab"`

**Explanation:** 
- `s = "da<strong><u>abc</u></strong>baabcbc"`, remove "abc" starting at index 2, so `s = "dabaabcbc"`.
- `s = "daba<strong><u>abc</u></strong>bc"`, remove "abc" starting at index 4, so `s = "dababc"`.
- `s = "dab<strong><u>abc</u></strong>"`, remove "abc" starting at index 3, so `s = "dab"`.
Now `s` has no occurrences of `"abc"`.

### Example 2

**Input:** `s = "axxxxyyyyb"`, `part = "xy"`

**Output:** `"ab"`

**Explanation:** 
- `s = "axxx<strong><u>xy</u></strong>yyyb"`, remove "xy" starting at index 4 so `s = "axxxyyyb"`.
- `s = "axx<strong><u>xy</u></strong>yyb"`, remove "xy" starting at index 3 so `s = "axxyyb"`.
- `s = "ax<strong><u>xy</u></strong>yb"`, remove "xy" starting at index 2 so `s = "axyb"`.
- `s = "a<strong><u>xy</u></strong>b"`, remove "xy" starting at index 1 so `s = "ab"`.
Now `s` has no occurrences of `"xy"`.

### Constraints

- `1 <= s.length <= 1000`
- `1 <= part.length <= 1000`
- `s` and `part` consists of lowercase English letters.

## Topic Tags
String, Stack, Simulation