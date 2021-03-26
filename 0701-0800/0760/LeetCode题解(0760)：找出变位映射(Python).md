# LeetCode题解(0760)：找出变位映射(Python)

题目：[原题链接](https://leetcode-cn.com/problems/find-anagram-mappings/)（简单）

标签：哈希表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(A+B)$   | $O(B)$     | 36ms (99.17%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        count = {}
        for i, n in enumerate(B):
            count[n] = i

        return [count[n] for n in A]
```