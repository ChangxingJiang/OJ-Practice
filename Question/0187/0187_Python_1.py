from typing import List


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = set()
        count = set()
        for i in range(len(s) - 9):
            ch = s[i:i + 10]
            if ch not in count:
                count.add(ch)
            else:
                ans.add(ch)
        return list(ans)


if __name__ == "__main__":
    # ["AAAAACCCCC","CCCCCAAAAA"]
    print(Solution().findRepeatedDnaSequences(s="AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))

    # ["AAAAAAAAAA"]
    print(Solution().findRepeatedDnaSequences(s="AAAAAAAAAAAAA"))

    # ["AAAAAAAAAA"]
    print(Solution().findRepeatedDnaSequences(s="AAAAAAAAAAA"))
