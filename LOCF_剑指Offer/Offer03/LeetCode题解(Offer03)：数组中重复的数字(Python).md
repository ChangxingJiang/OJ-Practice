# LeetCode题解(Offer03)：寻找数组中重复的数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)（简单）

标签：数组、集合

| 解法           | 时间复杂度                           | 空间复杂度 | 执行用时      |
| -------------- | ------------------------------------ | ---------- | ------------- |
| Ans 1 (Python) | $O(K)$ : 其中K为第一个重复元素的坐标 | $O(K)$     | 52ms (81.12%) |
| Ans 2 (Python) |                                      |            |               |
| Ans 3 (Python) |                                      |            |               |

解法一（）：

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashmap = set()
        for n in nums:
            if n in hashmap:
                return n
            hashmap.add(n)
```