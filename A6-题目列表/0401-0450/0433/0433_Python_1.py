from typing import List


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        pass


if __name__ == "__main__":
    # 1
    print(Solution().minMutation(start="AACCGGTT",
                                 end="AACCGGTA",
                                 bank=["AACCGGTA"]))

    # 2
    print(Solution().minMutation(start="AACCGGTT",
                                 end="AAACGGTA",
                                 bank=["AACCGGTA", "AACCGCTA", "AAACGGTA"]))

    # 3
    print(Solution().minMutation(start="AAAAACCC",
                                 end="AACCCCCC",
                                 bank=["AAAACCCC", "AAACCCCC", "AACCCCCC"]))
