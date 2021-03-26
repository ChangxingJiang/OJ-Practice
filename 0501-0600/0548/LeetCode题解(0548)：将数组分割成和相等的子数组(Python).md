# LeetCode题解(0548)：将数组分割成和相等的子数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/split-array-with-equal-sum/)（中等）

标签：数组、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N)$     | 2068ms (38.98%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def splitArray(self, nums: List[int]) -> bool:
        # 计算前缀和
        prefix = []
        now = 0
        for n in nums:
            now += n
            prefix.append(now)

        size = len(nums)

        if size < 7:
            return False

        for i1 in range(3, size - 3):
            choices = set()
            for i2 in range(1, i1 - 1):
                if prefix[i2 - 1] == prefix[i1 - 1] - prefix[i2]:
                    choices.add(prefix[i2 - 1])
            for i2 in range(i1 + 2, size - 1):
                if prefix[i2 - 1] - prefix[i1] == prefix[-1] - prefix[i2] and (prefix[i2 - 1] - prefix[i1]) in choices:
                    return True

        return False
```