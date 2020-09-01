# LeetCode题解(1419)：依据多个蛙叫混合的列表计算最少的青蛙数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/minimum-number-of-frogs-croaking/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 120ms (100.00%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

![LeetCode题解(1419)：截图](LeetCode题解(1419)：截图.png)

```python
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        ans = 0
        a, b, c, d = 0, 0, 0, 0  # 四个叫声状态的数量
        for ch in croakOfFrogs:
            # 计算当前叫声状态
            if ch == "c":
                a += 1
                total = a + b + c + d
                if total > ans:
                    ans = total
            elif ch == "r":
                a -= 1
                b += 1
                if a < 0:
                    return -1
            elif ch == "o":
                b -= 1
                c += 1
                if b < 0:
                    return -1
            elif ch == "a":
                c -= 1
                d += 1
                if c < 0:
                    return -1
            else:
                d -= 1
                if d < 0:
                    return -1

        # 判断所有叫声是否结束
        if a != 0 or b != 0 or c != 0 or d != 0:
            return -1
        else:
            return ans
```