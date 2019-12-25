# 不同路径
# 一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。
#
# 机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。
#
# 问总共有多少条不同的路径？
#
#
#
# 例如，上图是一个7 x 3 的网格。有多少可能的路径？
#
# 说明：m 和 n 的值均不超过 100。
#
# 示例 1:
#
# 输入: m = 3, n = 2
# 输出: 3
# 解释:
# 从左上角开始，总共有 3 条路径可以到达右下角。
# 1. 向右 -> 向右 -> 向下
# 2. 向右 -> 向下 -> 向右
# 3. 向下 -> 向右 -> 向右
# 示例 2:
#
# 输入: m = 7, n = 3
# 输出: 28

"""这一看递归可以做，动态规划也可以做啊"""
"""动态规划思想：到达目标f(m,n)可以看成是由f(m-1,n)或者f(m,n-1)到达的，所以
f(m,n) = f(m-1,n) + f(m,n-1),这一看就是递归，但是我们主题是动态规划所以这边还是用动态规划做，自底向上"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    result[i][j] = 1
                elif i == 0:
                    result[i][j] = result[i][j-1]
                elif j == 0:
                    result[i][j] = result[i-1][j]
                else:
                    result[i][j] = result[i-1][j] + result[i][j-1]

        return result[-1][-1]