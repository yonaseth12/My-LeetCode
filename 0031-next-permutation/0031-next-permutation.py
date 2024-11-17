class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1: return None
        for i in range(-2, -(len(nums)+1), -1):
            if nums[i] < nums[i+1]:
                #Finding the next greater but the least number in the right
                next_max_idx = i+1
                for j in range(i+1, 0):
                    if nums[j] > nums[i] and nums[j] < nums[next_max_idx]:
                        next_max_idx = j
                nums[i], nums[next_max_idx] = nums[next_max_idx], nums[i] 
                #sort in ascending order
                for k in range(i+1, 0):
                    min_idx = k
                    for l in range(k+1, 0):
                        if nums[l] < nums[min_idx]:
                            min_idx = l
                    nums[k], nums[min_idx] = nums[min_idx], nums[k]
                return None
        #If nothing is affected, reverse the order
        for i in range(len(nums)//2):
            nums[i], nums[-(i+1)] = nums[-(i+1)], nums[i]
         