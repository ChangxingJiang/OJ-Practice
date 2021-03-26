# LeetCode题解(1247)：交换字符串使得两个字符串相同(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-swaps-to-make-strings-equal/)（中等）

标签：字符串、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (92.37%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        N = len(s1)

        # 统计两字符串中不同的情况
        count1 = 0
        count2 = 0
        for i in range(N):
            ch1 = s1[i]
            ch2 = s2[i]
            if ch1 == "x" and ch2 == "y":
                count1 += 1
            elif ch1 == "y" and ch2 == "x":
                count2 += 1

        a1, b1 = divmod(count1, 2)
        a2, b2 = divmod(count2, 2)

        # 判断两字符串是否可交换生成
        if b1 + b2 != 1:
            return a1 + a2 + b1 + b2
        else:
            return -1
```