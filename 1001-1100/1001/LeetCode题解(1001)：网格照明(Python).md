# LeetCode题解(1001)：网格照明(Python)

题目：[原题链接](https://leetcode-cn.com/problems/grid-illumination/)（困难）

标签：哈希表、几何

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(L+Q)$   | $O(L)$     | 496ms (25.45%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def gridIllumination(self, N: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        def is_valid(x, y):
            return 0 <= x < N and 0 <= y < N

        def near(x, y):
            maybe = [(x, y), (x - 1, y - 1), (x - 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1), (x + 1, y),
                     (x + 1, y - 1), (x, y - 1)]
            return [(x, y) for x, y in maybe if is_valid(x, y)]

        size1, size2 = len(lamps), len(queries)

        count1 = collections.Counter()
        count2 = collections.Counter()
        count3 = collections.Counter()
        count4 = collections.Counter()

        count_lamp = {(x, y) for x, y in lamps}

        for i in range(size1):
            x1, y1 = lamps[i]
            count1[x1] += 1
            count2[y1] += 1
            count3[x1 - y1] += 1
            count4[x1 + y1] += 1

        ans = []

        for i in range(size2):
            # 查询
            x2, y2 = queries[i]
            if count1[x2] > 0 or count2[y2] > 0 or count3[x2 - y2] > 0 or count4[x2 + y2] > 0:
                ans.append(1)
            else:
                ans.append(0)

            # 关灯
            for x1, y1 in near(x2, y2):
                if (x1, y1) in count_lamp:
                    count1[x1] -= 1
                    count2[y1] -= 1
                    count3[x1 - y1] -= 1
                    count4[x1 + y1] -= 1
                    count_lamp.remove((x1, y1))

            # print(count1, count2, count3, count4, count_lamp)

        return ans
```