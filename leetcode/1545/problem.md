# Find Kth Bit in Nth Binary String

**Problem ID:** 1545

**Difficulty:** Medium

## Content
Given two positive integers `n` and `k`, the binary string `S_n` is formed as follows:

- `S_1 = "0"`
- `S_i = S_{i-1} + "1" + reverse(invert(S_{i-1}))` for `i > 1`

Where `+` denotes the concatenation operation, `reverse(x)` returns the reversed string `x`, and `invert(x)` inverts all the bits in `x` (`0` changes to `1` and `1` changes to `0`).

For example, the first four strings in the above sequence are:

- `S_1 = "0"`
- `S_2 = "0**1**1"`
- `S_3 = "011**1**001"`
- `S_4 = "0111001**1**0110001"`

Return the `k`th bit in `S_n`. It is guaranteed that `k` is valid for the given `n`.

## Example
**Example 1:**


Input: n = 3, k = 1
Output: "0"
Explanation: S_3 is "**<u>0</u>**111001".
The 1st bit is "0".


**Example 2:**


Input: n = 4, k = 11
Output: "1"
Explanation: S_4 is "0111001101**<u>1</u>**0001".
The 11th bit is "1".


## Constraints
- `1 <= n <= 20`
- `1 <= k <= 2^n - 1`

## Topic Tags
- String
- Recursion
- Simulation