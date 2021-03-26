# LeetCode题解(1243)：数组变换(Python)

题目：[原题链接](https://leetcode-cn.com/problems/array-transformation/)（简单）

标签：数组

| 解法           | 时间复杂度                 | 空间复杂度 | 执行用时      |
| -------------- | -------------------------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×L)$ : 其中L为所需天数 | $O(N)$     | 40ms (82.69%) |
| Ans 2 (Python) |                            |            |               |
| Ans 3 (Python) |                            |            |               |

解法一：

```python
class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        if len(arr) <= 2:
            return arr

        change = True
        while change:
            change = False
            new = [arr[0]]
            for i in range(1, len(arr) - 1):
                if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                    new.append(arr[i] - 1)
                    change = True
                elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                    new.append(arr[i] + 1)
                    change = True
                else:
                    new.append(arr[i])
            new.append(arr[-1])
            arr = new

        return arr
```