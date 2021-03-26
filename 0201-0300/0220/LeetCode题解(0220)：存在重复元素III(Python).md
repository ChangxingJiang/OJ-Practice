# LeetCode题解(0220)：存在重复元素III(Python)

题目：[原题链接](https://leetcode-cn.com/problems/contains-duplicate-iii/)（中等）

标签：排序、有序映射

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N×K)$   | $O(1)$     | 超出时间限制  |
| Ans 2 (Python) | $O(N)$     | $O(K)$     | 52ms (85.77%) |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        for i1 in range(len(nums)):
            n1 = nums[i1]
            for i2 in range(i1 + 1, min(i1 + k + 1, len(nums))):
                n2 = nums[i2]
                if abs(n2 - n1) <= t:
                    return True
        return False
```

解法二：

```python
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        buckets = {}  # 定义桶
        bucket_size = t + 1  # 定义桶的大小

        for i in range(len(nums)):
            # 计算需要放入的桶编号
            bucket_idx = nums[i] // bucket_size

            # 如果桶已经存在，则返回True
            if bucket_idx in buckets:
                return True

            # 将数据放入到桶中
            buckets[bucket_idx] = nums[i]

            # 如果前一个桶已经存在符合要求的值，则返回True
            if (bucket_idx - 1) in buckets and abs(buckets[bucket_idx - 1] - nums[i]) <= t:
                return True

            # 如果后一个桶已经存在符合要求的值，则返回True
            if (bucket_idx + 1) in buckets and abs(buckets[bucket_idx + 1] - nums[i]) <= t:
                return True

            # 如果没有符合要求的值，且桶的数量已经满了，则移除最老的桶
            if i >= k:
                buckets.pop(nums[i - k] // bucket_size)

        return False
```

