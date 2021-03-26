# LeetCode题解(0229)：求众数II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/majority-element-ii/)（中等）

标签：数组、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 48ms (70.08%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 摩尔投票
        n1_val, n1_num = 0, 0
        n2_val, n2_num = 0, 0
        for num in nums:
            if num == n1_val:
                n1_num += 1
            elif num == n2_val:
                n2_num += 1
            else:  # num != n1_val and num != n2_val
                if n1_num == 0:
                    n1_val, n1_num = num, 1
                    continue
                elif n2_num == 0:
                    n2_val, n2_num = num, 1
                    continue
                else:
                    n1_num -= 1
                    n2_num -= 1

        # 计票确认
        n1_num, n2_num = 0, 0
        for num in nums:
            if num == n1_val:
                n1_num += 1
            elif num == n2_val:
                n2_num += 1

        target = len(nums) / 3

        ans = []
        if n1_num > target:
            ans.append(n1_val)
        if n2_num > target:
            ans.append(n2_val)
        return ans
```

