# 给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。
#
#
#
# 在杨辉三角中，每个数是它左上方和右上方的数的和。
#
# 示例:
#
# 输入: 5
# 输出:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
# 递推关系
# 让我们从帕斯卡三角形内的递推关系开始。
# 首先，我们定义一个函数 f(i, j)f(i,j)，它将会返回帕斯卡三角形第 i 行、第 j 列的数字。
#
# 我们可以用下面的公式来表示这一递推关系：
# f(i, j) = f(i - 1, j - 1) + f(i - 1, j)
#
#
# 基本情况
# 可以看到，每行的最左边和最右边的数字是基本情况，在这个问题中，它总是等于 1。
# 因此，我们可以将基本情况定义如下:
#
# f(i,j)=1  where  j=1 or  j=i
#
# 我们可以将 f(5,3) 分解为 f(5, 3) = f(4, 2) + f(4, 3)，然后递归地调用f(4,2) 和 f(4, 3)  （这中间会有重复计算）：



class Solution:
    def generate(self, numRows: int) -> list[list[int]]:

        def fun(n):
            if n == 1:
                return [1]
            if n == 2:
                return [1,1]
            return_list = [None] * n
            return_list[0] = 1
            return_list[n - 1] = 1
            for i in range(1, n - 1):
                return_list[i] = fun(n - 1)[i - 1] + fun(n - 1)[i]
            return return_list

        list1 = []
        for i in range(numRows):
            list1.append(fun(i + 1))
        return list1
