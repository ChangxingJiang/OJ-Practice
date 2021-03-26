# LeetCode题解(1471)：数组中的k个最强值(Python)

题目：[原题链接](https://leetcode-cn.com/problems/the-k-strongest-values-in-an-array/)（中等）

标签：数组、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 460ms (27%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort()

        size = len(arr)

        mid = arr[int((size - 1) / 2)]
        # if size % 2 == 0:
        #     mid = (arr[size // 2 - 1] + arr[size // 2]) / 2
        # else:
        #     mid = arr[size // 2]

        arr.sort(key=lambda x: (abs(x - mid), x))

        # print(mid, arr)

        return arr[-k:]
```

