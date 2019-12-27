# Best Time to Buy and Sell Stock with Cooldown
# 给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​
#
# 设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
#
# 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
# 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
# 示例:
#
# 输入: [1,2,3,0,2]
# 输出: 3
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

"""
想状态转移方程，上述例子中结果[0,1,2,2,3],  买入、卖出、冷冻期、买入、卖出
状态转移方程，第i天可能的情况是手上有股票和手上没有股票。设没有股票的最大收益为
cash[i],有股票的最大收益为hold[i]，则：
cash[i] = max(昨天手里有股票的收益+今天卖股票的收益，昨天手里没有股票的收益)， 即max(cash[i-1], hold[i-1] + prices[i])；
hold = max(今天买股票是前天卖掉股票的收益-今天股票的价格，昨天手里有股票的收益）。即max(hold[i-1], cash[i-2] - prices[i])。
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        sell = [0] * len(prices)
        hold = [0] * len(prices)
        hold[0] = -prices[0]
        for i in range(1, len(prices)):
            sell[i] = max(sell[i - 1], hold[i - 1] + prices[i])
            hold[i] = max(hold[i - 1], (sell[i - 2] if i >= 2 else 0) - prices[i])
        return sell[-1]
