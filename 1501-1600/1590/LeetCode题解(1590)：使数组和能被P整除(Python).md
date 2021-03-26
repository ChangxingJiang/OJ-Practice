# LeetCode题解(1590)：使数组和能被P整除(Python)

题目：[原题链接](https://leetcode-cn.com/problems/make-sum-divisible-by-p/)（中等）

标签：数组、哈希表、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时    |
| -------------- | ---------- | ---------- | ----------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 312ms (38%) |
| Ans 2 (Python) |            |            |             |
| Ans 3 (Python) |            |            |             |

解法一：

```python
class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # 计算余数
        # O(N)
        total = sum(nums)
        surplus = total % p
        # print("目标余数:", surplus)

        # 处理余数为0的情况
        if surplus == 0:
            return 0

        # 前缀余哈希表
        hashmap = {}

        ans = -1

        # 计算前缀余
        # O(N)
        last = 0
        hashmap[0] = -1
        for i, num in enumerate(nums):
            last += num
            last %= p
            hashmap[last] = i

            # 检查是否构成目标余数
            aim_val = (p + last - surplus) % p
            if aim_val in hashmap:
                now = i - hashmap[aim_val]
                if ans == -1 or ans > now:
                    ans = now

        return ans if ans < len(nums) else -1
```