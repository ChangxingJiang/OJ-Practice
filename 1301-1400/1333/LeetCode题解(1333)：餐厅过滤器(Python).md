# LeetCode题解(1333)：餐厅过滤器(Python)

题目：[原题链接](https://leetcode-cn.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/)（中等）

标签：排序、数组

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(N)$     | 64ms (51.65%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

解法一：

```python
class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> \
            List[int]:
        restaurants = [restaurant for restaurant in restaurants
                       if restaurant[2] >= veganFriendly and restaurant[3] <= maxPrice and restaurant[4] <= maxDistance]
        restaurants.sort(key=lambda x: (x[1], x[0]), reverse=True)
        return [restaurant[0] for restaurant in restaurants]
```

