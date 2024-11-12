class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if digits[-1] == 9:
            digits[-1] = 0
            carry = 1
            if len(digits) == 1:
                digits.insert(0, 1)
                return digits
            for i in range(len(digits)-2, -1, -1):
                if carry == 1:
                    if digits[i] == 9:
                        digits[i] = 0
                        carry = 1
                        if i == 0: digits.insert(0, 1)
                    else:
                        digits[i] += 1
                        carry = 0
                else: return digits
        else:
            digits[-1] += 1
        
        return digits