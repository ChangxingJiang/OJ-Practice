# LeetCode题解(1525)：字符串中前后不同字符数相同的分隔数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-good-ways-to-split-a-string/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 88ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一（两次遍历）：

![LeetCode题解(1525)：截图](LeetCode题解(1525)：截图.png)

```python
class Solution:
    def numSplits(self, s: str) -> int:
        # 遍历统计正向到每个坐标的不同字符的数量
        nums = [0]
        now, lst = 0, set()
        for ch in s:
            if ch not in lst:
                lst.add(ch)
                now += 1
            nums.append(now)
        nums.pop()

        # 反向遍历每个坐标的不同字符数量与正向是否相同
        ans = 0
        now, lst = 0, set()
        for ch in s[::-1]:
            if ch not in lst:
                lst.add(ch)
                now += 1
            if nums.pop() == now:
                ans += 1

        return ans
```