# LeetCode题解(0398)：随机数索引(Python)

题目：[原题链接](https://leetcode-cn.com/problems/random-pick-index/)（中等）

标签：随机、蓄水池抽样

| 解法           | 时间复杂度                    | 空间复杂度 | 执行用时       |
| -------------- | ----------------------------- | ---------- | -------------- |
| Ans 1 (Python) | 构造 = $O(1)$ ; 随机 = $O(N)$ | $O(1)$     | 320ms (96.61%) |
| Ans 2 (Python) |                               |            |                |
| Ans 3 (Python) |                               |            |                |

解法一：

```python
class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        idx = 0
        ans = 0
        for i, n in enumerate(self.nums):
            if n == target:
                idx += 1
                rand = random.randint(1, idx)
                if rand == idx:
                    ans = i
        return ans
```