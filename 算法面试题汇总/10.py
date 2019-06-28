# 给定一个二维网格 board 和一个字典中的单词列表 words，找出所有同时在二维网格和字典中出现的单词。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
#
# 示例:
# 输入:
# words = ["oath","pea","eat","rain"] and board =
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
#
# 输出: ["eat","oath"]
# 说明:
# 你可以假设所有输入都由小写字母 a-z 组成。
#
# 提示:
# 你需要优化回溯算法以通过更大数据量的测试。你能否早点停止回溯？
# 如果当前单词不存在于所有单词的前缀中，则可以立即停止回溯。什么样的数据结构可以有效地执行这样的操作？散列表是否可行？为什么？ 前缀树如何？如果你想学习如何实现一个基本的前缀树，请先查看这个问题： 实现Trie（前缀树）。

class Solution:
    def findWords(self, board, words):
        if not words or not board:
            return []
        result = []
        for word in words:
            if self.findWord(board, word):
                result.append(word)
        return result

    def findWord(self, board, word):
        # 首先应该是定位第一个字母的位置 x，y
        for i in range(len(board)):
            for j in range(len(board[0])):
                x, y = j, i
                if self.findnextchar(board, x, y, 0, word, []):
                    print('zai')
                    return True
        return False

    def findnextchar(self, board, x, y, index, word, result):
        print(result, len(result),' |', board[y][x], word[index])
        #  result为空了，且
        if not result and board[y][x] != word[index]:
            return False

        # 控制不能走重复的路线
        if board[y][x] == word[index]:
            result.append((x, y))
            index += 1
            print(index)
            # 完整匹配了
            if index == len(word):
                return True
            # 上
            if 0 <= y-1 < len(board) and (x,y-1) not in result:
                if self.findnextchar(board, x, y-1, index, word, result):
                    return True
            # 下：
            if 0 <= y+1 < len(board) and (x,y+1) not in result:
                if self.findnextchar(board, x, y+1, index, word, result):
                    return True
            # 左：
            if 0 <= x-1 < len(board[0]) and (x-1,y) not in result:
                if self.findnextchar(board, x-1, y, index, word, result):
                    return True
            # 右：
            if 0 <= x+1 < len(board[0]) and (x+1,y) not in result:
                if self.findnextchar(board, x+1, y, index, word, result):
                    return True



solution = Solution()
words =["bbaabaabaaaaabaababaaaaababb"]
board =[["b","a","a","b","a","b"],
        ["a","b","a","a","a","a"],
        ["a","b","a","a","a","b"],
        ["a","b","a","b","b","a"],
        ["a","a","b","b","a","b"],
        ["a","a","b","b","b","a"],
        ["a","a","b","a","a","b"]]
print(solution.findWords(board, words))
