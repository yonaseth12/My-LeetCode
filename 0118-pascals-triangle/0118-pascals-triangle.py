class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal_triangle = []
        for i in range(1, numRows+1):
            if i == 1:
                pascal_triangle.append([1])
            elif i == 2:
                pascal_triangle.append([1,1])
            else:
                upper_list = pascal_triangle[i-2]
                current_list = [1]
                for j in range(len(upper_list) - 1):
                    current_list.append(upper_list[j] + upper_list[j+1])
                current_list.append(1)
                pascal_triangle.append(current_list)
        return pascal_triangle