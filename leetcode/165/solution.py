class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split('.'), version2.split('.')
        
        for i in range(max(len(v1), len(v2))):
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0
            
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
    
        return 0