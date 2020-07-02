# LeetCode题解(0888)：公平的糖果交换(Python)

题目：[原题链接](https://leetcode-cn.com/problems/fair-candy-swap/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(A+B)$   | $O(1)$     | 3784ms (33.83%) |
| Ans 2 (Python) | $O(A+B)$   | $O(B)$     | 448ms (88.16%)  |
| Ans 3 (Python) |            |            |                 |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（暴力解法）：

```python
def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
    differ = sum(A) - sum(B)
    for a in A:
        b = a - differ // 2
        if b in B:
            return [a, b]
```

解法二（将B转换为集合）：

```python
def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
    differ = sum(A) - sum(B)
    B = set(B)
    for a in A:
        b = a - differ // 2
        if b in B:
            return [a, b]
```