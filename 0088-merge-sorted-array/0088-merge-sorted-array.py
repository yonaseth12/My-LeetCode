class Solution(object):
    def insertInPlace(self, nums, index, a):
        tempCarried = nums[index]
        nums[index] = a
        pointer = index + 1
        while pointer < len(nums):
            tempCurrent = nums[pointer]
            nums[pointer] = tempCarried
            pointer += 1
            tempCarried = tempCurrent
        return nums
            
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        n1_index, n2_index = 0, 0
        offsetInNums1 = 0
        while n1_index < m + offsetInNums1 and n2_index < n:
            if nums2[n2_index] <= nums1[n1_index]:
                nums1 = self.insertInPlace(nums1, n1_index, nums2[n2_index])
                print(n1_index, n2_index, nums1)
                offsetInNums1 += 1
                n1_index += 1
                n2_index += 1
            else: n1_index += 1
        if n2_index != n:
            nums1[n1_index:] = nums2[n2_index:]
        