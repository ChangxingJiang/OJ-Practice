from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        if len(S) == 2:
            return [S, S[::-1]]
        else:
            ans = []
            for i in range(len(S)):
                ch = S[i]
                for other in self.permutation(S[:i] + S[i + 1:]):
                    ans.append(ch + other)
            return ans


if __name__ == "__main__":
    # ["qwe", "qew", "wqe", "weq", "ewq", "eqw"]
    print(Solution().permutation("qwe"))

    # ["ab", "ba"]
    print(Solution().permutation("ab"))
