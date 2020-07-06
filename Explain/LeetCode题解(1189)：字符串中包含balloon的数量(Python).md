# LeetCode题解(1189)：字符串中包含balloon的数量(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-number-of-balloons/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (83.40%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（哈希表）：

```python
def maxNumberOfBalloons(self, text: str) -> int:
    count = collections.Counter(text)
    if "b" not in count or "a" not in count or "l" not in count or "o" not in count or "n" not in count:
        return 0
    else:
        return min(count["b"], count["a"], count["l"] // 2, count["o"] // 2, count["n"])
```

