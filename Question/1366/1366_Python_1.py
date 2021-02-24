from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        size = len(votes[0])
        count = {ch: [0] * size for ch in votes[0]}

        for vote in votes:
            for i, ch in enumerate(vote):
                count[ch][i] -= 1

        return "".join(sorted(count, key=lambda x: (count[x], x)))


if __name__ == "__main__":
    print(Solution().rankTeams(["ABC", "ACB", "ABC", "ACB", "ACB"]))  # ACB
    print(Solution().rankTeams(["WXYZ", "XYZW"]))  # XWYZ
    print(Solution().rankTeams(["ZMNAGUEDSJYLBOPHRQICWFXTVK"]))  # ZMNAGUEDSJYLBOPHRQICWFXTVK
    print(Solution().rankTeams(["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]))  # ABC
    print(Solution().rankTeams(["M", "M", "M", "M"]))  # M
