from typing import List


class Solution:
    def findCoins(self, numWays: List[int]) -> List[int]:
        coin = []
        n = len(numWays)

        # res[i]：金额 i 有 res[i] 种方法
        res = [0] * (n + 1)
        res[0] = 1  # 金额 0 有一种方法

        for i in range(1, n + 1):
            way = numWays[i - 1]

            if res[i] == way:
                continue
            elif res[i] == way - 1:
                coin.append(i)
                for j in range(i, n + 1, 1):
                    res[j] += res[j - i]
            else:
                return []

        return coin


if __name__ == "__main__":
    print(Solution().findCoins([0, 1, 0, 2, 0, 3, 0, 4, 0, 5]))  # [2,4,6]
    print(Solution().findCoins([1, 2, 2, 3, 4]))  # [1,2,5]
    print(Solution().findCoins([1, 2, 3, 4, 15]))  # []
