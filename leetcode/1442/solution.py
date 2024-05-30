class Solution:
    def countTriplets(self, arr):
        n = len(arr)
        count = 0
        
        for i in range(n-2):
            xor_sum = 0
            for j in range(i+1, n):
                xor_sum ^= arr[j-1]
                if xor_sum == arr[j]:
                    count += j - i
                    
        return count