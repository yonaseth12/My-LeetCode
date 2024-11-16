class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_pair = {')':'(' , '}':'{', ']':'['}
        opening_set = list(bracket_pair.values())
        stack = []
        if s == "": return True
        if s[0] not in opening_set: return False
        for char in s:
            if char in opening_set: stack.append(char)
            else:
                if len(stack) == 0: return False
                if stack[-1] == bracket_pair[char]: stack.pop()
                else: return False
        
        if len(stack) > 0: return False
        return True