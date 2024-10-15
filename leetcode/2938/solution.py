class Solution:
    def minimum_steps(self, s):
        count, black_ball_index = 0, s.rfind('1') + 1

        for i in range(black_ball_index):
            if s[i] == '1':
                count += black_ball_index - i
                black_ball_index += 1

        return count