# LeetCode题解(0870)：优势洗牌(Python)

题目：[原题链接](https://leetcode-cn.com/problems/advantage-shuffle/)（中等）

标签：数组、贪心算法、排序

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 384ms (84.62%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        size = len(A)
        sorted_A, sorted_B = sorted(A), sorted(B)

        mapping = collections.defaultdict(list)
        useless = set()
        i1, i2 = 0, 0
        while i1 < size:
            while i1 < size and sorted_A[i1] <= sorted_B[i2]:
                useless.add(sorted_A[i1])
                i1 += 1
            if i1 < size:
                mapping[sorted_B[i2]].append(sorted_A[i1])
            i2 += 1
            i1 += 1

        ans = []
        for b in B:
            if mapping[b]:
                ans.append(mapping[b].pop())
            else:
                ans.append(useless.pop())
        return ans
```

