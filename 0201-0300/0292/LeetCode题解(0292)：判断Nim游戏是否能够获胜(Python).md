# LeetCode题解(0292)：判断Nim游戏是否能够获胜(Python)

题目：[原题链接](https://leetcode-cn.com/problems/nim-game/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(1)       | O(1)       | 32ms (94.49%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（当时4的倍数时无法获胜，其他时候均可获胜）：

```python
def canWinNim(self, n: int) -> bool:
    return not n % 4 == 0
```