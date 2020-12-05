from typing import List


class Solution:
    def minimalSteps(self, maze: List[str]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().minimalSteps(["S#O", "M..", "M.T"]))  # 16
    print(Solution().minimalSteps(["S#O", "M.#", "M.T"]))  # -1
    print(Solution().minimalSteps(["S#O", "M.T", "M.."]))  # 17
