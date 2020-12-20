# LeetCode题解(0425)：单词方块(Python)

题目：[原题链接](https://leetcode-cn.com/problems/word-squares/)（困难）

标签：回溯算法、字典树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(W×L^2)$ | $O(W×L^2)$ | 264ms (97.67%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
def build_tree(words):
    tree = {}
    for i, word in enumerate(words):
        node = tree
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["@"] = i
    return tree


class Solution:
    def __init__(self):
        self.words = []
        self.size = 0
        self.tree = {}
        self.dic = collections.defaultdict(list)

    def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.words = words
        self.size = len(words[0])

        # 构造字典树
        self.tree = build_tree(words)

        # 构造开头字母对应字典
        for word in words:
            for i in range(self.size):
                self.dic[word[0:i + 1]].append(word)

        ans = []

        for word in words:
            ans.extend(self.check(word))

        ans.sort()

        return ans

    def check(self, word):
        """检查指定词语"""
        nodes = []
        for i in range(self.size):
            node = self.tree
            nodes.append(node)

        find = True
        for i in range(self.size):
            if word[i] in nodes[i]:
                nodes[i] = nodes[i][word[i]]
            else:
                find = False
                break

        if not find:
            return []

        return self.count([word], word, nodes)

    def count(self, path, word1, nodes):
        """寻找下一行的词语"""
        idx = len(path)

        # 处理递归完成的情况
        if idx == self.size:
            return [path]

        # 寻找已经被确定的字符
        confirm = []
        for i in range(idx):
            confirm.append(path[i][idx])
        confirm = "".join(confirm)

        ans = []

        for word2 in self.dic[confirm]:
            new_nodes = []
            for i in range(self.size):
                if word2[i] in nodes[i]:
                    new_nodes.append(nodes[i][word2[i]])
                else:
                    break
            else:
                ans.extend(self.count(path + [word2], word1, new_nodes))

        return ans
```