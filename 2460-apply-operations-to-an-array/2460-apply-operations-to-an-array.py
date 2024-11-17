class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
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
        return nums