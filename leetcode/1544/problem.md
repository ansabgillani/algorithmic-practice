# Make The String Great

**Problem ID:** 1544  
**Difficulty:** Easy  

## Content

Given a string `s` of lower and upper case English letters.

A good string is a string which doesn't have **two adjacent characters** `s[i]` and `s[i + 1]` where:

- `0 <= i <= s.length - 2`
- `s[i]` is a lower-case letter and `s[i + 1]` is the same letter but in upper-case or **vice-versa**.

To make the string good, you can choose **two adjacent** characters that make the string bad and remove them. You can keep doing this until the string becomes good.

Return **the string** after making it good. The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

&nbsp;

**Example 1:**

<pre>
<strong>Input:</strong> s = "leEeetcode"
<strong>Output:</strong> "leetcode"
<strong>Explanation:</strong> In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
</pre>

&nbsp;

**Example 2:**

<pre>
<strong>Input:</strong> s = "abBAcC"
<strong>Output:</strong> ""
<strong>Explanation:</strong> We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
</pre>

&nbsp;

**Example 3:**

<pre>
<strong>Input:</strong> s = "s"
<strong>Output:</strong> "s"
</pre>

&nbsp;

**Constraints:**

- `1 <= s.length <= 100`
- `s` contains only lower and upper case English letters.

## Topic Tags

- String
- Stack