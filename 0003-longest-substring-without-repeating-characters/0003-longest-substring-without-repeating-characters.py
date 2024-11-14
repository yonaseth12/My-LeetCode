class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 1: return 1
        longest_start = 0
        longest_end = 1
        start_index = 0
        end_index = 1
        while end_index < len(s):
            if s[end_index] not in s[start_index: end_index]:
                end_index += 1
                if(end_index - start_index) > (longest_end - longest_start):
                    longest_start = start_index
                    longest_end = end_index
                    
            else:
                start_index += 1
                
        return len(s[longest_start: longest_end])
        