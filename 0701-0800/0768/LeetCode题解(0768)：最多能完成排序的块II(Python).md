# LeetCode题解(0768)：最多能完成排序的块II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/max-chunks-to-make-sorted-ii/)（困难）

标签：数组、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 100ms (37.20%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxChunksToSorted(self, arr1: List[int]) -> int:
        arr2 = list(arr1)
        arr2.sort()
        ans = 0
        count = collections.Counter()
        for i in range(len(arr1)):
            if arr1[i] != arr2[i]:
                count[arr1[i]] += 1
                count[arr2[i]] -= 1
                if count[arr1[i]] == 0:
                    count.pop(arr1[i])
                if count[arr2[i]] == 0:
                    count.pop(arr2[i])
            if len(count) == 0:
                ans += 1
        return ans
```

