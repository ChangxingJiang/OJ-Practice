# LeetCode题解(0899)：计算移动后字典序最小的序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/orderly-queue/)（困难）

标签：字符串

| 解法           | 时间复杂度   | 空间复杂度 | 执行用时      |
| -------------- | ------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2logN)$ | $O(N^2)$   | 32ms (95.77%) |
| Ans 2 (Python) | $O(N^2)$     | $O(N^2)$   | 44ms (50.70%) |
| Ans 3 (Python) |              |            |               |

解法一：

```python
class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:
            temp = set()
            for i in range(len(S)):
                temp.add(S[i:] + S[:i])
            return min(list(temp))
        else:
            return "".join(sorted(list(S)))
```

解法二：

```python
class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K == 1:
            now = S
            for i in range(len(S)):
                tmp = S[i:] + S[:i]
                if tmp < now:
                    now = tmp
            return now
        else:
            return "".join(sorted(list(S)))
```