# LeetCode题解(1073)：负二进制数相加(Python)

题目：[原题链接](https://leetcode-cn.com/problems/adding-two-negabinary-numbers/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 28ms (100.00%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1

        arr1.reverse()
        arr2.reverse()

        for i in range(len(arr2)):
            arr1[i] += arr2[i]

        arr1.extend([0, 0, 0])
        i = 0
        while i < len(arr1):
            if arr1[i] >= 2:
                v = arr1[i] // 2
                arr1[i] %= 2
                arr1[i + 1] -= v
            elif arr1[i] <= -1:
                arr1[i] *= -1
                arr1[i + 1] += arr1[i]
            i += 1

        while arr1 and arr1[-1] == 0:
            arr1.pop()

        arr1.reverse()

        return arr1 if len(arr1) > 0 else [0]
```

