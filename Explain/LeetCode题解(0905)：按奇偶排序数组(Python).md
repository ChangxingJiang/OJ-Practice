# LeetCode题解(0905)：按奇偶排序数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sort-array-by-parity/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 96ms (79.94%)  |
| Ans 2 (Python) | $O(N)$     | $O(N)$     | 100ms (63.23%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（Pythonic）：

```python
def sortArrayByParity(self, A: List[int]) -> List[int]:
    return [a for a in A if a % 2 == 0] + [a for a in A if a % 2 == 1]
```

解法二：

```python
def sortArrayByParity(self, A: List[int]) -> List[int]:
    odd = []
    even = []
    for a in A:
        if a % 2 == 0:
            even.append(a)
        else:
            odd.append(a)
    return even+odd
```