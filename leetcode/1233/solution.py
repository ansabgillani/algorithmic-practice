class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """
        Remove all sub-folders from the given list of folders.
        
        :param folder: List of folder paths
        :return: List of folder paths after removing sub-folders
        """
        # Sort folders lexicographically to handle sub-folder relationships easily
        folder.sort()
        result = [folder[0]]
        
        for i in range(1, len(folder)):
            if not folder[i].startswith(result[-1] + '/'):
                result.append(folder[i])
        
        return result

# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"])) 
    # Output: ["/a", "/c/d", "/c/f"]
    
    # Example 2
    print(sol.removeSubfolders(["/a", "/a/b/c", "/a/b/d"])) 
    # Output: ["/a"]
    
    # Example 3
    print(sol.removeSubfolders(["/a/b/c", "/a/b/ca", "/a/b/d"])) 
    # Output: ["/a/b/c", "/a/b/ca", "/a/b/d"]