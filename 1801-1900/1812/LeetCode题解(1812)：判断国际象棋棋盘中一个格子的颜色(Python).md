# LeetCode题解(1812)：判断国际象棋棋盘中一个格子的颜色(Python)

题目：[原题链接](https://leetcode-cn.com/problems/determine-color-of-a-chessboard-square/)（简单）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 40ms (50.67%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        lst1 = ["a", "c", "e", "g"]
        lst2 = ["1", "3", "5", "7"]
        ch1, ch2 = coordinates
        if not (ch1 in lst1 and ch2 in lst2) and (ch1 in lst1 or ch2 in lst2):
            return True
        else:
            return False
```

