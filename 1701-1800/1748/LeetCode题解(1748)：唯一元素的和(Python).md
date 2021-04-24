# LeetCode题解(1748)：唯一元素的和(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sum-of-unique-elements/)（简单）

标签：数组、哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 44ms (35.31%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        s1 = set()
        s2 = set()
        for num in nums:
            if num not in s2:
                if num not in s1:
                    s1.add(num)
                else:
                    s1.remove(num)
                    s2.add(num)
        return sum(s1)
```

