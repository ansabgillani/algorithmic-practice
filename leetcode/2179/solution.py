class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        # Create a mapping from value to index in nums2
        index_map = {num: i for i, num in enumerate(nums2)}
        
        # Transform nums1 into an array of indices in nums2
        transformed = [index_map[num] for num in nums1]
        
        # Function to count the number of increasing subsequences of length 3
        def count_increasing_subsequences(arr):
            n = len(arr)
            left_smaller = [0] * n
            right_larger = [0] * n
            
            # Count smaller elements on the left for each element
            stack = []
            for i in range(n):
                while stack and arr[stack[-1]] < arr[i]:
                    left_smaller[i] += 1
                    stack.pop()
                stack.append(i)
            
            # Clear the stack for reuse
            stack.clear()
            
            # Count larger elements on the right for each element
            for i in range(n - 1, -1, -1):
                while stack and arr[stack[-1]] > arr[i]:
                    right_larger[i] += 1
                    stack.pop()
                stack.append(i)
            
            # Sum up the number of good triplets
            count = 0
            for i in range(n):
                if left_smaller[i] > 0 and right_larger[i] > 0:
                    count += left_smaller[i] * right_larger[i]
            
            return count
        
        # Return the count of good triplets
        return count_increasing_subsequences(transformed)