class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return None
        idx = 0
        while idx < len(nums):
            if nums[idx] != 0:
                idx += 1
                continue
            #Swap with the first non zero element
            nz_idx = idx
            while nz_idx < len(nums):
                if nums[nz_idx] != 0:
                    nums[idx], nums[nz_idx] = nums[nz_idx], nums[idx]
                    break
                nz_idx += 1
            idx += 1