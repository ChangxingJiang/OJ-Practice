# LeetCode题解(Offer39)：数组中出现次数超过一半的数字(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)（简单）

标签：数组、

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 52ms (70.50%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        last = None
        num = 0
        for n in nums:
            if n == last:
                num += 1
            elif num > 0:
                num -= 1
            else:
                last = n
                num = 0
        return last
```