from typing import List


class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().pyramidTransition(bottom="BCD", allowed=["BCG", "CDE", "GEA", "FFF"]))  # True
    print(Solution().pyramidTransition(bottom="AABA", allowed=["AAA", "AAB", "ABA", "ABB", "BAC"]))  # False
