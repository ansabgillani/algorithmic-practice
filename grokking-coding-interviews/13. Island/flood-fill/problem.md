# Flood Fill

## Difficulty: 
Easy

## Description: 
You are given an image represented by an <code>m x n</code> grid of integers <code>image</code>, where <code>image[i][j]</code> represents the pixel value of the image. You are also given three integers <code>sr</code>, <code>sc</code>, and <code>color</code>. Your task is to perform a <strong>flood fill</strong> on the image starting from the pixel <code>image[sr][sc]</code>.

To perform a <strong>flood fill</strong>:

1. Begin with the starting pixel and change its color to <code>color</code>.
2. Perform the same process for each pixel that is <strong>directly adjacent</strong> (pixels that share a side with the original pixel, either horizontally or vertically) and shares the <strong>same color</strong> as the starting pixel.
3. Keep <strong>repeating</strong> this process by checking neighboring pixels of the <em>updated</em> pixels&nbsp;and modifying their color if it matches the original color of the starting pixel.
4. The process <strong>stops</strong> when there are <strong>no more</strong> adjacent pixels of the original color to update.

Return the <strong>modified</strong> image after performing the flood fill.

### Example 1:

- **Input:** 
  - `image = [[1,1,1],[1,1,0],[1,0,1]]`, `sr = 1`, `sc = 1`, `color = 2`
  
- **Output:**
  - `[[2,2,2],[2,2,0],[2,0,1]]`

### Example 2:

- **Input:** 
  - `image = [[0,0,0],[0,0,0]]`, `sr = 0`, `sc = 0`, `color = 0`
  
- **Output:**
  - `[[0,0,0],[0,0,0]]`

### Constraints:
- <code>m == image.length</code>
- <code>n == image[i].length</code>
- <code>1 &lt;= m, n &lt;= 50</code>
- <code>0 &lt;= image[i][j], color &lt; 2<sup>16</sup></code>
- <code>0 &lt;= sr &lt; m</code>
- <code>0 &lt;= sc &lt; n</code>