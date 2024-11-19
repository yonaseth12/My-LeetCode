class Solution(object):
    def maximumSetSize(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # create dict for both with key: num and value: repetition
        # select the dict with the smallest number of pairs - call it small_dict
        # set cunter_tracker ct_small for the small dict, initialize with n/2
        # while ct_small > 0: add to s if not in big_dict, del the element , ct_small--
        # if ct_small is not 0: add from small_dict until
        # ct_big
        # while ct_big > 0: add to s if not in ct_small
        # return the len(s)
        
        dict_1, dict_2 = {}, {}
        for i in nums1:
            if i in dict_1:
                dict_1[i] += 1
            else: dict_1[i] = 1
        for j in nums2:
            if j in dict_2:
                dict_2[j] += 1
            else: dict_2[j] = 1
                
        if len(dict_1) <= len(dict_2):
            smaller_dict = dict_1
            bigger_dict = dict_2
        else:
            smaller_dict = dict_2
            bigger_dict = dict_1
        
        s = set()
        
        ct_small = len(nums1) // 2
        for key, value in list(smaller_dict.items()):
            if ct_small == 0: break
            if key not in bigger_dict:
                s.add(key)
                ct_small -= 1
                del smaller_dict[key]
        if ct_small != 0:      # n/2 elements must be added, so common elements may be added
            while ct_small > 0 and smaller_dict:
                s.add(smaller_dict.popitem()[0])
                ct_small -= 1
        
        ct_big = len(nums1) // 2
        for key, value in list(bigger_dict.items()):
            if ct_big == 0: break
            if key not in s:
                s.add(key)
                ct_big -= 1
                del bigger_dict[key]
        
        return len(s)
                