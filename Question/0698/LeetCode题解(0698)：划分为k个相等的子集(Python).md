# LeetCode题解(0698)：划分为k个相等的子集(Python)

题目：[原题链接](https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/)（中等）

标签：递归、数学、集合、动态规划

| 解法           | 时间复杂度     | 空间复杂度 | 执行用时       |
| -------------- | -------------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN+N^3)$ | $O(N^2)$   | 152ms (33.24%) |
| Ans 2 (Python) |                |            |                |
| Ans 3 (Python) |                |            |                |

解法一（递归）：

```python
class Solution:
    def __init__(self):
        self.chooses_set = set()
        self.chooses = list()
        self.nums = []

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()

        total = sum(nums)

        # 处理数组的和不能被整除的情况
        if total % k != 0:
            return False

        # 处理数组中最大值过大的情况
        avg = total / k
        if nums[-1] > avg:
            return False

        # print(nums, "目标值:", avg)

        # 寻找所有可能的子集
        self.nums = nums
        self.count_choose([], 0, avg)

        # 依据子集中的最大值排序所有可能的子集
        surplus = set([i for i in range(len(nums))])
        self.chooses = list(set(choose) for choose in sorted(self.chooses_set, key=lambda x: max(x)))

        # print(self.chooses)

        # 处理子集计算存在结果
        return self.count_ans(frozenset(surplus), len(self.chooses) - 1)

    def count_choose(self, now, i, aim):
        if i < len(self.nums):
            num = self.nums[i]
            if num < aim:
                now.append(i)
                self.count_choose(now, i + 1, aim - num)
                now.remove(i)
                self.count_choose(now, i + 1, aim)
            elif num == aim:
                now.append(i)
                self.chooses_set.add(tuple(now))
                now.remove(i)
                self.count_choose(now, i + 1, aim)

    def count_ans(self, surplus, i):
        if not surplus:
            return True
        elif i >= 0:
            idx = set(self.chooses[i])
            if idx <= surplus:
                return self.count_ans(surplus - idx, i - 1) or self.count_ans(surplus, i - 1)
            else:
                return self.count_ans(surplus, i - 1)
        else:
            return False
```