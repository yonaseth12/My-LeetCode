class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_value_pair = {"I" : 1,
                             "V" : 5,
                             "IV": 4,
                             "IX": 9,
                             "X" : 10,
                             "L" : 50,
                             "XL": 40,
                             "XC": 90,
                             "C" : 100,
                             "D" : 500,
                             "M" : 1000,
                             "CD": 400,
                             "CM": 900,}
        if len(s) == 1:
            return symbol_value_pair[s]
        sum = 0
        i = 0
        while i < len(s):
            if s[i:i+2] in symbol_value_pair:
                sum += symbol_value_pair[s[i:i+2]]
                i += 2
            else:
                sum += symbol_value_pair[s[i]]
                i += 1
        return sum