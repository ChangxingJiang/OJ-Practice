# LeetCode题解(面试08.04)：幂集(Python)

题目：[原题链接](https://leetcode-cn.com/problems/power-set-lcci/)（中等）

标签：数组、回溯算法、位运算

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(2^N)$   | $O(2^N)$   | 44ms (41.01%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.ans = set()
        self.nums = []
        self.now = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums

        self.count()

        return [list(i) for i in self.ans]

    def count(self, left=0):
        if left == len(self.nums):
            self.ans.add(tuple(self.now))
        else:
            self.now.append(self.nums[left])
            self.count(left + 1)
            self.now.pop()
            self.count(left + 1)
```