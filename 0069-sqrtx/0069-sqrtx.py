class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1: return 1
        def innerSqrt(lower, upper):
            if lower==upper: return lower
            mid = (lower + upper) // 2
            if (mid+1)*(mid+1) > x >= mid*mid: return mid
            if mid*mid < x: lower=mid
            else: upper = mid
            return innerSqrt(lower, upper)
        return innerSqrt(0,x)