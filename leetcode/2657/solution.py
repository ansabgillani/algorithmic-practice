class Solution:
    def findThePrefixCommonArray(self, A, B):
        elements_in_a = set()
        prefix_common_array = []
        
        for i in range(len(A)):
            elements_in_a.add(A[i])
            
            common_count = sum(1 for x in B[:i+1] if x in elements_in_a)
            
            prefix_common_array.append(common_count)

        return prefix_common_array