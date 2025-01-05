class Solution:
    def shiftingLettersII(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_arr = [0] * (n + 1)

        for start, end, direction in shifts:
            if direction == 1:
                shift_arr[start] += 1
                shift_arr[end + 1] -= 1
            else:
                shift_arr[start] -= 1
                shift_arr[end + 1] += 1

        for i in range(1, n):
            shift_arr[i] += shift_arr[i - 1]

        result = []
        for char, shift in zip(s, shift_arr[:-1]):
            shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            result.append(shifted_char)

        return ''.join(result)