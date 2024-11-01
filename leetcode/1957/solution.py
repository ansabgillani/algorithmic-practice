class Solution:
    def makeFancyString(self, s: str) -> str:
        result = [s[0]]
        prev_char = s[0]
        count = 1

        for char in s[1:]:
            if char == prev_char:
                count += 1
            else:
                result.extend([prev_char] * min(2, count))
                prev_char = char
                count = 1

        result.extend([prev_char] * min(2, count))
        return ''.join(result)