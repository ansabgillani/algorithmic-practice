Order-Agnostic Binary Search

Order-Agnostic Binary Search is a modified version of Binary Search algorithm. Here in this modified binary search comes with one more condition checking. The intuition behind this algorithm is what if the order of the sorted array is not given. So here check that the value of the first element is greater or smaller than the last element.

If the first element is smaller than the last element-then if the search key value X is less than the middle of the interval then the end pointer will be changed to middle -1 otherwise start will be changed to middle + 1.
If the first element is greater than the last element-then if the search key value X is less than the middle of the interval then the start pointer will move to the next element of the middle element otherwise the end pointer will move previous to the middle element.
In the end, if the search key value matches with the middle element then the element which was given to the search is found.

Implementation of Order-Agnostic Binary Search:

Let us see the implementation of Order-Agnostic Binary Search with the help of an example.

Given an array, arr[ ] of size N and an element X and the array is sorted in any order(ascending or descending), the task is to find whether the element x is present in the array or not. If yes, then print its index, else print -1.

Examples:


Input: arr[] = {40, 10, 5, 2, 1}, N=5, X=10
Output: 1
Explanation: 
 





The array is sorted in descending order and the element is present at index 1.


Input: arr[] = {1}, N=1, X=10
Output: -1