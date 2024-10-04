class Solution:
    def dividePlayers(self, skill):
        n = len(skill)
        total_skill = sum(skill)
        
        if total_skill % (n // 2) != 0:
            return -1
        
        target_team_skill = total_skill // (n // 2)
        
        skill.sort()
        
        chemistry_sum = 0
        i, j = 0, n - 1
        
        while i < j:
            if skill[i] + skill[j] != target_team_skill:
                return -1
            chemistry_sum += skill[i] * skill[j]
            i += 1
            j -= 1
        
        return chemistry_sum