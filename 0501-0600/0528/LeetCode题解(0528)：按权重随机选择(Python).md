# LeetCode题解(0528)：按权重随机选择(Python)

题目：[原题链接](https://leetcode-cn.com/problems/random-pick-with-weight/)（中等）

标签：随机、二分查找

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(logW)$  | $O(W)$     | 312ms (43.72%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:

    def __init__(self, w: List[int]):
        self.nums = w

        self.prefix = []
        now = 0
        for i, num in enumerate(self.nums):
            now += num
            self.prefix.append(now)

    def pickIndex(self) -> int:
        target = random.randint(0, self.prefix[-1] - 1)
        # print("随机数:", target)

        l, r = 0, len(self.prefix) - 1
        ans = 0
        while l <= r:
            m = (l + r) // 2
            # print(l, r, "->", m, "->", self.prefix[m], target)
            if self.prefix[m] <= target:
                l = m + 1
                ans = m + 1
            else:  # self.prefix[m] > target:
                r = m - 1

        return ans
```