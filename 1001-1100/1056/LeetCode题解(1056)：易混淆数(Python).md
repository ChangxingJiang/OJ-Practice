# LeetCode题解(1056)：易混淆数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/confusing-number/)（简单）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(logN)$  | $O(logN)$  | 44ms (20.27%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def confusingNumber(self, N: int) -> bool:
        s = str(N)

        lst = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6",
        }

        new = []
        for i in range(len(s)):
            if s[i] in ("2", "3", "4", "5", "7"):
                return False
            else:
                new.append(lst[s[i]])

        return s != "".join(new[::-1])
```