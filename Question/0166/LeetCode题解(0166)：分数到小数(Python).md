# LeetCode题解(0166)：分数到小数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/fraction-to-recurring-decimal/)（中等）

标签：数学、哈希表

| 解法           | 时间复杂度                         | 空间复杂度 | 执行用时      |
| -------------- | ---------------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$ : 其中N为出现重复小数的位数 | $O(N)$     | 40ms (71.16%) |
| Ans 2 (Python) |                                    |            |               |
| Ans 3 (Python) |                                    |            |               |

解法一：

```python
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # 处理负数
        if numerator * denominator < 0:
            numerator *= -1
            sign = "-"
        else:
            sign = ""

        ans = []
        i2 = 0
        count = {}
        while True:
            if numerator not in count:
                count[numerator] = i2
                now, numerator = divmod(numerator, denominator)  # a=numerator//denominator; b=numerator%denominator
                ans.append(now)
                if numerator == 0:
                    if len(ans) == 1:
                        return sign + str(ans[0])
                    else:
                        return sign + "".join(str(ch) for ch in ([ans[0]] + ["."] + ans[1:]))
                else:
                    numerator *= 10
            else:
                i1 = count[numerator]
                return sign + "".join(str(ch) for ch in ([ans[0]] + ["."] + ans[1:i1] + ["("] + ans[i1:] + [")"]))
            i2 += 1
```