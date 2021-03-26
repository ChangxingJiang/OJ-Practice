# LeetCode题解(1296)：划分数组为连续数字的集合(Python)

题目：[原题链接](https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers/)（中等）

标签：数组、贪心算法、有序映射

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时        |
| -------------- | ---------- | ---------- | --------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 124ms (100.00%) |
| Ans 2 (Python) |            |            |                 |
| Ans 3 (Python) |            |            |                 |

解法一：

```python
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        size = len(nums)

        if size % k != 0:
            return False

        def get_num(nums):
            lst = [0] * (len(nums) + 1)
            now = 0
            for i in range(len(nums)):
                if nums[i] > now:
                    lst[i] += (nums[i] - now)
                    if i + k > len(nums):
                        return False
                    lst[i + k - 1] -= (nums[i] - now)
                now += lst[i]
            return now == 0

        count = collections.Counter(nums)

        now_val = []
        now_num = []
        for v in sorted(count):
            if not now_val or now_val[-1] == v - 1:
                now_val.append(v)
                now_num.append(count[v])
            else:
                if not get_num(now_num):
                    return False
                now_val, now_num = [v], [count[v]]

        if not get_num(now_num):
            return False

        return True
```

