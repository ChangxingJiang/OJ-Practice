# LeetCode题解(1432)：改变一个整数能得到的最大差值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-difference-you-can-get-from-changing-an-integer/)（中等）

标签：字符串、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (51.98%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxDiff(self, num: int) -> int:
        num_max = num_min = str(num)

        # 计算替换后的最大值
        for ch in num_max:
            if ch != "9":
                num_max = num_max.replace(ch, "9")
                break

        # 计算替换后的最小值
        first_num = num_min[0]
        for i, ch in enumerate(num_min):
            if i == 0:
                if ch != "1":
                    num_min = num_min.replace(ch, "1")
                    break
            elif ch != "0" and ch != first_num:
                num_min = num_min.replace(ch, "0")
                break

        return int(num_max) - int(num_min)
```