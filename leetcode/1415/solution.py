class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if 3 * (2 ** (n-1)) < k:
            return ""
        
        res = ['a']
        
        for _ in range(1, n):
            if len(res) % 3 == 0:
                last = res[-1]
                if last == 'b':
                    res.append('c')
                else:
                    res.append('b')
            elif len(res) % 3 == 1:
                res.append('b')
            else:
                res.append('a')

        return ''.join(res)