from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        dp = [True] + [False] * target
        stones.sort()
        for stone in stones:
            for i in range(target, -1, -1):
                if dp[i] is True and i + stone <= target:
                    # print(i, "+", stone, "=", i + stone)
                    dp[i + stone] = True

        # print(total, len(dp), dp)

        while dp and dp[-1] is False:
            dp.pop()

        return int(2 * (total / 2 - (len(dp) - 1)))


if __name__ == "__main__":
    print(Solution().lastStoneWeightII([1, 2]))  # 1
    print(Solution().lastStoneWeightII([2, 7, 4, 1, 8, 1]))  # 1
    print(Solution().lastStoneWeightII([8, 2, 4, 4, 8]))  # 2
    print(Solution().lastStoneWeightII([31, 26, 33, 21, 40]))  # 5
    print(Solution().lastStoneWeightII([21, 60, 61, 20, 31]))  # 9
