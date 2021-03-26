from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minDifficulty(jobDifficulty=[6, 5, 4, 3, 2, 1], d=2))  # 7
    print(Solution().minDifficulty(jobDifficulty=[9, 9, 9], d=4))  # -1
    print(Solution().minDifficulty(jobDifficulty=[1, 1, 1], d=3))  # 3
    print(Solution().minDifficulty(jobDifficulty=[7, 1, 7, 1, 7, 1], d=3))  # 15
    print(Solution().minDifficulty(jobDifficulty=[11, 111, 22, 222, 33, 333, 44, 444], d=6))  # 843
