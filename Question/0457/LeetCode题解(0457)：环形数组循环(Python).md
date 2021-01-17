# LeetCode题解(0457)：环形数组循环(Python)

题目：[原题链接](https://leetcode-cn.com/problems/circular-array-loop/)（中等）

标签：数组、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 460ms (33.64%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()
        for i1, num in enumerate(nums):
            if i1 in visited:
                continue
            flag1 = 1 if nums[i1] > 0 else -1
            circle = set()
            i2 = i1
            while i2 not in circle:
                flag2 = 1 if nums[i2] > 0 else -1
                if flag1 != flag2:
                    break
                circle.add(i2)
                i2 = (i2 + nums[i2]) % len(nums)
            else:
                if len(circle) != 1 and i2 != (i2 + nums[i2]) % len(nums):  # 进入单个数字的循环
                    return True
            visited &= circle
        return False
```

