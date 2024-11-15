Find m-th smallest value in k sorted arrays
Last Updated : 31 Mar, 2023
Given k sorted arrays of possibly different sizes, find m-th smallest value in the merged array.
Examples: 
 

Input: m = 5     
      arr[][] = { {1, 3},
                  {2, 4, 6},
                  {0, 9, 10, 11}} ;
Output: 4
Explanation The merged array would
be {0 1 2 3 4 6 9 10 11}.  The 5-th 
smallest element in this merged
array is 4.

Input: m = 2
      arr[][] = { {1, 3, 20},
                  {2, 4, 6}} ;
Explanation The merged array would
be {1 2 3 4 6 20}. The 2nd smallest element would be 2. 
Output: 2