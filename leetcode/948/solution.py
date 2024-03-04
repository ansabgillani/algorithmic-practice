class Solution(object):
    def bagOfTokensScore(self, tokens, P):
        """
        :type tokens: List[int]
        :type P: int
        :rtype: int
        """
        tokens.sort()
        i, j = 0, len(tokens) - 1
        score, ans = 0, 0
        
        while i <= j:
            if P >= tokens[i]:
                P -= tokens[i]
                score += 1
                i += 1
                ans = max(ans, score)
            elif score > 0 and i < j:
                P += tokens[j]
                score -= 1
                j -= 1
            else:
                break

        return ans