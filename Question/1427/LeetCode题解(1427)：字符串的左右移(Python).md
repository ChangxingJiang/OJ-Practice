# LeetCode题解(1427)：字符串的左右移(Python)

题目：[原题链接](https://leetcode-cn.com/problems/perform-string-shifts/)（简单）

标签：数组、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (74.55%) |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 48ms (21.82%) |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for direction, amount in shift:
            if direction == 1:
                s = s[len(s) - amount:] + s[:len(s) - amount]
            else:
                s = s[amount:] + s[:amount]
        return s
```

解法二：

```python
class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        num = 0
        for direction, amount in shift:
            if direction == 1:
                num += amount
            else:
                num -= amount

        num %= len(shift)

        if num > 0:
            s = s[len(s) - num:] + s[:len(s) - num]
        else:
            s = s[num:] + s[:num]

        return s
```