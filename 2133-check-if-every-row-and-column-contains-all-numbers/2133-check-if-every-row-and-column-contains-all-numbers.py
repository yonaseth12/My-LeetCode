class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        #Check 1 : Horizontal Check
        for i in matrix:
            unique = set(range(1, len(matrix)+1))
            for j in i:
                if j in unique: unique.remove(j)
                else: return False
        #Check 2 : Vertical Check
        for i in range(len(matrix)):
            unique = set(range(1, len(matrix)+1))
            for j in range(len(matrix)):
                if matrix[j][i] in unique: unique.remove(matrix[j][i])
                else: return False
        return True