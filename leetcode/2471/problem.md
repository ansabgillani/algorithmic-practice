# Minimum Number of Operations to Sort a Binary Tree by Level

**Problem ID:** 2471

**Difficulty:** Medium

## Description
Given the `root` of a binary tree with **unique values**, return the minimum number of operations needed to make the values at each level sorted in a **strictly increasing order**.

## Example
### Example 1:
<img src="https://assets.leetcode.com/uploads/2022/09/18/image-20220918174006-2.png" style="width: 500px; height: 324px;" />
**Input:** root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
**Output:** 3
**Explanation:** 
- Swap 4 and 3. The 2<sup>nd</sup> level becomes [3,4].
- Swap 7 and 5. The 3<sup>rd</sup> level becomes [5,6,8,7].
- Swap 8 and 7. The 3<sup>rd</sup> level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.

### Example 2:
<img src="https://assets.leetcode.com/uploads/2022/09/18/image-20220918174026-3.png" style="width: 400px; height: 303px;" />
**Input:** root = [1,3,2,7,6,5,4]
**Output:** 3
**Explanation:** 
- Swap 3 and 2. The 2<sup>nd</sup> level becomes [2,3].
- Swap 7 and 4. The 3<sup>rd</sup> level becomes [4,6,5,7].
- Swap 6 and 5. The 3<sup>rd</sup> level becomes [4,5,6,7].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.

### Example 3:
<img src="https://assets.leetcode.com/uploads/2022/09/18/image-20220918174052-4.png" style="width: 400px; height: 274px;" />
**Input:** root = [1,2,3,4,5,6]
**Output:** 0
**Explanation:** Each level is already sorted in increasing order so return 0.

## Constraints
- The number of nodes in the tree is in the range `[1, 10^5]`.
- `1 <= Node.val <= 10^5`
- All the values of the tree are **unique**.

## Topic Tags
Tree, Breadth-First Search, Binary Tree