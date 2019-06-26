# 实现 Trie (前缀树)
# 实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。
#
# 示例:
#
# Trie trie = new Trie();
#
# trie.insert("apple");
# trie.search("apple");   // 返回 true
# trie.search("app");     // 返回 false
# trie.startsWith("app"); // 返回 true
# trie.insert("app");
# trie.search("app");     // 返回 true
# 说明:
#
# 你可以假设所有的输入都是由小写字母 a-z 构成的。
# 保证所有输入均为非空字符串

"数结构， 结束标记。 没啥了"

class Trie:

    def __init__(self):
        self.word_dict = {}
        for i in range(ord('a'), ord('z') + 1):
            self.word_dict[i] = {}

    def insert(self, word: str) -> None:
        now_index = self.word_dict
        for i in word:
            if i in now_index.keys():
                now_index = now_index[i]
                continue
            now_index[i] = {}
            now_index = now_index[i]
        now_index['end'] = 1

    def search(self, word: str) -> bool:
        now_index = self.word_dict
        for i in word:
            if i in now_index.keys():
                now_index = now_index[i]
                continue
            return False
        if 'end' in now_index.keys():
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        now_index = self.word_dict
        for i in prefix:
            if i in now_index.keys():
                now_index = now_index[i]
                continue
            return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

["Trie","insert","insert","insert","insert","insert","insert","search","search","search","search","search","search","search","search","search","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith","startsWith"]
[[],["app"],["apple"],["beer"],["add"],["jam"],["rental"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"],["apps"],["app"],["ad"],["applepie"],["rest"],["jan"],["rent"],["beer"],["jam"]]

[null,null,null,null,null,null,null,false,true,false,false,false,false,false,true,true,false,false,true,false,false,false,true,true,true]

[null,null,null,null,null,null,null,false,true,false,false,false,false,false,true,true,false,true,true,false,false,false,true,true,true]