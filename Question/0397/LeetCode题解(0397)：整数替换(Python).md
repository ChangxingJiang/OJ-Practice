# LeetCode题解(0397)：整数替换(Python)

题目：[原题链接](https://leetcode-cn.com/problems/integer-replacement/)（中等）

标签：数学、位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(1)$     | 44ms (51.55%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def integerReplacement(self, n: int) -> int:
        ans = 0
        while n > 1:
            # 处理n为偶数的情况
            if n % 2 == 0:
                n //= 2
            else:
                # 处理特殊的奇数3
                if n == 3:
                    n -= 1
                else:
                    if n % 4 == 1:
                        n -= 1
                    else:
                        n += 1
            ans += 1

        return ans
```

