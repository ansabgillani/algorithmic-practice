class Solution:
    def removeSubfolders(self, folder):
        folder.sort()  # Sort folders lexicographically to ensure parent paths come before sub-paths
        res = [folder[0]]  # Initialize result list with the first folder

        for path in folder[1:]:  # Start from the second folder and iterate through all folders
            if not path.startswith(res[-1] + '/'):  # Check if current folder is a sub-folder of the last folder in result
                res.append(path)  # If it's not, add it to result

        return res  # Return the list of non-sub-folders