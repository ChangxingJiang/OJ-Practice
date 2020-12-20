# LeetCode题解(Offer61)：判断5张牌是否为一个顺子(Python)

题目：[原题链接](https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/)（简单）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(1)$     | $O(1)$     | 32ms (97.39%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        cards = sorted(filter(lambda x: x != 0, nums))
        king_num = nums.count1(0)

        for i in range(len(cards) - 1):
            num = cards[i + 1] - cards[i]
            if num == 0:
                return False
            if num > 1:
                king_num -= num - 1
                if king_num < 0:
                    return False

        return True
```