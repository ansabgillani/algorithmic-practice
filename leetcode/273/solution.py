class Solution:
    def numberToWords(self, num):
        if num == 0:
            return 'Zero'
        
        under_20 = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        thousands = ['', 'Thousand', 'Million', 'Billion']

        def helper(num):
            if num < 20:
                return under_20[num]
            elif num < 100:
                return tens[num//10] + (' ' + under_20[num%10] if num % 10 != 0 else '')
            else:
                return under_20[num//100] + ' Hundred ' + helper(num % 100)

        result = ''
        i = 0
        while num > 0:
            if num % 1000 != 0:
                result = helper(num%1000) + thousands[i] + ' ' + result
            num //= 1000
            i += 1
        
        return result.strip()