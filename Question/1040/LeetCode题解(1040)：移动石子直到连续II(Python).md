# LeetCode题解(1040)：移动石子直到连续II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/moving-stones-until-consecutive-ii/)（中等）

标签：数组、滑动窗口

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 124ms (77.55%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        size = len(stones)

        max_val = stones[-1] - stones[0] + 1 - size - min(stones[1] - stones[0] - 1, stones[-1] - stones[-2] - 1)

        min_val = max_val
        l = 0
        num = 0
        for r in range(size):
            num += 1
            while stones[r] - stones[l] + 1 > size:
                l += 1
                num -= 1

            # 处理特殊情况：3,4,5,6,10
            if size - num == 1 and stones[r] - stones[l] + 1 == size - 1:
                min_val = min(min_val, 2)
            else:
                min_val = min(min_val, size - num)

        return [min_val, max_val]
```

