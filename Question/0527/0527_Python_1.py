import collections
from typing import List


class TrieNode:
    def __init__(self):
        self.num = collections.Counter()
        self.children = collections.defaultdict(TrieNode)
        self.end = False


def build_tree(words):
    tree = TrieNode()
    for word in words:
        end = word[-1]
        node = tree
        for ch in word:
            node.num[end] += 1
            node = node.children[ch]
        node.end = True
    return tree


class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        # 依据单词长度分组单词
        dic_in_len = collections.defaultdict(list)
        for word in dict:
            if len(word) >= 3:
                dic_in_len[len(word)].append(word)

        # 构造前缀字典树
        tree_dic = {key: build_tree(dic_in_len[key]) for key in dic_in_len.keys()}

        ans = []
        for word in dict:
            if len(word) <= 3:
                ans.append(word)
            else:
                size = len(word)
                end = word[-1]
                node = tree_dic[size].children[word[0]]
                i = 1
                while node.num[end] > 1:
                    node = node.children[word[i]]
                    i += 1
                if size - i - 1 > 1:
                    ans.append(word[:i] + str(size - i - 1) + word[-1])
                else:
                    ans.append(word)

        return ans


if __name__ == "__main__":
    # ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
    print(Solution().wordsAbbreviation(
        ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]))
