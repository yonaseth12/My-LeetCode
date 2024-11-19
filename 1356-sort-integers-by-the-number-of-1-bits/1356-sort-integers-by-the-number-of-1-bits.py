class Solution(object):
    def set_bit(self, num):
        return bin(num).count('1')
    
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """ 
        if len(arr) == 1: return arr
        for i in range(1, len(arr)):
            if self.set_bit(arr[i]) <= self.set_bit(arr[i-1]):
                ptr = i
                # finish down the road for this element
                while ptr > 0:
                    curr_set = self.set_bit(arr[ptr]) 
                    prev_set = self.set_bit(arr[ptr-1])
                    if curr_set == prev_set:    # sort in ascending order
                        if arr[ptr] < arr[ptr-1]:
                            arr[ptr-1], arr[ptr] = arr[ptr], arr[ptr-1]
                    elif curr_set < prev_set:
                        arr[ptr-1], arr[ptr] = arr[ptr], arr[ptr-1]
                    else: break
                    ptr -= 1
        return arr