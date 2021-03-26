# LeetCode题解(0775)：全局倒置与局部倒置(Python)

题目：[原题链接](https://leetcode-cn.com/problems/global-and-local-inversions/)（中等）

标签：数组、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 372ms (81.98%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        n1 = 0  # 局部倒置
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                n1 += 1
        n2 = 0  # 全局倒置
        for i in range(len(A)):
            if A[i] > i:
                n2 += (A[i] - i + 1) * (A[i] - i) // 2
        return n1 >= n2
```



