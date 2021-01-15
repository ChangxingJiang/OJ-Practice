# LeetCode题解(0015)：三数之和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/3sum/)（中等）

标签：数组、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N^2)$   | $O(N^2)$   | 超出时间限制   |
| Ans 2 (Python) | $O(N^2)$   | $O(logN)$  | 840ms (57.90%) |
| Ans 3 (Python) |            |            |                |

解法一（暴力解法）：

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        count = collections.defaultdict(set)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    count[nums[i] + nums[j]].add((i, j))

        ans = set()
        for k in range(len(nums)):
            if -nums[k] in count:
                for i, j in count[-nums[k]]:
                    if i != k and j != k:
                        ans.add(tuple(sorted([nums[i], nums[j], nums[k]])))

        return [list(res) for res in ans]
```

解法二：

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:  # 如果和上一个数相同则跳过
                continue
            if nums[i] > 0:  # 如果第1个数已经大于0，则跳过当前选择
                break
            k = len(nums) - 1
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:  # 如果和上一个数相同则跳过
                    continue
                if nums[i] + nums[j] > 0:  # 如果第1个数和第2个数之和已经大于0，则跳过当前选择
                    break
                while j < k and nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                if j == k:
                    break
                if nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])

        return ans
```