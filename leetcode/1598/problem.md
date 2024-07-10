# Crawler Log Folder

**Problem ID:** 1598

**Difficulty:** Easy

## Content
The Leetcode file system keeps a log each time some user performs a **change folder** operation.

### Operations
- `"../"`: Move to the parent folder of the current folder. (If you are already in the main folder, **remain in the same folder**).
- `"./"`: Remain in the same folder.
- `"x/"`: Move to the child folder named `x` (This folder is **guaranteed to always exist**).

Given a list of strings `logs` where `logs[i]` is the operation performed by the user at the `i-th` step.

The file system starts in the main folder, then the operations in `logs` are performed.

Return the minimum number of operations needed to go back to the main folder after the change folder operations.

## Example
**Example 1:**

![image]


Input: logs = ["d1/", "d2/", "../", "d21/", "./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.


**Example 2:**

![image]


Input: logs = ["d1/", "d2/", "./", "d3/", "../", "d31/"]
Output: 3
Explanation: Use this change folder operation "../" 3 times and go back to the main folder.


**Example 3:**


Input: logs = ["d1/", "../", "../", "../"]
Output: 0
Explanation: Already in the main folder, so no operations needed.


## Constraints
- `1 <= logs.length <= 10^3`
- `2 <= logs[i].length <= 10`
- `logs[i]` contains lowercase English letters, digits, `'.'`, and `'/'`.
- `logs[i]` follows the format described in the statement.
- Folder names consist of lowercase English letters and digits.

## Topic Tags
- Array
- String
- Stack