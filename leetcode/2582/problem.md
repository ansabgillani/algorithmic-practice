# Pass the Pillow

**Problem ID:** 2582

**Difficulty:** Easy

## Content
There are `n` people standing in a line labeled from `1` to `n`. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

- For example, once the pillow reaches the `n`<sup>th</sup> person they pass it to the `n - 1`<sup>st</sup> person, then to the `n - 2`<sup>nd</sup> person and so on.

Given the two positive integers `n` and `time`, return *the index of the person holding the pillow after* `time` *seconds*.

&nbsp;

**Example 1:**

**Input:** n = 4, time = 5  
**Output:** 2  
**Explanation:** People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.  
After five seconds, the 2<sup>nd</sup> person is holding the pillow.


&nbsp;

**Example 2:**

**Input:** n = 3, time = 2  
**Output:** 3  
**Explanation:** People pass the pillow in the following way: 1 -> 2 -> 3.  
After two seconds, the 3<sup>rd</sup> person is holding the pillow.


&nbsp;

**Constraints:**

- `2 <= n <= 1000`
- `1 <= time <= 1000`

&nbsp;

**Note:** This question is the same as [Find the Child Who Has the Ball After K Seconds](https://leetcode.com/problems/find-the-child-who-has-the-ball-after-k-seconds/description/).

## Topic Tags
Math, Simulation