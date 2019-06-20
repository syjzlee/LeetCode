# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，在字符串中增加空格来构建一个句子，使得句子中所有的单词都在词典中。返回所有这些可能的句子。
# 说明：
# 分隔时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。

# 示例 1：
# 输入:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# 输出:
# [
#   "cats and dog",
#   "cat sand dog"
# ]

# 示例 2：
# 输入:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# 输出:
# [
#   "pine apple pen apple",
#   "pineapple pen apple",
#   "pine applepen apple"
# ]
# 解释: 注意你可以重复使用字典中的单词。
# 示例 3：
#
# 输入:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出:
# []

""" 自底向上的动态规划问题 （就是记忆型的跌追求解）"""
class Solution2:
    def wordBreak(self, s, wordDict):
        if wordDict == []:
            return []
        wordSet = set(wordDict)
        dp_tf = [False for i in range(len(s))]
        dp = [[] for i in range(len(s))]
        min_len = min(map(lambda x: len(x), wordDict))
        max_len = max(map(lambda x: len(x), wordDict))
        print(min_len, max_len)
        for i in range(min_len-1, len(s)):
            if s[:i+1] in wordSet:
                dp_tf[i] = True
            else:
                for j in range(i-max_len, i-min_len+1):
                    if j >= 0 and dp_tf[j] and s[j+1:i+1] in wordSet:
                        dp_tf[i] = True
                        break
        print(dp_tf)
        if not dp_tf[-1]:
            return []
        for i in range(min_len - 1, len(s)):
            if s[:i + 1] in wordSet:
                dp[i].append(s[:i + 1])
            for j in range(i - max_len, i - min_len + 1):
                if j >= 0 and dp[j] and s[j + 1:i + 1] in wordSet:
                    for l in dp[j]:
                        dp[i].append(l + ' ' + s[j + 1:i + 1])

        return dp[-1]


class Solution:
    def wordBreak(self, s, wordDict):
        maxlen = 0
        for i in wordDict:
            if len(i) > maxlen:
                maxlen = len(i)

        # 先检测是否可拆分
        res = [0 for _ in s]
        for i in range(len(s)):
            p = i
            while (i - p <= maxlen and p >= 0):
                if (p == 0 and s[p:i + 1] in wordDict) or (res[p]==1 and s[p + 1:i + 1] in wordDict):
                    res[i] = 1
                p -= 1
        if res[-1] == 0:
            return []

        res = [[] for _ in s]
        for i in range(len(s)):
            p = i
            while(i-p<=maxlen and p>=0):
                if p==0 and s[p:i+1] in wordDict:
                    res[i].append(s[p:i+1])
                if res[p] and s[p+1:i+1] in wordDict:
                    for str in res[p]:
                        str += ' ' + s[p+1:i+1]
                        res[i].append(str)
                p-=1
        return res[-1]

solution = Solution()
# print(solution.wordBreak('pineapplepenapple', ["apple", "pen", "applepen", "pine", "pineapple"]))
# print(solution.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"]))
# print(solution.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]))
print(solution.wordBreak('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))


