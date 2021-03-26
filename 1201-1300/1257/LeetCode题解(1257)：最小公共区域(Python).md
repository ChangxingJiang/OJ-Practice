# LeetCode题解(1257)：最小公共区域(Python)

题目：[原题链接](https://leetcode-cn.com/problems/smallest-common-region/)（中等）

标签：树、深度优先搜索

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(R)$     | $O(R)$     | 320ms (14.29%) |
| Ans 2 (Python) | $O(R)$     | $O(R)$     | 268ms (88.10%) |
| Ans 3 (Python) |            |            |                |

解法一（深度优先搜索）：

```python
class Solution:
    def __init__(self):
        self.hashmap = {}
        self.ans = None

    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        for region in regions:
            self.hashmap[region[0]] = region[1:]

        self.dfs(regions[0][0], region1, region2)
        return self.ans

    def dfs(self, p, r1, r2):
        find = 0
        if p == r1 or p == r2:
            find += 1
        if p in self.hashmap:
            find += sum(self.dfs(c, r1, r2) for c in self.hashmap[p])
        if find == 2:
            if not self.ans:
                self.ans = p
        return find
```

解法二（优化解法一）：

```python
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        for region in reversed(regions):
            if region1 in region:
                region1 = region[0]
            if region2 in region:
                region2 = region[0]
            if region1 == region2:
                return region1
```