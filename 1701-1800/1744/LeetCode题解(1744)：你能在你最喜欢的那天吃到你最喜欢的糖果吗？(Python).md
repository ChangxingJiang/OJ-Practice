# LeetCode题解(1744)：你能在你最喜欢的那天吃到你最喜欢的糖果吗？(Python)

题目：[原题链接](https://leetcode-cn.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/)（中等）

标签：数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(C+Q)$   | $O(C)$     | 248ms (40.47%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def canEat(self, candies_count: List[int], queries: List[List[int]]) -> List[bool]:
        prefix_candies_count = [0]
        for num in candies_count:
            prefix_candies_count.append(prefix_candies_count[-1] + num)

        ans = []
        for favorite_type, favorite_day, daily_cap in queries:
            min_num = prefix_candies_count[favorite_type] - daily_cap + 1  # 这一天之前吃的最少数量
            max_num = prefix_candies_count[favorite_type] + candies_count[favorite_type] - 1  # 这一天吃的最多数量

            min_eat = 1 * favorite_day
            max_eat = daily_cap * favorite_day

            ans.append(min_num <= min_eat <= max_num or
                       min_num <= max_eat <= max_num or
                       min_eat <= min_num <= max_num <= max_eat)

        return ans
```

