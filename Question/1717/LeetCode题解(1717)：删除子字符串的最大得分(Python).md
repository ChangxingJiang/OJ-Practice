# LeetCode题解(1717)：删除子字符串的最大得分(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-score-from-removing-substrings/)（中等）

标签：字符串、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 1056ms (25.82%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        lst = [""]
        for ch in s:
            if ch == "a" or ch == "b":
                lst[-1] += ch
            else:
                if lst[-1] != "":
                    lst.append("")

        ans = 0

        for ss in lst:
            # 计算总数的最大值
            max_num = min(ss.count("a"), ss.count("b"))

            if x >= y:
                # 计算ab数量的最大值
                max_n1 = 0
                count = 0
                for ch in ss:
                    if ch == "a":
                        count += 1
                    else:
                        if count > 0:
                            count -= 1
                            max_n1 += 1

                # 计算最终结果
                ans += max_n1 * x + (max_num - max_n1) * y

            else:
                # 计算ba数量的最大值
                max_n2 = 0
                count = 0
                for ch in ss:
                    if ch == "b":
                        count += 1
                    else:
                        if count > 0:
                            count -= 1
                            max_n2 += 1

                # 计算最终结果
                ans += max_n2 * y + (max_num - max_n2) * x

        return ans
```

