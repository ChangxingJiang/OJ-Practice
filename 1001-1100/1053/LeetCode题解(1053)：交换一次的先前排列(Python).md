# LeetCode题解(1053)：交换一次的先前排列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/previous-permutation-with-one-swap/)（中等）

标签：贪心算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 64ms (8.11%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        idx1 = -1
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                idx1 = i

        if idx1 == -1:
            return arr

        idx2 = idx1 + 1
        for i in range(idx1 + 1, len(arr)):
            if arr[idx2] < arr[i] < arr[idx1]:
                idx2 = i

        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
        return arr
```

