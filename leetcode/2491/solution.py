from typing import List

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        """
        Divide players into teams of equal skill and return the sum of team chemistries.
        If not possible to divide the players as per requirement, return -1.
        
        :param skill: List of player skills
        :return: Sum of team chemistries or -1 if division is not possible
        """
        total_skill = sum(skill)
        num_teams = len(skill) // 2
        
        # Check if equal division is possible
        if total_skill % num_teams != 0:
            return -1
        
        target_team_skill = total_skill // num_teams
        skill.sort()
        
        left, right = 0, len(skill) - 1
        chemistry_sum = 0
        
        while left < right:
            current_team_skill = skill[left] + skill[right]
            if current_team_skill != target_team_skill:
                return -1
            chemistry_sum += skill[left] * skill[right]
            left += 1
            right -= 1
        
        return chemistry_sum

# Example usage:
solution = Solution()
print(solution.dividePlayers([3,2,5,1,3,4]))  # Output: 22
print(solution.dividePlayers([3,4]))         # Output: 12
print(solution.dividePlayers([1,1,2,3]))     # Output: -1