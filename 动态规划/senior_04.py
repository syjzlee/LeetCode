# 给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。
#
# 说明：
#
# 拆分时可以重复使用字典中的单词。
# 你可以假设字典中没有重复的单词。
# 示例 1：
#
# 输入: s = "leetcode", wordDict = ["leet", "code"]
# 输出: true
# 解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
# 示例 2：
#
# 输入: s = "applepenapple", wordDict = ["apple", "pen"]
# 输出: true
# 解释: 返回 true 因为 "applepenapple" 可以被拆分成 "apple pen apple"。
#      注意你可以重复使用字典中的单词。
# 示例 3：
## 输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# 输出: false


"""
动态规划思想，将问题分步解决，每一步基于上一步的答案而进行求解。
f(i)代表以第i个字符结尾的字符串是否可被字典中的字符串拆分，
（1）首先，从开始位置，遍历寻找子字符串，若某子串str1为字典里的某个单词，则str1部分满足条件；
（2）然后，从剩余部分开始，继续遍历寻找子字符串，若某子串str2为字典里的某个单词，则str1+str2部分满足条件；
（3）以此类推，直到最终整个字符串s满足条件，则返回为true，否则，返回为false。
"""

class Solution:
    def wordBreak(self, s: str, wordDict):
        maxlen = 0
        for word in wordDict:
            if maxlen < len(word):
                maxlen = len(word)

        res = [0 for _ in s]
        for i in range(len(s)):
            p = i
            while p >= 0 and i - p <= maxlen:
                if (res[p] == 1 and s[p + 1:i + 1] in wordDict) or (p == 0 and s[p:i + 1] in wordDict):
                    # print(p, i, s[p+1:i+1], s[p:i+1])
                    res[i] = 1
                p -= 1

        return res[-1] == 1


s = Solution()
print(s.wordBreak("catsandog",["cats", "dog", "sand", "and", "cat"]))
