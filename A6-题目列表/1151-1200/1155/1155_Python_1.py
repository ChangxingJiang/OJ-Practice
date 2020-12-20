class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().numRollsToTarget(d=1, f=6, target=3))  # 1
    print(Solution().numRollsToTarget(d=2, f=6, target=7))  # 6
    print(Solution().numRollsToTarget(d=2, f=5, target=10))  # 1
    print(Solution().numRollsToTarget(d=1, f=2, target=3))  # 0
    print(Solution().numRollsToTarget(d=30, f=30, target=500))  # 222616187
