# 跳跃游戏
# 给定一个非负整数数组，你最初位于数组的第一个位置。
#
# 数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个位置。
#
# 示例 1:
#
# 输入: [2,3,1,1,4]
# 输出: true
# 解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
# 示例 2:
#
# 输入: [3,2,1,0,4]
# 输出: false
# 解释: 无论怎样，你总会到达索引为 3 的位置。但该位置的最大跳跃长度是 0 ， 所以你永远不可能到达最后一个位置。

"""
尴尬第一次竟然没理解题啥意思。。。。。。
索引表示的是位置，第一个索引0代表的就是位置0，所以最后一个位置其实就是n-1， 每一个索引具体的值是从该位置跳最大能跳多远，不是像摇色子
一样跳到固定远。
因为要跳到下一个位置，肯定是要由之前的有限个位置跳跃上来的（因为n是有限的，方案肯定有限，但是肯定不一定必须从n-1上跳上来），
想到能用动态规划去解（因为到目前思维过程已经是自底向上了，只不过直观想好像方程右边因子个数不确定，所以我们要继续构建）。
而要想因子个数固定的（最好是两个的）状态转移方程，在本例中只要能想到到达第i个位置还能够剩余的最大跳跃长度就OK了
例如到达位置i的剩余最大跳跃长度 f(i)= max(f(n-1)-1, nums[i-1]-1) , -1是因为从i-1跳到i还需要1个跳跃长度。
"""

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        result = [_ for _ in nums]
        if len(nums) == 0:
            return False
        if len(nums) == 1:
            return True
        for i in range(1, len(nums)):
            result[i] = max(nums[i-1]-1, result[i-1]-1)
            if result[i] < 0:       # 忘记加这层了。。。。。。。
                return False

        return result[-1] >= 0



# 还可以用贪婪算法。