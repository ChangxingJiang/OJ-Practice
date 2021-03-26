# LeetCode题解(0769)：最多能完成排序的块(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-chunks-to-make-sorted/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 36ms (80.58%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maxChunksToSorted(self, arr1: List[int]) -> int:
        ans = 0
        find = set()
        need = set()
        for i in range(len(arr1)):
            find.add(arr1[i])
            need.add(i)
            if find == need:
                ans += 1
        return ans
```

