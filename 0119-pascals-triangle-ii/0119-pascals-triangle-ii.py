class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowNum = rowIndex + 1
        previous_row = [1,1]    # Starting case (row number two)
        if rowNum == 1: return [1]
        elif rowNum == 2: return previous_row
        else:
            for i in range(3, rowNum+1):
                new_row = [1]
                for j in range(len(previous_row)-1):
                    new_row.append(previous_row[j] + previous_row[j+1])
                new_row.append(1)
                previous_row = new_row
            return previous_row
            