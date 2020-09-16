# LeetCode题解(Offer38)：生成字符串中字母的全排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/)（中等）

标签：字符串、回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N!)$    | $O(N!)$    | 464ms (9.31%)  |
| Ans 2 (Python) | $O(N!)$    | $O(N!)$    | 112ms (95.61%) |
| Ans 3 (Python) | $O(N!)$    | $O(N!)$    | 84ms (98.78%)  |

解法一（递归）：

```python
class Solution:
    def __init__(self):
        self.s = []
        self.lst = []
        self.ans = set()

    def permutation(self, s: str) -> List[str]:
        self.s = list(s)

        def dfs():
            if self.s:
                for i, ch in enumerate(self.s):
                    ch = self.s.pop(i)
                    self.lst.append(ch)
                    dfs()
                    self.lst.pop()
                    self.s.insert(i, ch)
            else:
                self.ans.add("".join(self.lst))

        dfs()

        return list(self.ans)
```

解法二（迭代）：

```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        ans = collections.deque([""])
        for ch in s:
            for _ in range(len(ans)):
                now = ans.popleft()
                for i in range(len(now) + 1):
                    ans.append(now[:i] + ch + now[i:])
        ans = list(set(ans))
        return ans
```

解法三（优化解法二）：

```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        ans = collections.deque([""])
        for ch in s:
            for _ in range(len(ans)):
                now = ans.popleft()
                for i in range((now + ch).index(ch) + 1):
                    ans.append(now[:i] + ch + now[i:])
        ans = list(set(ans))
        return ans
```