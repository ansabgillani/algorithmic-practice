class HouseRobber:
    def rob(self, hval: List[int]) -> int:
        """
        :type hval: List[int]
        :rtype: int
        """
        if not hval:
            return 0
        elif len(hval) == 1:
            return hval[0]
        
        n = len(hval)
        dp = [0] * n
        dp[0], dp[1] = hval[0], max(hval[0], hval[1])
        
        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + hval[i])
        
        return dp[n-1]