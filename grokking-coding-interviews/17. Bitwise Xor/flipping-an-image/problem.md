# Name: Flipping an Image

## Difficulty: Easy

## Description: 
Given an <code>n x n</code> binary matrix <code>image</code>, flip the image horizontally, then invert it, and return the resulting image.

To flip an image horizontally means that each row of the image is reversed.
For example, flipping <code>[1,1,0]</code> horizontally results in <code>[0,1,1]</code>.

To invert an image means that each <code>0</code> is replaced by <code>1</code>, and each <code>1</code> is replaced by <code>0</code>.
For example, inverting <code>[0,1,1]</code> results in <code>[1,0,0]</code>.

Example 1:
Input: image = [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]]. Then invert the image: [[1,0,0],[0,1,0],[1,1,1]].

Example 2:
Input: image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]. Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]].

Constraints:
- <code>n == image.length</code>
- <code>n == image[i].length</code>
- <code>1 &lt;= n &lt;= 20</code>
- <code>images[i][j]</code> is either <code>0</code> or <code>1</code>.