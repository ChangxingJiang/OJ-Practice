from typing import List


class Solution:
    def permutation(self, S: str) -> List[str]:
        if len(S) == 1:
            return [S]
        elif len(S) == 2:
            if S[0] == S[1]:
                return [S]
            else:
                return [S, S[::-1]]
        else:
            ans = set()
            for i in range(len(S)):
                ch = S[i]
                for other in self.permutation(S[:i] + S[i + 1:]):
                    ans.add(ch + other)
            return list(ans)


if __name__ == "__main__":
    # ["eqq","qeq","qqe"]
    print(Solution().permutation("qqe"))

    # ["ab", "ba"]
    print(Solution().permutation("ab"))
