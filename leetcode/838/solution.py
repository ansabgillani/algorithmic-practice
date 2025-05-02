class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        forces = [0] * n
        
        # Apply force from left to right
        f = 0
        for i in range(n):
            if dominoes[i] == 'R':
                f = n
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f - 1, 0)
            forces[i] += f
        
        # Apply force from right to left
        f = 0
        for i in range(n-1, -1, -1):
            if dominoes[i] == 'L':
                f = n
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f - 1, 0)
            forces[i] -= f
        
        # Determine the final state based on forces
        result = []
        for force in forces:
            if force > 0:
                result.append('R')
            elif force < 0:
                result.append('L')
            else:
                result.append('.')
        
        return ''.join(result)