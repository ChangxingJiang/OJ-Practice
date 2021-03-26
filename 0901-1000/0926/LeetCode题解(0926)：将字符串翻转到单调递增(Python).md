# LeetCode题解(0926)：将字符串翻转到单调递增(Python)

题目：[原题链接](https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 92ms (41.28%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        lst1 = [0]
        for ch in S:
            if ch == "1":
                lst1.append(lst1[-1] + 1)
            else:
                lst1.append(lst1[-1])

        lst2 = [0]
        for ch in S[::-1]:
            if ch == "0":
                lst2.append(lst2[-1] + 1)
            else:
                lst2.append(lst2[-1])
        lst2.reverse()

        ans = len(S)
        for i in range(len(lst1)):
            ans = min(ans, lst1[i] + lst2[i])
        return ans
```

