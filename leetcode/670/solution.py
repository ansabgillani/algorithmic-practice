class Solution:
    def maximumSwap(self, num):
        if not num:
            return 0
        
        str_num = list(str(num))
        max_index = [-1] * 10
        for i, digit in enumerate(str_num):
            max_index[int(digit)] = i

        for i, digit in enumerate(str_num):
            for j in range(9, int(digit), -1):
                if max_index[j] > i:
                    str_num[i], str_num[max_index[j]] = str_num[max_index[j]], str_num[i]
                    return int(''.join(str_num))

        return num