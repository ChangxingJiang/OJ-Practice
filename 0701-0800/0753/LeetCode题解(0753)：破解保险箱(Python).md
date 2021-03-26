# LeetCode题解(0753)：破解保险箱(Python)

题目：[原题链接](https://leetcode-cn.com/problems/cracking-the-safe/)（困难）

标签：深度优先搜索、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(N×K^N)$ | $O(N×K^N)$ | 84ms (9.38%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        visited = set()

        def dfs(s1):
            visited.add(s1)
            for v in range(k):
                s2 = s1[1:] + str(v)
                if s2 not in visited:
                    dfs(s2)
            stack.append(s1[0])

        # 处理其他进制的情况
        stack = ["0" * (n - 1)]
        dfs("0" * n)
        return "".join(stack[::-1])
```

