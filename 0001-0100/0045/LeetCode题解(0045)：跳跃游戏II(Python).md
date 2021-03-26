# LeetCode题解(0045)：跳跃游戏II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/jump-game-ii/)（困难）

标签：数组、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (99.70%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        size = len(nums)

        end = 0  # 上一步可达位置
        far = 0  # 当前步的下一步的最远距离
        ans = 0  # 当前步数

        for i in range(size - 1):
            # 计算当前步可达到的最远位置
            if i + nums[i] > far:
                far = i + nums[i]

            # print(i, end, far, "->", ans)
            # 上一步已经迈完了
            if i == end:
                ans += 1
                end = far

        return ans
```

