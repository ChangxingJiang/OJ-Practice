# LeetCode题解(0922)：调整数组中奇偶数的位置(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sort-array-by-parity-ii/)（简单）

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 244ms (85.83%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 232ms (98.83%) |
| Ans 3 (Python) |            |            |                |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```python
def sortArrayByParityII(self, A: List[int]) -> List[int]:
    type1 = []
    type2 = []
    for i in range(len(A)):
        i2 = i % 2
        A2 = A[i] % 2
        if i2 != A2:
            if i2 == 0:
                if len(type1) > 0:
                    n = type1.pop()
                    A[n], A[i] = A[i], A[n]
                else:
                    type2.append(i)
            else:
                if len(type2) > 0:
                    n = type2.pop()
                    A[n], A[i] = A[i], A[n]
                else:
                    type1.append(i)

    return A
```

解法二（双指针）：

```python
def sortArrayByParityII(self, A: List[int]) -> List[int]:
    idx = 1
    for i in range(0, len(A), 2):
        if A[i] % 2 != 0:
            while A[idx] % 2 != 0:
                idx += 2
            A[idx], A[i] = A[i], A[idx]
    return A
```