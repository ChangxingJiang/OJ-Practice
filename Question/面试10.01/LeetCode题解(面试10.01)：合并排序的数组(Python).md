# LeetCode题解(面试10.01)：合并排序的数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sorted-merge-lcci/)（简单）

标签：排序、数组、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 48ms (20.19%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        i, i1, i2 = m + n - 1, m - 1, n - 1
        while True:
            if i1 >= 0 and i2 >= 0:
                if A[i1] >= B[i2]:
                    A[i] = A[i1]
                    i -= 1
                    i1 -= 1
                else:
                    A[i] = B[i2]
                    i -= 1
                    i2 -= 1
            elif i1 >= 0:
                A[i] = A[i1]
                i -= 1
                i1 -= 1
            elif i2 >= 0:
                A[i] = B[i2]
                i -= 1
                i2 -= 1
            else:
                break
```