class Solution(object):
    
    def __init__(self):
        self.memo_sum = {}
        self.list1 = []
    
    
    # This function works great but may lead to maximum allowed recursion depth exceeding
    def list_sum (self, i):
        if i in self.memo_sum: return self.memo_sum[i]
        if i == 0: return 0
        elif i<0: sum = self.list1[i] + self.list_sum(i+1)          # [i:] from back, i<0
        else: sum = self.list1[i-1] + self.list_sum(i-1)            # [:i] from front, i>0
        self.memo_sum[i] = sum
        return sum
    
    # This func prevents maximum rec. depth exceeding by starting from ends & going inward
    def initialize_memo(self, k):
        for i in range(k):
            self.memo_sum[i] = self.list_sum(i)
        for i in range(-1, -(k+1), -1):
            self.memo_sum[i] = self.list_sum(i)
        
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        self.list1 = cardPoints
        self.initialize_memo(k)
        max_sum = 0
        for i in range(k):  # if k+1 used instead of k, last case will result in slicing
                            # from [-0:] which literally means all elements (while intention 
                            # was to select no elements)
            sum1 = self.list_sum(-k+i) + self.list_sum(i)
            if sum1 > max_sum:
                max_sum = sum1
        front_sum = self.list_sum(k)       # remaining unchecked sum
        if max_sum < front_sum: max_sum = front_sum
        return max_sum