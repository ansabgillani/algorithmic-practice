# Valid Parenthesis String

**Problem ID:** 678  
**Difficulty:** Medium

## Description
Given a string `s` containing only three types of characters: `'('`, `')'`, and `'*'`, return `true` if `s` is **valid**.

The following rules define a **valid** string:
- Any left parenthesis `'('` must have a corresponding right parenthesis `')'`.
- Any right parenthesis `')'` must have a corresponding left parenthesis `'('`.
- Left parenthesis `'('` must go before the corresponding right parenthesis `')'`.
- `'*'` could be treated as a single right parenthesis `')'`, a single left parenthesis `'('`, or an empty string `""`.

## Examples

**Example 1:**
```plaintext
Input: s = "()"
Output: true


**Example 2:**
```plaintext
Input: s = "(*)"
Output: true


**Example 3:**
```plaintext
Input: s = "(*))"
Output: true


## Constraints

- `1 <= s.length <= 100`
- `s[i]` is `'('`, `')'`, or `'*'`.

## Topic Tags
- String
- Dynamic Programming
- Stack
- Greedy