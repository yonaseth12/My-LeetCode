class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        
        check_dict = {}
        for i in range(len(nums)):
            if nums[i] in check_dict:
                for index in check_dict[nums[i]]:
                    if 0 < abs(index - i) <= k: return True
                    elif abs(index-i) != 0: check_dict[nums[i]].append(i) 
            else: 
                check_dict[nums[i]] = [i]
        return False