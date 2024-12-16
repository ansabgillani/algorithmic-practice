Climbing stairs to reach the top
Last Updated : 11 Jan, 2025
There are n stairs, and a person standing at the bottom wants to climb stairs to reach the top. The person can climb either 1 stair or 2 stairs at a time, the task is to count the number of ways that a person can reach at the top.

Note: This problem is similar to Count ways to reach Nth stair (Order does not matter) with the only difference that in this problem, we count all distinct ways where different orderings of the steps are considered unique.

Examples:

Input: n = 1                                                                                                                                                 
Output: 1 
Explanation: There is only one way to climb 1 stair.                                                                                          


Input: n = 2
Output: 2 
Explanation: There are two ways to reach 2th stair: {1, 1} and {2}.  


Input: n = 4 
Output: 5 
Explanation: There are five ways to reach 4th stair: {1, 1, 1, 1}, {1, 1, 2}, {2, 1, 1}, {1, 2, 1} and {2, 2