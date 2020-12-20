from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        pass


if __name__ == "__main__":
    print(Solution().rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"]))  # ACB
    print(Solution().rankTeams(["WXYZ", "XYZW"]))  # XWYZ
    print(Solution().rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))  # ZMNAGUEDSJYLBOPHRQICWFXTVK
    print(Solution().rankTeams(["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]))  # ABC
    print(Solution().rankTeams(["M", "M", "M", "M"]))  # M
