# Kth Largest Element in a Stream

**Problem ID:** 703

**Difficulty:** Easy

---

## Content

You are part of a university admissions office and need to keep track of the _k_ largest test scores from applicants in real-time. This helps dynamically determine cut-off marks for interviews and admissions as new applicants submit their scores.

Implement a class that, given an integer `k` and a stream of test scores `nums`, maintains a stream of test scores and continuously returns the _k_<sup>th</sup> highest test score after each new score is submitted. Specifically, you need to find the _k_<sup>th</sup> largest score in the sorted list of all scores.

---

## Class

- **KthLargest(int k, int[] nums)**: Initializes the object with the integer `k` and the stream of test scores `nums`.
- **int add(int val)**: Adds a new test score `val` to the stream and returns the element representing the _k_<sup>th</sup> largest element in the pool of test scores so far.


---

## Examples

**Example 1**

- **Input:** ["KthLargest", "add", "add", "add", "add", "add"], [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
- **Output:** [null, 4, 5, 5, 8, 8]
- **Explanation:**
    - KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
    - kthLargest.add(3); // return 4
    - kthLargest.add(5); // return 5
    - kthLargest.add(10); // return 5
    - kthLargest.add(9); // return 8
    - kthLargest.add(4); // return 8


**Example 2**

- **Input:** ["KthLargest", "add", "add", "add", "add"], [[4, [7, 7, 7, 7, 8, 3]], [2], [10], [9], [9]]
- **Output:** [null, 7, 7, 7, 8]
- **Explanation:**
    - KthLargest kthLargest = new KthLargest(4, [7, 7, 7, 7, 8, 3]);
    - kthLargest.add(2); // return 7
    - kthLargest.add(10); // return 7
    - kthLargest.add(9); // return 7
    - kthLargest.add(9); // return 8


---

## Constraints

- `0 <= nums.length <= 10^4`
- `1 <= k <= nums.length + 1`
- `-10^4 <= nums[i] <= 10^4`
- `-10^4 <= val <= 10^4`
- At most `10^4` calls will be made to `add`.

---

## Topic Tags

- Tree
- Design
- Binary Search Tree
- Heap (Priority Queue)
- Binary Tree
- Data Stream