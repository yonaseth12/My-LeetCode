class Solution(object):
    def isInRow(self, keys_set, word):
        for char in word:
            if char not in keys_set:
                return False
        return True
    
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        keyRows = [
        {char for char in 'QWERTYUIOPqwertyuiop'},
        {char for char in 'ASDFGHJKLasdfghjkl'},
        {char for char in 'ZXCVBNMzxcvbnm'},
        ]
        filtered_words = []
        for word in words:
            print("my word is: ", word)
            if not any(self.isInRow(row, word) for row in keyRows): pass
            else: filtered_words.append(word)
        return filtered_words
        
        