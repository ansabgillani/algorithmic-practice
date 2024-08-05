# Kth Distinct String in an Array

**Problem ID:** 2053

**Difficulty:** Easy

## Description
A **distinct string** is a string that appears only once in an array.

Given an array of strings `arr` and an integer `k`, return the `k`<sup>th</sup> distinct string present in `arr`. If there are fewer than `k` distinct strings, return an empty string `" "`.

Note that the strings are considered in the order in which they appear in the array.

## Examples

**Example 1:**
```plaintext
Input: arr = ["d","b","c","b","c","a"], k = 2
Output: "a"
Explanation:
The only distinct strings in arr are "d" and "a".
"d" appears 1<sup>st</sup>, so it is the 1<sup>st</sup> distinct string.
"a" appears 2<sup>nd</sup>, so it is the 2<sup>nd</sup> distinct string.
Since k == 2, "a" is returned. 


**Example 2:**
```plaintext
Input: arr = ["aaa","aa","a"], k = 1
Output: "aaa"
Explanation:
All strings in arr are distinct, so the 1<sup>st</sup> string "aaa" is returned.


**Example 3:**
```plaintext
Input: arr = ["a","b","a"], k = 3
Output: ""
Explanation:
The only distinct string is "b". Since there are fewer than 3 distinct strings, we return an empty string "".


## Constraints
- `1 <= k <= arr.length <= 1000`
- `1 <= arr[i].length <= 5`
- `arr[i]` consists of lowercase English letters.

## Topic Tags
Array, Hash Table, String, Counting