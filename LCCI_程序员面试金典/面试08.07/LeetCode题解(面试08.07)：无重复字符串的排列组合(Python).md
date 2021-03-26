# LeetCode题解(面试08.07)：无重复字符串的排列组合(Python)

题目：[原题链接](https://leetcode-cn.com/problems/permutation-i-lcci/)（中等）

标签：回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^N)$   | $O(N^N)$   | 280ms (6.01%)  |
| Ans 2 (Python) | $O(N^N)$   | $O(N^N)$   | 184ms (35.93%) |
| Ans 3 (Python) | $O(N^N)$   | $O(N^N)$   | 104ms (85.68%) |

解法一（暴力解法）：

```python
class Solution:
    def __init__(self):
        self.ans = []
        self.lst = []
        self.now = []

    def permutation(self, S: str) -> List[str]:
        self.lst = list(S)
        self.count()
        return ["".join(e) for e in self.ans if e]

    def count(self):
        if len(self.now) == len(self.lst):
            self.ans.append(list(self.now))
        else:
            for ch in self.lst:
                if ch not in self.now:
                    self.now.append(ch)
                    self.count()
                    self.now.pop()
```

解法二（更好的暴力）：

```python
class Solution:
    def __init__(self):
        self.lst = set()
        self.size = 0

        self.ans = []

        self.now = []

    def permutation(self, S: str) -> List[str]:
        self.lst = set(S)
        self.size = len(self.lst)

        self.count()

        return ["".join(e) for e in self.ans if e]

    def count(self):
        if len(self.now) == self.size:
            self.ans.append(list(self.now))
        else:
            for ch in list(self.lst):
                self.lst.remove(ch)
                self.now.append(ch)
                self.count()
                self.now.pop()
                self.lst.add(ch)
```

解法三（又一种暴力）：

```python
class Solution:
    def permutation(self, S: str) -> List[str]:
        if len(S) == 2:
            return [S, S[::-1]]
        else:
            ans = []
            for i in range(len(S)):
                ch = S[i]
                for other in self.permutation(S[:i] + S[i + 1:]):
                    ans.append(ch + other)
            return ans
```



