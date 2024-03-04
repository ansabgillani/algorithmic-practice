class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        # Sort tokens to facilitate the face-up and face-down operations
        tokens.sort()
        
        left, right = 0, len(tokens) - 1
        score = max_score = 0
        
        while left <= right:
            if P >= tokens[left]:
                # Play token face-up
                P -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                # Play token face-down
                P += tokens[right]
                score -= 1
                right -= 1
            else:
                break
        
        return max_score