class Solution(object):
    def longestCommonPrefixBnTwo(self, str1, str2):
        comm_pref = ""
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]: comm_pref += str1[i]
            else: break
        return comm_pref
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        common = strs[0]
        for i in range(1, len(strs)):
            common = self.longestCommonPrefixBnTwo(common, strs[i])
        return common