# LeetCode题解(1217)：筹码游戏(Python)

题目：[原题链接](https://leetcode-cn.com/problems/play-with-chips/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 48ms (37.23%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 32ms (98.85%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（情景模拟）：

```python
def minCostToMoveChips(self, chips: List[int]) -> int:
    a = 0
    b = 0
    for chip in chips:
        if chip % 2 == 0:
            a += 1
        else:
            b += 1
    return min(a, b)
```

解法二（优化解法一）：

```python
def minCostToMoveChips(self, chips: List[int]) -> int:
    a = 0
    for chip in chips:
        a += (chip % 2 == 0)
    return min(a, len(chips) - a)
```