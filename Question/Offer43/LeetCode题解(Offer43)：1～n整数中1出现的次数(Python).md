# LeetCode题解(Offer43)：计算n个整数中数字1出现的次数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(logN)$  | 32ms (96.57%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        ans = 0

        s = str(n)
        for i, ch in enumerate(s):
            high = int(s[:i]) if i > 0 else 0  # 当前位左侧数值
            curr = int(ch)  # 当前位数值
            low = int(s[i + 1:]) if i + 1 < len(s) else 0  # 当前位右侧数值
            digit = 10 ** (len(s) - i - 1)  # 当前位位数

            if curr == 0:
                ans += high * digit
            elif curr == 1:
                ans += high * digit + low + 1
            else:
                ans += high * digit + digit

        return ans
```