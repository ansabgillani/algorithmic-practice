class Solution:
    def numberToWords(self, num: int) -> str:
        # Helper functions to convert numbers less than 20 and multiples of ten
        def ones(num):
            switcher = {
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            }
            return switcher.get(num, '')

        def tens(num):
            switcher = {
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety'
            }
            return switcher.get(num, '')

        def lessThan20(num):
            if num < 10:
                return ones(num)
            elif num < 20:
                return tens(num // 10) + (' ' + ones(num % 10)) if (num % 10 != 0) else tens(num // 10)

        # Main function to convert number to words
        def helper(num):
            billion = num // 1000000000
            million = (num - billion * 1000000000) // 1000000
            thousand = (num - billion * 1000000000 - million * 1000000) // 1000
            rest = num - billion * 1000000000 - million * 1000000 - thousand * 1000

            if not num:
                return 'Zero'
            
            result = ''
            if billion:
                result += lessThan20(billion) + ' Billion'
            if million:
                result += ' ' if result else ''
                result += lessThan20(million) + ' Million'
            if thousand:
                result += ' ' if result else ''
                result += lessThan20(thousand) + ' Thousand'
            if rest:
                result += ' ' if result else ''
                result += lessThan20(rest)

            return result.strip()

        return helper(num)