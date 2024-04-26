class Solution(object):
    def minFallingPathSumII(self, A):
        n = len(A)
        if n == 1:
            return A[0][0]
        
        prev_min, prev_secmin, prev_ind = float('inf'), float('inf'), -1
        
        for i in range(n):
            cur_min, cur_secmin, cur_ind = float('inf'), float('inf'), -1
            
            for j in range(n):
                curr_val = A[i][j] + (prev_min if prev_ind != j else prev_secmin)
                
                if curr_val < cur_min:
                    cur_secmin, cur_min = cur_min, curr_val
                    cur_ind = j
                elif curr_val < cur_secmin:
                    cur_secmin = curr_val
        
            prev_min, prev_secmin, prev_ind = cur_min, cur_secmin, cur_ind
    
        return prev_min