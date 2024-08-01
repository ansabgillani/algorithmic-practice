class Solution:
    def countSeniors(self, details):
        seniors = 0
        for detail in details:
            age_str = detail[11:13]
            if int(age_str) > 60:
                seniors += 1
        return seniors