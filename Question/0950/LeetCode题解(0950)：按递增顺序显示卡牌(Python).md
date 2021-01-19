# LeetCode题解(0950)：按递增顺序显示卡牌(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reveal-cards-in-increasing-order/)（中等）

标签：数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 52ms (78.29%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一（情景模拟）：

```python
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        size = len(deck)
        deck.sort()

        index = collections.deque(range(size))
        ans = [0] * size

        for card in sorted(deck):
            ans[index.popleft()] = card
            if index:
                index.append(index.popleft())

        return ans
```

