# LeetCode题解(0781)：森林中的兔子(Python)

题目：[原题链接](https://leetcode-cn.com/problems/rabbits-in-forest/)（中等）

标签：哈希表、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 48ms (90.91%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = collections.Counter(answers)
        ans = 0
        for k, v in count.items():
            ans += math.ceil(v / (k + 1)) * (k + 1)
        return ans
```

