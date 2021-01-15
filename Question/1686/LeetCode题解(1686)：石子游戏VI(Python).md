# LeetCode题解(1686)：石子游戏VI(Python)

题目：[原题链接](https://leetcode-cn.com/problems/stone-game-vi/)（中等）

标签：排序、贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 296ms (68.85%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)

        # 按两人总分排序石子
        lst = [(aliceValues[i], bobValues[i]) for i in range(n)]
        lst.sort(key=lambda x: x[0] + x[1], reverse=True)

        alice, bob = 0, 0
        for i in range(len(lst)):
            if i % 2 == 0:
                alice += lst[i][0]
            else:
                bob += lst[i][1]

        if alice > bob:
            return 1
        elif alice < bob:
            return -1
        else:
            return 0
```

