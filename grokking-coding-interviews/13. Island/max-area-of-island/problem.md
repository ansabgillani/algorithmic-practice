# Max Area of Island

## Difficulty: 
Medium

## Description: 
You are given an <code>m x n</code> binary matrix <code>grid</code>. An island is a group of <code>1</code>s (representing land) connected 4-directionally (horizontal or vertical). You may assume all four edges of the grid are surrounded by water. The area of an island is the number of cells with a value <code>1</code> in the island.

Return the maximum area of an island in <code>grid</code>. If there is no island, return 0.

### Example 1:

```
Input:
grid = [
  [0,0,1,0,0,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,1,1,0,1,0,0,0,0,0,0,0,0],
  [0,1,0,0,1,1,0,0,1,0,1,0,0],
  [0,1,0,0,1,1,0,0,1,1,1,0,0],
  [0,0,0,0,0,0,0,0,0,0,1,0,0],
  [0,0,0,0,0,0,0,1,1,1,0,0,0],
  [0,0,0,0,0,0,0,1,1,0,0,0,0]
]

Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.
```

### Example 2:

```
Input:
grid = [[0,0,0,0,0,0,0,0]]

Output: 0
```

### Constraints:
- <code>m == grid.length</code>
- <code>n == grid[i].length</code>
- <code>1 &lt;= m, n &lt;= 50</code>
- <code>grid[i][j]</code> is either <code>0</code> or <code>1</code>.