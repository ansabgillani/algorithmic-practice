# Find Missing Observations

**Problem ID:** 2028

**Difficulty:** Medium

## Content
You have observations of `n + m` **6-sided** dice rolls with each face numbered from `1` to `6`. `n` of the observations went missing, and you only have the observations of `m` rolls. Fortunately, you have also calculated the **average value** of the `n + m` rolls.

You are given an integer array `rolls` of length `m` where `rolls[i]` is the value of the `i`<sup>th</sup> observation. You are also given the two integers `mean` and `n`.

Return **an array of length `n`** containing the missing observations such that the **average value** of the `n + m` rolls is **exactly** `mean`. If there are multiple valid answers, return **any of them**. If no such array exists, return **an empty array**.

The **average value** of a set of `k` numbers is the sum of the numbers divided by `k`.

Note that `mean` is an integer, so the sum of the `n + m` rolls should be divisible by `n + m`.

&nbsp;

**Example 1:**

<pre>
<strong>Input:</strong> rolls = [3,2,4,3], mean = 4, n = 2
<strong>Output:</strong> [6,6]
<strong>Explanation:</strong> The mean of all n + m rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4.
</pre>

**Example 2:**

<pre>
<strong>Input:</strong> rolls = [1,5,6], mean = 3, n = 4
<strong>Output:</strong> [2,3,2,2]
<strong>Explanation:</strong> The mean of all n + m rolls is (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3.
</pre>

**Example 3:**

<pre>
<strong>Input:</strong> rolls = [1,2,3,4], mean = 6, n = 4
<strong>Output:</strong> []
<strong>Explanation:</strong> It is impossible for the mean to be 6 no matter what the 4 missing rolls are.
</pre>

&nbsp;

**Constraints:**

- `m == rolls.length`
- `1 &lt;= n, m &lt;= 10<sup>5</sup>`
- `1 &lt;= rolls[i], mean &lt;= 6`

## Topic Tags
Array, Math, Simulation