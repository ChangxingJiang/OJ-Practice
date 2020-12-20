# LeetCode题解(0360)：有序转化数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sort-transformed-array/)（中等）

标签：数学、双指针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 44ms (92.65%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:

        size = len(nums)

        # 处理开口向上的情况
        if a > 0:
            # 计算对称轴的x坐标
            mid = -(b / (2 * a))

            ans = []
            l, r = 0, size - 1
            while l <= r:
                if abs(mid - nums[l]) >= abs(nums[r] - mid):
                    v = nums[l]
                    l += 1
                else:
                    v = nums[r]
                    r -= 1
                ans.append(a * v * v + b * v + c)
            ans.reverse()
            return ans

        # 处理开口向下的情况
        elif a < 0:
            # 计算对称轴的x坐标
            mid = -(b / (2 * a))

            ans = []
            l, r = 0, size - 1
            while l <= r:
                if abs(mid - nums[l]) >= abs(nums[r] - mid):
                    v = nums[l]
                    l += 1
                else:
                    v = nums[r]
                    r -= 1
                ans.append(a * v * v + b * v + c)
            return ans

        # 处理一次函数的情况
        else:
            ans = []
            for i in range(size):
                ans.append(b * nums[i] + c)
            # 处理单调递减的情况
            if b < 0:
                ans.reverse()
            return ans
```