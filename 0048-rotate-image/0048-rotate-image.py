class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        leng = len(matrix)
        # Strategy: Rotating square then diminsh the square and repeat rotating square
        # Think the clockwise sense/direction
        # rotate the outter elements with 4 elements at once (in rotated square pattern)
        # do the above  n// 2 reps (getting inner inside each time each involving L-1 reps)
        for i in range(leng//2):    # number of times square size is reduced by 1
            for j in range(i, leng-(i+1)):
                num_lt = matrix[i][j]
                num_rt = matrix[j][(leng-1)-i]
                num_rb = matrix[(leng-1)-i][(leng-1)-j]
                num_lb = matrix[(leng-1)-j][i]
                matrix[i][j] = num_lb
                matrix[j][(leng-1)-i] = num_lt
                matrix[(leng-1)-i][(leng-1)-j] = num_rt
                matrix[(leng-1)-j][i] = num_rb