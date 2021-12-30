# rank is the width of the matrix
# level is the layer of the matrix, starting from the outest layer
def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 0:
            return matrix
        rank = len(matrix)
        level = 0
        while(level <= rank // 2):
            length = rank - level * 2
            for i in range(0, length - 1):
                temp = matrix[level][level + i]
                matrix[level][level + i] = matrix[level + length - 1 - i][level]
                matrix[level + length - 1 - i][level] = matrix[level + length - 1][level + length - 1 - i]
                matrix[level + length - 1][level + length - 1 - i] = matrix[level + i][level + length - 1]
                matrix[level + i][level + length - 1] = temp
            level += 1
        return matrix