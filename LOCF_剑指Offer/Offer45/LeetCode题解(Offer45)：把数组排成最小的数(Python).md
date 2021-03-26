# LeetCode题解(Offer45)：把非负整数数组排成一个最小的数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/)（中等）

标签：数学、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 40ms (95.95%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（自定义排序）：

```python
class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = [str(n) for n in nums]

        def sort_key(x, y):
            a, b = x + y, y + x
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0

        nums.sort(key=functools.cmp_to_key(sort_key))

        return "".join(nums)
```