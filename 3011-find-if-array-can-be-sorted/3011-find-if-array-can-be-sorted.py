class Solution(object):
    def hasSameSetBits(self, num1, num2):
        sb1 = bin(num1).count('1')
        sb2 = bin(num2).count('1')
        if sb1 == sb2: return True
        else: return False
        
    def canSortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 1: return True
        idx = 1
        while idx<len(nums):
            if nums[idx] < nums[idx-1] and self.hasSameSetBits(nums[idx], nums[idx-1]):
                nums[idx-1], nums[idx] = nums[idx], nums[idx-1]
                for i in range(idx-1, 0, -1):       #pushing to the front
                    if nums[i] < nums[i-1] and self.hasSameSetBits(nums[i], nums[i-1]):
                        nums[i-1], nums[i] = nums[i], nums[i-1]
            idx += 1
        prev = nums[0]
        for i in range(1, len(nums)):
            if prev > nums[i]: return False
            prev = nums[i]
        return True