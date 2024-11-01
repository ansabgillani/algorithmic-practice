# Delete Characters to Make Fancy String

**Problem ID:** 1957

**Difficulty:** Easy

## Description
A **fancy string** is a string where no **three** consecutive characters are equal. Given a string `s`, delete the **minimum** possible number of characters from `s` to make it **fancy**. Return the final string after deletion.

## Examples

- **Example 1:**
    - **Input:** s = "leetcode"
    - **Output:** "leetcode"
    - **Explanation:** Remove an 'e' from the first group of 'e's to create "leetcode". No three consecutive characters are equal, so return "leetcode".

- **Example 2:**
    - **Input:** s = "aaabaaa"
    - **Output:** "aabaa"
    - **Explanation:** Remove an 'a' from the first group of 'a's to create "aabaaaa". Remove two 'a's from the second group of 'a's to create "aabaa". No three consecutive characters are equal, so return "aabaa".

- **Example 3:**
    - **Input:** s = "aab"
    - **Output:** "aab"
    - **Explanation:** No three consecutive characters are equal, so return "aab".

## Constraints
- `1 <= s.length <= 10^5`
- `s` consists only of lowercase English letters.

## Topic Tags
String