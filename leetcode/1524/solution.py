class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        Return the number of sub-arrays with an odd sum.
        
        :param arr: List of integers representing the array.
        :return: Number of sub-arrays with an odd sum, modulo 10^9 + 7.
        """
        MOD = 10**9 + 7
        prefix_sum = [0]
        curr_sum = 0
        count_odd = count_even = 0
        
        for num in arr:
            curr_sum += num
            if curr_sum % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
            
            count_odd += even_count
            count_even += odd_count
        
        return (count_odd) % MOD