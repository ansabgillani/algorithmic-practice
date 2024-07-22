# Sort the People

**Problem ID:** 2418  
**Difficulty:** Easy

## Content

You are given an array of strings `names`, and an array `heights` that consists of **distinct** positive integers. Both arrays are of length `n`.

For each index `i`, `names[i]` and `heights[i]` denote the name and height of the `i`<sup>th</sup> person.

Return `names` sorted in **descending** order by the people's heights.

&nbsp;

### Example 1:

<pre>
<strong>Input:</strong> names = ["Mary","John","Emma"], heights = [180,165,170]
<strong>Output:</strong> ["Mary","Emma","John"]
<strong>Explanation:</strong> Mary is the tallest, followed by Emma and John.
</pre>

### Example 2:

<pre>
<strong>Input:</strong> names = ["Alice","Bob","Bob"], heights = [155,185,150]
<strong>Output:</strong> ["Bob","Alice","Bob"]
<strong>Explanation:</strong> The first Bob is the tallest, followed by Alice and the second Bob.
</pre>

&nbsp;

### Constraints:

- `n == names.length == heights.length`
- `1 <= n <= 10^3`
- `1 <= names[i].length <= 20`
- `1 <= heights[i] <= 10^5`
- `names[i]` consists of lower and upper case English letters.
- All the values of `heights` are distinct.

## Topic Tags

- Array
- Hash Table
- String
- Sorting