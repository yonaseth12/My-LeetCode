class Solution(object):
        
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_seq = []
        for i in nums:
            if not curr_seq:
                curr_seq.append(i)
            elif i-1==curr_seq[-1]: curr_seq.append(i)
            else:
                break
        sum = 0
        for i in curr_seq:
            sum += i
        min_miss = sum
        if min_miss not in nums: return min_miss
        else:
            min_miss += 1
            above_sum = set()
            for i in nums:
                if i > sum: above_sum.add(i)
            while True:
                if min_miss in above_sum:
                    min_miss += 1
                    continue
                return min_miss
