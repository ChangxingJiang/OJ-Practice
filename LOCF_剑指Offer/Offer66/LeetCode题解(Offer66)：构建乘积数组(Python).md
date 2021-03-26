# LeetCode题解(Offer66)：不使用除法的情况下构建乘积数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/)（中等）

标签：数组、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 72ms (90.62%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（前后缀数组）：

```python
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        prefix = [1]
        now = 1
        for n in a:
            now *= n
            prefix.append(now)

        suffix = [1]
        now = 1
        for n in a[::-1]:
            now *= n
            suffix.append(now)
        suffix.reverse()

        ans = []
        for i in range(len(a)):
            ans.append(prefix[i] * suffix[i + 1])

        return ans
```