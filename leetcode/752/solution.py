class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if '0000' in dead or target in dead:
            return -1
        
        q = deque([('0000', 0)])
        visited = {}
        visited['0000'] = True
        
        while q:
            curr, step = q.popleft()
            
            if curr == target:
                return step
            
            for i in range(4):
                digit = int(curr[i])
                
                # Turn clockwise
                nxt_digit = (digit + 1) % 10
                nxt_code = curr[:i] + str(nxt_digit) + curr[i+1:]
                
                if nxt_code not in visited and nxt_code not in dead:
                    q.append((nxt_code, step + 1))
                    visited[nxt_code] = True
                    
                # Turn counterclockwise
                prev_digit = (digit - 1) % 10
                prev_code = curr[:i] + str(prev_digit) + curr[i+1:]
                
                if prev_code not in visited and prev_code not in dead:
                    q.append((prev_code, step + 1))
                    visited[prev_code] = True
        
        return -1