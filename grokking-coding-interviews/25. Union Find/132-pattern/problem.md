# Name: 
132 Pattern

## Difficulty: 
Medium

## Description: 
Given an array of <code>n</code> integers <code>nums</code>, a <strong>132 pattern</strong> is a subsequence of three integers <code>nums[i]</code>, <code>nums[j]</code>, and <code>nums[k]</code> such that <code>i &lt; j &lt; k</code> and <code>nums[i] &lt; nums[k] &lt; nums[j]</code>. Return <code>true</code> if there is a <strong>132 pattern</strong> in <code>nums</code>, otherwise, return <code>false</code>.

### Example 1:
- **Input:** nums = [1,2,3,4]
- **Output:** false
- **Explanation:** There is no 132 pattern in the sequence.

### Example 2:
- **Input:** nums = [3,1,4,2]
- **Output:** true
- **Explanation:** There is a 132 pattern in the sequence: [1, 4, 2].

### Example 3:
- **Input:** nums = [-1,3,2,0]
- **Output:** true
- **Explanation:** There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0], and [-1, 2, 0].

### Constraints:
- <code>n == nums.length</code>
- <code>1 &lt;= n &lt;= 2 * 10<sup>5</sup></code>
- <code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code>