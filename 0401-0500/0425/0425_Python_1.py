import collections
from typing import List


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


if __name__ == "__main__":
    # [
    #   [ "wall",
    #     "area",
    #     "lead",
    #     "lady"
    #   ],
    #   [ "ball",
    #     "area",
    #     "lead",
    #     "lady"
    #   ]
    # ]
    print(Solution().wordSquares(["area", "lead", "wall", "lady", "ball"]))

    # [
    #   [ "baba",
    #     "abat",
    #     "baba",
    #     "atan"
    #   ],
    #   [ "baba",
    #     "abat",
    #     "baba",
    #     "atal"
    #   ]
    # ]
    print(Solution().wordSquares(["abat", "baba", "atan", "atal"]))

    # [["aaab","aaba","abaa","baaa"],
    #  ["aaab","abaa","aaba","baaa"],
    #  ["aaba","aaab","baaa","abaa"],
    #  ["aaba","abaa","baaa","aaab"],
    #  ["abaa","baaa","aaab","aaba"],
    #  ["abaa","baaa","aaba","aaab"],
    #  ["baaa","aaab","aaba","abaa"],
    #  ["baaa","aaba","abaa","aaab"],
    #  ["baaa","abaa","aaab","aaba"],
    #  ["baaa","abaa","aaba","aaab"]]
    print(Solution().wordSquares(["abaa", "aaab", "baaa", "aaba"]))
