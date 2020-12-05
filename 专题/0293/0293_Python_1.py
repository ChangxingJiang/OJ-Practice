from typing import List


class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        ans = []
        for i in range(len(s) - 1):
            if s[i:i + 2] == "++":
                ans.append(s[:i] + "--" + s[i + 2:])
        return ans


if __name__ == "__main__":
    # [
    #   "--++",
    #   "+--+",
    #   "++--"
    # ]
    print(Solution().generatePossibleNextMoves(s="++++"))
