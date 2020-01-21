# 斐波那契数，通常用
# F(n)
# 表示，形成的序列称为斐波那契数列。该数列由
# 0
# 和
# 1
# 开始，后面的每一项数字都是前面两项数字的和。也就是：
#
# F(0) = 0, F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中
# N > 1.
# 给定
# N，计算
# F(N)。
#
#
#
# 示例
# 1：
#
# 输入：2
# 输出：1
# 解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
# 示例
# 2：
#
# 输入：3
# 输出：2
# 解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
# 示例
# 3：
#
# 输入：4
# 输出：3
# 解释：F(4) = F(3) + F(2) = 2 + 1 = 3.


class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            result = self.fib(N-1) + self.fib(N-2)
            return result


    catch = {0: 0, 1: 1}
    def fib_memory(self, N: int) -> int:
        # 记忆版本
        if N not in self.catch:
            self.catch[N] = self.fib_memory(N - 1) + self.fib_memory(N - 2)

        return self.catch[N]

