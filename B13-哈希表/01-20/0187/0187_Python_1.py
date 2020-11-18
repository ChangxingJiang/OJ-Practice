from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        pass


if __name__ == "__main__":
    # ["AAAAACCCCC","CCCCCAAAAA"]
    print(Solution().findRepeatedDnaSequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

    # ["AAAAAAAAAA"]
    print(Solution().findRepeatedDnaSequences(s="AAAAAAAAAAAAA"))
