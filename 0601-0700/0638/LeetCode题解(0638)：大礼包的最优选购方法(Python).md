# LeetCode题解(0638)：大礼包的最优选购方法(Python)

题目：[原题链接](https://leetcode-cn.com/problems/shopping-offers/)（中等）

标签：动态规划、深度优先搜索、记忆化递归

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N^S)$   | $O(N+S)$   | 84ms (81.82%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def __init__(self):
        self.price = []
        self.special = []

    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        self.price = price
        self.special = special
        return self.dfs(needs)

    def dfs(self, needs):
        ans = self.buy(needs)
        for special in self.special:
            clone = needs.copy()
            for i in range(len(needs)):
                clone[i] -= special[i]
                if clone[i] < 0:
                    break
            else:
                ans = min(ans, special[-1] + self.dfs(clone))
        return ans

    def buy(self, needs):
        """直接购买"""
        return sum(needs[i] * self.price[i] for i in range(len(needs)))
```

