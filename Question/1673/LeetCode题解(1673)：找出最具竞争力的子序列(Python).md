# LeetCode题解(1673)：找出最具竞争力的子序列(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-the-most-competitive-subsequence/)（中等）

标签：栈、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N×K)$   | $O(N+K)$   | 352ms (32.99%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)

        ans = []

        right = 0

        queue = collections.deque()
        while k > 0:
            for _ in range(right, size - k + 1):
                while queue and queue[-1] > nums[right]:
                    queue.pop()
                queue.append(nums[right])
                right += 1

            ans.append(queue.popleft())
            k -= 1

        return ans
```

