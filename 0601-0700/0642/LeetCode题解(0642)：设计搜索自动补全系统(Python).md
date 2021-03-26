# LeetCode题解(0642)：设计搜索自动补全系统(Python)

题目：[原题链接](https://leetcode-cn.com/problems/design-search-autocomplete-system/)（困难）

标签：设计、字典树

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | --         | --         | 872ms (13.51%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class TrieNode:
    def __init__(self, count=0):
        self.count = count
        self.word = ""
        self.next = collections.defaultdict(TrieNode)

    def insert(self, word, time):
        """将单词插入到当前节点"""
        curr = self
        for ch in word:
            curr = curr.next[ch]
        curr.word = word
        curr.count = time

    def __lt__(self, other):
        if self.count < other.count:
            return True
        elif self.count > other.count:
            return False
        return self.word > other.word

    def get_words(self):
        """搜索当前节点一下的所有单词"""
        ans, queue = list(), collections.deque([self, ])
        while queue:
            curr = queue.popleft()
            if curr.count:
                heapq.heappush(ans, curr)
                if len(ans) > 3:
                    heapq.heappop(ans)
            for node in curr.next.values():
                queue.append(node)
        ans.sort(reverse=True)
        return [node.word for node in ans]


class AutocompleteSystem:
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = TrieNode()
        self.curr = self.root
        self.word = ""

        # 初始化字典树
        for word, time in zip(sentences, times):
            self.root.insert(word, time)

    def input(self, c: str) -> List[str]:
        if c == '#':
            self.curr.word = self.word
            self.curr.count += 1
            self.curr = self.root
            self.word = ""
            return []
        if c not in self.curr.next:
            self.curr = self.curr.next[c]
            self.word += c
            return []
        else:
            self.curr = self.curr.next[c]
            self.word += c
            return self.curr.get_words()
```