# LeetCode题解(0520)：检查单词大写是否正确(Python)

题目：[原题链接](https://leetcode-cn.com/problems/detect-capital/)（简单）

题目标签：

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | O(n)       | O(1)       | 36ms (90.14%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def detectCapitalUse(self, word: str) -> bool:
    lower_num = 0
    upper_num = 0
    for c in word:
        if ord(c) >= 97:
            if upper_num >= 2:
                return False
            else:
                lower_num += 1
        else:
            if lower_num > 0:
                return False
            else:
                upper_num += 1
    else:
        return True
```