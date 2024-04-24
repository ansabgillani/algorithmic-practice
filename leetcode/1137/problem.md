# N-th Tribonacci Number

**Problem ID:** 1137

**Difficulty:** Easy

## Content

The Tribonacci sequence \( T_n \) is defined as follows:

\[
T_0 = 0, \quad T_1 = 1, \quad T_2 = 1, \quad \text{and} \quad T_{n+3} = T_n + T_{n+1} + T_{n+2} \quad \text{for} \quad n \geq 0.
\]

Given \( n \), return the value of \( T_n \).

### Examples

**Example 1:**

Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4


**Example 2:**

Input: n = 25
Output: 1389537


### Constraints

- \( 0 \leq n \leq 37 \)
- The answer is guaranteed to fit within a 32-bit integer, i.e., \( \text{answer} \leq 2^{31} - 1 \)

## Topic Tags

- Math
- Dynamic Programming
- Memoization