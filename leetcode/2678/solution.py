class Solution:
    def countSeniors(self, details: List[str]) -> int:
        """
        Counts the number of passengers who are strictly more than 60 years old.
        
        Args:
        details (List[str]): A list of passenger details where each detail is a string of length 15.
        
        Returns:
        int: The count of passengers older than 60 years.
        """
        # Initialize the count of senior citizens
        senior_count = 0
        
        # Iterate through each detail in the list
        for detail in details:
            # Extract the age from the string (characters at indices 11 and 12)
            age = int(detail[11:13])
            
            # Check if the age is greater than 60
            if age > 60:
                senior_count += 1
        
        return senior_count

# Example usage:
solution = Solution()
print(solution.countSeniors(["7868190130M7522", "5303914400F9211", "9273338290F4010"]))  # Output: 2
print(solution.countSeniors(["1313579440F2036", "2921522980M5644"]))  # Output: 0