# Minimum Remove to Make Valid Parentheses

**Problem ID:** 1249  
**Difficulty:** Medium

## Description
Given a string `s` of `(`, `)` and lowercase English characters.

Your task is to remove the minimum number of parentheses (`(` or `)`, in any positions ) so that the resulting **parentheses string** is valid and return **any** valid string.

Formally, a **parentheses string** is valid if and only if:

- It is the empty string, contains only lowercase characters, or
- It can be written as `AB` (`A` concatenated with `B`), where `A` and `B` are valid strings, or
- It can be written as `(A)`, where `A` is a valid string.

## Examples

**Example 1:**

<strong>Input:</strong> s = &quot;lee(t(c)o)de)&quot;
<strong>Output:</strong> &quot;lee(t(c)o)de&quot;
<strong>Explanation:</strong> &quot;lee(t(co)de)&quot;, &quot;lee(t(c)ode)&quot; would also be accepted.


**Example 2:**

<strong>Input:</strong> s = &quot;a)b(c)d&quot;
<strong>Output:</strong> &quot;ab(c)d&quot;


**Example 3:**

<strong>Input:</strong> s = &quot;))(&quot;
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong> An empty string is also valid.


## Constraints

- `1 <= s.length <= 10^5`
- `s[i]` is either `(`, `)`, or lowercase English letter.

## Topics
- String
- Stack