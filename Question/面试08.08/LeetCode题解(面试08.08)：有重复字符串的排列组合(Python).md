# LeetCode题解(面试08.08)：有重复字符串的排列组合(Python)

题目：[原题链接](https://leetcode-cn.com/problems/permutation-ii-lcci/)（中等）

标签：回溯算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^N)$   | $O(N^N)$   | 240ms (33.07%) |
| Ans 2 (Python) | $O(N^N)$   | $O(N^N)$   | 44ms (87.12%)  |
| Ans 3 (Python) |            |            |                |

解法一（暴力算法）：

```python
class Solution:
    def permutation(self, S: str) -> List[str]:
        if len(S) == 1:
            return [S]
        elif len(S) == 2:
            if S[0] == S[1]:
                return [S]
            else:
                return [S, S[::-1]]
        else:
            ans = set()
            for i in range(len(S)):
                ch = S[i]
                for other in self.permutation(S[:i] + S[i + 1:]):
                    ans.add(ch + other)
            return list(ans)
```

解法二（更好的暴力）：

```python
class Solution:
    def permutation(self, S: str) -> List[str]:
        if len(S) == 1:
            return [S]
        elif len(S) == 2:
            if S[0] == S[1]:
                return [S]
            else:
                return [S, S[::-1]]
        else:
            ans = set()
            visited = set()
            for i in range(len(S)):
                ch = S[i]
                if ch not in visited:
                    visited.add(ch)
                    for other in self.permutation(S[:i] + S[i + 1:]):
                        ans.add(ch + other)
            return list(ans)
```