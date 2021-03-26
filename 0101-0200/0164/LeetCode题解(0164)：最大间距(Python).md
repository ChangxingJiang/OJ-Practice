# LeetCode题解(0164)：最大间距(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-gap/)（困难）

标签：排序、基数排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(KN)$    | $O(N)$     | 52ms (58.01%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        max_val = max(nums)  # O(N)
        now = 1

        while (10 ** (now - 1)) <= max_val:
            v1, v2 = 10 ** now, 10 ** (now - 1)

            # 生成桶：O(N)
            buckets = [[] for _ in range(10)]
            for n in nums:
                buckets[n % v1 // v2].append(n)

            # 合并桶：O(N)
            nums = []
            for bucket in buckets:
                nums.extend(bucket)

            now += 1

        # 计算结果：O(N)
        ans = 0
        for i in range(len(nums) - 1):
            ans = max(ans, nums[i + 1] - nums[i])
        return ans
```