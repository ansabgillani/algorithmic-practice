class Solution:
    def longestSpecialSubstring(self, s):
        def count_substrings(k):
            cnt = 0
            i = 0
            while i < len(s) - k + 1:
                if s[i:i+k] == s[i]*k:
                    cnt += 1
                    while i < len(s) - k + 1 and s[i] == s[i+1]:
                        i += 1
                i += 1
            return cnt
        
        ans = -1
        left, right = 0, len(s)
        
        while left <= right:
            mid = (left + right) // 2
            if count_substrings(mid) >= 3:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans