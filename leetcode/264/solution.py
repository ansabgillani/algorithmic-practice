class Solution:
    def nthUglyNumber(self, n: int) -> int:
        """
        Finds the n-th ugly number.
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return None
        
        ugly_numbers = [1]
        i2 = i3 = i5 = 0
        
        while len(ugly_numbers) < n:
            next_ugly = min(ugly_numbers[i2] * 2, ugly_numbers[i3] * 3, ugly_numbers[i5] * 5)
            ugly_numbers.append(next_ugly)
            
            if next_ugly == ugly_numbers[i2] * 2:
                i2 += 1
            if next_ugly == ugly_numbers[i3] * 3:
                i3 += 1
            if next_ugly == ugly_numbers[i5] * 5:
                i5 += 1
        
        return ugly_numbers[n - 1]