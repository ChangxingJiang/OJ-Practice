from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)

        dp_0 = [0] * (k + 1)  # 当前已购买 j 次的情况下，没有持仓的收益（当前交易日可以做任何操作）
        dp_1 = [0] * (k + 1)  # 当前已购买 j 次的情况下，仍然持有多单的收益（至少在上一个交易日购入，当前交易日可卖出，但当前交易日不能做其他操作）
        dp_2 = [0] * (k + 1)  # 当前已购买 j 次的情况下，仍然持有空单的收益（至少在上一个交易日购入，当前交易日可卖出，但当前交易日不能做其他操作）

        for i in range(1, n):
            new_dp_0 = [0] * (k + 1)
            new_dp_1 = [0] * (k + 1)
            new_dp_2 = [0] * (k + 1)
            for j in range(k):
                new_dp_0[j] = max(
                    dp_0[j],  # 不作操作（0 > 0）
                    dp_1[j] + (prices[i] - prices[i - 1]),  # 卖出多单（1 > 0）
                    dp_2[j] + (prices[i - 1] - prices[i])  # 卖出空单（2 > 0）
                )
                new_dp_1[j] = max(
                    dp_0[j - 1] if j > 0 else 0,  # 买入多单（0 > 1）
                    dp_1[j] + (prices[i] - prices[i - 1])  # 保留多单（1 > 1）
                )
                new_dp_2[j] = max(
                    dp_0[j - 1] if j > 0 else 0,  # 买入空单（0 > 1）
                    dp_2[j] + (prices[i - 1] - prices[i])  # 保留空单（2 > 2）
                )
            dp_0 = new_dp_0
            dp_1 = new_dp_1
            dp_2 = new_dp_2

        return max(max(dp_0), max(dp_1), max(dp_2))


if __name__ == "__main__":
    print(Solution().maximumProfit(prices=[1, 7, 9, 8, 2], k=2))  # 14
    print(Solution().maximumProfit(prices=[12, 16, 19, 19, 8, 1, 19, 13, 9], k=3))  # 36
