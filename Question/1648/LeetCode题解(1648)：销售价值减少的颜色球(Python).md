# LeetCode题解(1648)：销售价值减少的颜色球(Python)

题目：[原题链接](https://leetcode-cn.com/problems/sell-diminishing-valued-colored-balls/)（中等）

标签：贪心算法、排序、数学

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时       |
| -------------- | ---------- | ---------- | -------------- |
| Ans 1 (Python) | $O(NlogN)$ | $O(1)$     | 460ms (34.31%) |
| Ans 2 (Python) |            |            |                |
| Ans 3 (Python) |            |            |                |

解法一：

```python
class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        def check(val):
            # O(N)
            total = 0
            for i in inventory:
                if i > val:
                    total += i - val
            return total

        # O(N)
        left, right = 0, max(inventory)

        # 二分查找
        # O(NlogN)
        while left < right:
            mid = (left + right) // 2
            if check(mid) >= orders:
                left = mid + 1
            else:
                right = mid

        # 计算销售临界值
        sale_val = left

        # 计算销售临界值的总量(不卖临界值的情况下)
        sale_num = check(sale_val)

        # 计算临界值之上的结果
        ans = 0
        for i in inventory:
            if i > sale_val:
                ans += (sale_val + 1 + i) * (i - sale_val) // 2
                # print(i, "->", (sale_val + 1 + i) * (i - sale_val) // 2)

        # 计算临界值的结果
        ans += (orders - sale_num) * sale_val

        # print("临界值:", sale_val, sale_num)

        return ans % (10 ** 9 + 7)
```

