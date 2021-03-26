# LeetCode题解(1282)：用户分组(Python)

题目：[原题链接](https://leetcode-cn.com/problems/group-the-people-given-the-group-size-they-belong-to/)（中等）

标签：贪心算法、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (91.24%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        people_list = [[] for _ in range(max(groupSizes) + 1)]

        for i, n in enumerate(groupSizes):
            people_list[n].append(i)

        groups = []
        for i in range(1, len(people_list)):
            for j in range(0, len(people_list[i]), i):
                groups.append(people_list[i][j:j + i])
        return groups
```

