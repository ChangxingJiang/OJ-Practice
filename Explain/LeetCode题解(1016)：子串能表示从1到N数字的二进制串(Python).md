# LeetCode题解(1016)：判断大量整数的二进制表示是否为字符串的子串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/binary-string-with-substrings-representing-1-to-n/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (83.94%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（暴力解法）：

```python
class Solution:
    def queryString(self, S: str, N: int) -> bool:
        # 先将二进制转换为数字，去除不可能的N
        if int(S, base=2) < N:
            return False

        for i in range(N, 0, -1):
            if str(bin(i))[2:] not in S:
                return False

        return True
```