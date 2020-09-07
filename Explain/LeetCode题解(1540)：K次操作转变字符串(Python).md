# LeetCode题解(1540)：通过K次指定操作能否将字符串转换为指定字符串(Python)

题目：[原题链接](https://leetcode-cn.com/problems/can-convert-string-in-k-moves/)（中等）

标签：字符串、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(S+T)$   | $O(1)$     | 468ms (58.16%) |
| Ans 2 (Python) | $O(S+T)$   | $O(1)$     | 364ms (84.43%) |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        N1, N2 = len(s), len(t)

        # 处理特殊情况
        if N1 != N2:
            return False

        # 统计k中可以处理各种切换数量的次数
        a, b = divmod(k, 26)
        count = [a + 1] * b + [a] * (26 - b)

        # 统计将s变为t所需要的切换次数
        for i in range(N1):
            if s[i] != t[i]:
                c1, c2 = ord(s[i]), ord(t[i])
                diff = (c2 + 26 - c1) % 26
                if count[diff - 1] > 0:
                    count[diff - 1] -= 1
                else:
                    return False

        return True
```

解法二（优化解法一）：

```python
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        N1, N2 = len(s), len(t)

        # 处理特殊情况
        if N1 != N2:
            return False

        # 统计k中可以处理各种切换数量的次数
        a, b = divmod(k, 26)
        count = [a + 1] * b + [a] * (26 - b)

        # 统计将s变为t所需要的切换次数
        for s_ch, t_ch in zip(s, t):
            diff = (ord(t_ch) - ord(s_ch)) % 26 - 1
            if diff >= 0:
                if count[diff] > 0:
                    count[diff] -= 1
                else:
                    return False

        return True
```