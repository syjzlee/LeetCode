# 给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
#
# 如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。
#
# 注意你不能在买入股票前卖出股票。
#
# 示例 1:
#
# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
# 示例 2:
#
# 输入: [7,6,4,3,1]
# 输出: 0
# 解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。



"""
最大的利润可以看成是上一位置的最大利润与当前数字比较后更大的利润。
f(n)= max(f(n-1), prices[n]-min(prices[:n))
还是那句话后面的由前面的向上铺垫而成
"""
class Solution:
    def maxProfit(self, prices):
        max_profit = [0 for _ in prices]
        if len(prices) <= 1:
            return 0
        min_price = sys.maxsize
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            max_profit[i] = max(max_profit[i-1], prices[i] - min_price)

        return max_profit[-1]




class Solution2:
    def maxProfit(self, prices):
        maxPro = 0
        low = sys.maxsize
        for i in range(len(prices)):
            if low > prices[i]:
                low = prices[i]
            maxPro = max(maxPro, prices[i] - low)
        return maxPro
