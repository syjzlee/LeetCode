# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：
#
# 每行的元素从左到右升序排列。  每列的元素从上到下升序排列。
# 示例:
# 现有矩阵 matrix 如下：
# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# 给定 target = 5，返回 true。
# 给定 target = 20，返回 false。

class Solution :
    def searchMatrix(self, matrix, target) :
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # 上次从右上角开始的。   这次咱从左下角开始
        row,col = len(matrix)-1,0
        while(row>=0 and col<=len(matrix[0]) - 1):
            if matrix[row][col] < target:
                col += 1
            elif matrix[row][col] > target:
                row -= 1
            else:
                return True
        return False


matrix = [[ 1, 3, 5, 7, 9],
          [ 2, 4, 6, 8,10],
          [11,13,15,17,19],
          [12,14,16,18,20],
          [21,22,23,24,25]]
target = 11
Solution = Solution()
print(Solution.searchMatrix(matrix, target))