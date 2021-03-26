class Solution:
    _MOD = 10 ** 9 + 7

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp1 = [1] + [0] * target

        for _ in range(d):
            dp2 = [0] * (target + 1)
            for i in range(target + 1):
                if dp1[i] > 0:
                    for j in range(i + 1, min(i + f + 1, target + 1)):
                        dp2[j] += dp1[i]
                        dp2[j] %= self._MOD
            dp1 = dp2

        return dp1[target]


if __name__ == "__main__":
    print(Solution().numRollsToTarget(d=1, f=6, target=3))  # 1
    print(Solution().numRollsToTarget(d=2, f=6, target=7))  # 6
    print(Solution().numRollsToTarget(d=2, f=5, target=10))  # 1
    print(Solution().numRollsToTarget(d=1, f=2, target=3))  # 0
    print(Solution().numRollsToTarget(d=30, f=30, target=500))  # 222616187
