from collections import deque

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_counts = [0] * (n + 1)

        # Apply the difference array technique to efficiently compute cumulative shifts
        for start, end, direction in shifts:
            if direction == 1:
                shift_counts[start] += 1
                shift_counts[end + 1] -= 1
            else:
                shift_counts[start] -= 1
                shift_counts[end + 1] += 1

        # Compute the cumulative sum to get the actual number of shifts for each character
        for i in range(1, n + 1):
            shift_counts[i] += shift_counts[i - 1]

        # Apply the shifts to the string
        result = []
        for i in range(n):
            original_char = s[i]
            shift_amount = shift_counts[i]
            if ord('a') <= ord(original_char) <= ord('z'):
                new_char = chr((ord(original_char) - ord('a') + shift_amount) % 26 + ord('a'))
            else:
                raise ValueError("Character out of expected range")
            result.append(new_char)

        return ''.join(result)