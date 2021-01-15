from typing import List


class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        n = len(aliceValues)

        # 按两人总分排序石子
        lst = [(aliceValues[i], bobValues[i]) for i in range(n)]
        lst.sort(key=lambda x: x[0] + x[1], reverse=True)

        alice, bob = 0, 0
        for i in range(len(lst)):
            if i % 2 == 0:
                alice += lst[i][0]
            else:
                bob += lst[i][1]

        if alice > bob:
            return 1
        elif alice < bob:
            return -1
        else:
            return 0


if __name__ == "__main__":
    print(Solution().stoneGameVI(aliceValues=[1, 3], bobValues=[2, 1]))  # 1
    print(Solution().stoneGameVI(aliceValues=[1, 2], bobValues=[3, 1]))  # 0
    print(Solution().stoneGameVI(aliceValues=[2, 4, 3], bobValues=[1, 6, 7]))  # -1
