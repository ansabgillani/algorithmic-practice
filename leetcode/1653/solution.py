class Solution:
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Calculate prefix sum of 'b' counts
        b_prefix_sum = [0] * (len(s) + 1)
        for i in range(len(s)):
            b_prefix_sum[i+1] = b_prefix_sum[i] + (s[i] == 'b')

        min_deletions = float('inf')
        a_count = 0

        # Iterate through the string and calculate deletions
        for i in range(len(s)):
            if s[i] == 'a':
                a_count += 1
            else:
                b_count = b_prefix_sum[len(s)] - b_prefix_sum[i+1]
                min_deletions = min(min_deletions, a_count + b_count)

        return min(min_deletions, a_count, b_prefix_sum[-1])