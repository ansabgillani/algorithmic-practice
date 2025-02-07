# Find the Number of Distinct Colors Among the Balls

**Problem ID:** 3160

**Difficulty:** Medium

## Content
You are given an integer `limit` and a 2D array `queries` of size `n x 2`.

There are `limit + 1` balls with **distinct** labels in the range `[0, limit]`. Initially, all balls are uncolored. For every query in `queries` that is of the form `[x, y]`, you mark ball `x` with the color `y`. After each query, you need to find the number of colors among the balls.

Return an array `result` of length `n`, where `result[i]` denotes the number of colors **after** `i`<sup>th</sup> query.

**Note** that when answering a query, lack of a color **will not** be considered as a color.

&nbsp;

**Example 1:**

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">limit = 4, queries = [[1,4],[2,5],[1,3],[3,4]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2,2,3]</span></p>

<p><strong>Explanation:</strong></p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2024/04/17/ezgifcom-crop.gif" style="width: 455px; height: 145px;" /></p>

<ul>
	<li>After query 0, ball 1 has color 4.</li>
	<li>After query 1, ball 1 has color 4, and ball 2 has color 5.</li>
	<li>After query 2, ball 1 has color 3, and ball 2 has color 5.</li>
	<li>After query 3, ball 1 has color 3, ball 2 has color 5, and ball 3 has color 4.</li>
</ul>
</div>

**Example 2:**

<div class="example-block">
<p><strong>Input:</strong> <span class="example-io">limit = 4, queries = [[0,1],[1,2],[2,2],[3,4],[4,5]]</span></p>

<p><strong>Output:</strong> <span class="example-io">[1,2,2,3,4]</span></p>

<p><strong>Explanation:</strong></p>

<strong><img alt="" src="https://assets.leetcode.com/uploads/2024/04/17/ezgifcom-crop2.gif" style="width: 457px; height: 144px;" /></strong>

<ul>
	<li>After query 0, ball 0 has color 1.</li>
	<li>After query 1, ball 0 has color 1, and ball 1 has color 2.</li>
	<li>After query 2, ball 0 has color 1, and balls 1 and 2 have color 2.</li>
	<li>After query 3, ball 0 has color 1, balls 1 and 2 have color 2, and ball 3 has color 4.</li>
	<li>After query 4, ball 0 has color 1, balls 1 and 2 have color 2, ball 3 has color 4, and ball 4 has color 5.</li>
</ul>
</div>

&nbsp;

**Constraints:**

- `1 <= limit <= 10^9`
- `1 <= n == queries.length <= 10^5`
- `queries[i].length == 2`
- `0 <= queries[i][0] &le; limit`
- `1 <= queries[i][1] &le; 10^9`

## Topic Tags
- Array
- Hash Table
- Simulation