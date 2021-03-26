# LeetCode题解(0188)：买卖股票的最佳时机IV(Python)

题目：[原题链接](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv/)（困难）

标签：动态规划

| 解法           | 时间复杂度      | 空间复杂度    | 执行用时      |
| -------------- | --------------- | ------------- | ------------- |
| Ans 1 (Python) | $O(N×min(N,K))$ | $O(min(N,K))$ | 84ms (97.65%) |
| Ans 2 (Python) |                 |               |               |
| Ans 3 (Python) |                 |               |               |

解法一：

```python
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # 将price数组转换为递增递减段落数组
        # O(P)
        nums = collections.deque()
        for i in range(len(prices) - 1):
            num = prices[i + 1] - prices[i]
            if not nums:
                if num != 0:
                    nums.append(num)
            elif nums[-1] * num > 0:
                nums[-1] += num
            elif nums[-1] * num < 0:
                nums.append(num)

        # 剔除递增递减段落数组首尾的递减段落
        # O(1)
        if nums and nums[0] < 0:
            nums.popleft()
        if nums and nums[-1] < 0:
            nums.pop()

        # 如果没有递增段落，则无法获利，返回0
        # O(1)
        if not nums:
            return 0

        # 计算递增段落的总数
        # O(1)
        size = len(nums) // 2 + 1

        # 处理可交易次数大于等于递增段落总数的情况：直接返回所有递增段落的总和即可
        # O(N)
        if k >= size:
            return sum(nums[i * 2] for i in range(size))

        # 构造状态矩阵
        # O(K)
        # 状态矩阵说明
        # i == 0 : 执行0笔交易的最大利润
        # i == 1 : 执行1笔交易尚未卖出的最大利润
        # i == 2 : 执行1笔交易已经卖出的最大利润
        # i == 3 : 执行2笔交易尚未卖出的最大利润
        # i == 4 : 执行2笔交易已经卖出的最大利润
        # ......
        dp = [0] * (k * 2 + 1)

        # 计算状态转移
        # O(N×K)
        for i in range(len(nums)):
            # 因为可以在同一时间点连续购买、抛售股票，因此仅第一天就可以达到k笔交易

            for j in range(k * 2, 0, -1):
                # 处理尚未卖出情况下的最大利润
                if j % 2 == 1:
                    dp[j] = max(
                        dp[j] + nums[i],  # 仍然保持持有状态：第i-1次递增递减段落的k次交易尚未卖出的最大利润加第i次递增递减的价格变动
                        dp[j - 1] + nums[i]  # 当日重新购入股票：第i-1次递增递减段落的k-1次交易已经卖出的最大利润加第i次递增递减的价格变动
                    )

                # 处理已经卖出情况下的最大利润
                else:
                    dp[j] = max(
                        dp[j],  # 仍然保持没有持有的状态：第i-1次递增递减段落的k次交易已经卖出的最大利润
                        dp[j - 1] + nums[i],  # 当日抛售正在持有的股票：第i-1次递增递减段落的k次交易尚未卖出的最大利润加第i次递增递减的价格变动
                        dp[j - 2] + nums[i]  # 当日购入并抛售股票：第i-1次递增递减段落的k次交易已经卖出的最大利润加第i次递增递减的价格变动
                    )

        return dp[-1]
```