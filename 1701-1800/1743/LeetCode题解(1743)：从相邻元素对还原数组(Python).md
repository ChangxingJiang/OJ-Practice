# LeetCode题解(1743)：从相邻元素对还原数组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs/)（中等）

标签：哈希表、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 520ms (20.76%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        near = defaultdict(set)
        count = Counter()

        for n1, n2 in adjacentPairs:
            near[n1].add(n2)
            near[n2].add(n1)
            count[n1] += 1
            count[n2] += 1

        start = 0
        for num in count:
            if count[num] == 1:
                start = num
                break

        ans = [start]
        while near[ans[-1]]:
            now = ans[-1]
            nxt = near[now].pop()
            near[nxt]._remove(now)
            ans.append(nxt)

        return ans
```

