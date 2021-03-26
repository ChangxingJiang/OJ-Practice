# LeetCode题解(1726)：同积元组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/tuple-with-same-product/)（中等）

标签：数组、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 2432ms (6.75%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = collections.defaultdict(list)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                count[nums[i] * nums[j]].append((i, j))

        ans = 0
        for lst in count.values():
            for i in range(len(lst)):
                for j in range(i + 1, len(lst)):
                    if lst[i][0] != lst[i][1] != lst[j][0] != lst[j][1]:
                        ans += 8

        return ans
```

