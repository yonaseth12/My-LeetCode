class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sorted_list = []
        activeRange = []
        for i in nums:
            if not activeRange:
                activeRange.append(i)
            else:
                if i - activeRange[-1] == 1:
                    if len(activeRange) == 1:
                        activeRange.append(i)
                    else:
                        activeRange[1] = i
                else:
                    if len(activeRange) == 1:
                        sorted_list.append(str(activeRange[0]))
                    else:
                        sorted_list.append(str(activeRange[0]) + "->" + str(activeRange[1]))
                    activeRange = [i]
                    
        if activeRange:
            if len(activeRange) == 1:
                sorted_list.append(str(activeRange[0]))
            else:
                sorted_list.append(str(activeRange[0]) + "->" + str(activeRange[1]))
        return sorted_list
                
        