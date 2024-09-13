class Solution:
    def xorQueries(self, arr, queries):
        n = len(arr)
        # Compute prefix XORs for efficient query processing
        prefix_xor = [0] * (n + 1)  
        for i in range(n):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]
        
        # Process each query using the precomputed prefix XOR values
        answer = []
        for left, right in queries:
            answer.append(prefix_xor[right + 1] ^ prefix_xor[left])
        
        return answer