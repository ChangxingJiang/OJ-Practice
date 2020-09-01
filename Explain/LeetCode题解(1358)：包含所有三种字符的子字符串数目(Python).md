# LeetCode题解(1358)：包含所有三种字符的子字符串数目(Python)

题目：[原题链接](https://leetcode-cn.com/problems/number-of-substrings-containing-all-three-characters/)（中等）

标签：字符串、双指针、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 168ms (100.00%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

![LeetCode题解(1358)：截图1](LeetCode题解(1358)：截图1.png)

```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        N = len(s)
        left = -1  # 窗口左侧坐标
        a, b, c = -1, -1, -1  # 当前最近的a,b,c坐标
        ans = 0
        for right, ch in enumerate(s):
            # 更新最近的a,b,c坐标
            if ch == "a":
                a = right
            elif ch == "b":
                b = right
            else:
                c = right

            # 判断窗口内是否包含三个字母
            if a > left and b > left and c > left:
                new_left = min(a, b, c)
                ans += (new_left - left) * (N - right)
                left = new_left

        return ans
```