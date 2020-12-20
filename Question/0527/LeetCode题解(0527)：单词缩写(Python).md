# LeetCode题解(0527)：单词缩写(Python)

题目：[原题链接](https://leetcode-cn.com/problems/word-abbreviation/)（困难）

标签：字符串、排序、字典树、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 2296ms (6.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
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
```