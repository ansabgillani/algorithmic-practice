class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = sorted([ch, freq] for ch, freq in dict.fromkeys(s).items())
        
        ans = ''
        while len(count) > 1:
            ch1, freq1 = count.pop()
            ch2, freq2 = count.pop()
            
            ans += ch1 * min(freq1, repeatLimit)
            if freq2 > 0:
                ans += ch2
                freq2 -= 1
            
            if freq1 > repeatLimit:
                count.append([ch1, freq1 - repeatLimit])
            if freq2 > 0:
                count.append([ch2, freq2])
    
        if len(count) == 1:
            ch, freq = count[0]
            ans += ch * min(freq, repeatLimit)
        
        return ans