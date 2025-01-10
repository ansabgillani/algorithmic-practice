# Word Subsets

**Problem ID:** 916

**Difficulty:** Medium

## Content

Given two string arrays `words1` and `words2`.

A string `b` is a **subset** of string `a` if every letter in `b` occurs in `a` including multiplicity.

For example, `"wrr"` is a subset of `"warrior"` but is not a subset of `"world"`.

A string `a` from `words1` is **universal** if for every string `b` in `words2`, `b` is a subset of `a`.

Return an array of all the **universal** strings in `words1`. You may return the answer in **any order**.

&nbsp;

**Example 1:**

*Input:* words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]

*Output:* ["facebook","google","leetcode"]

&nbsp;

**Example 2:**

*Input:* words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lc","eo"]

*Output:* ["leetcode"]

&nbsp;

**Example 3:**

*Input:* words1 = ["acaac","cccbb","aacbb","caacc","bcbbb"], words2 = ["c","cc","b"]

*Output:* ["cccbb"]

&nbsp;

**Constraints:**

* 1 <= words1.length, words2.length <= 10<sup>4</sup>
* 1 <= words1[i].length, words2[i].length <= 10
* `words1[i]` and `words2[i]` consist only of lowercase English letters.
* All the strings of `words1` are **unique**.

## Topic Tags

- Array
- Hash Table
- String