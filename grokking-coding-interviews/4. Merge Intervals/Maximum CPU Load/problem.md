Given an array of jobs with different time requirements, where each job consists of start time, end time and CPU load. 

The task is to find the maximum CPU load at any time if all jobs are running on the same machine.

Examples: 


Input: jobs[] = {{1, 4, 3}, {2, 5, 4}, {7, 9, 6}} 
Output: 7 
Explanation: 
In the above-given jobs, there are two jobs which overlaps. 
That is, Job [1, 4, 3] and [2, 5, 4] overlaps for the time period in [2, 4] 
Hence, the maximum CPU Load at this instant will be maximum (3 + 4 = 7).


Input: jobs[] = {{6, 7, 10}, {2, 4, 11}, {8, 12, 15}} 
Output: 15 
Explanation: 
Since, There are no jobs that overlaps. 
Maximum CPU Load will be – max(10, 11, 15) = 15  