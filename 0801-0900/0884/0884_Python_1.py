from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        A = A.split(" ")
        B = B.split(" ")
        ans = []
        for a in A:
            if a not in B and A.count(a) == 1:
                ans.append(a)
        for b in B:
            if b not in A and B.count(b) == 1:
                ans.append(b)
        return ans


if __name__ == "__main__":
    print(Solution().uncommonFromSentences(A="this apple is sweet", B="this apple is sour"))  # ["sweet","sour"]
    print(Solution().uncommonFromSentences(A="apple apple", B="banana"))  # ["banana"]
