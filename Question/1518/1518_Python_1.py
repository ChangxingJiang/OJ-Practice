# 情景模拟
# O(NlogN)

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans = empty = numBottles

        while empty >= numExchange:
            drink, surplus_empty = divmod(empty, numExchange)
            ans += drink
            empty = drink + surplus_empty

        return ans


if __name__ == "__main__":
    print(Solution().numWaterBottles(numBottles=9, numExchange=3))  # 13
    print(Solution().numWaterBottles(numBottles=15, numExchange=4))  # 19
    print(Solution().numWaterBottles(numBottles=5, numExchange=5))  # 6
    print(Solution().numWaterBottles(numBottles=2, numExchange=3))  # 2
