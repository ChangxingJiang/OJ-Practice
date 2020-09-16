from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        ans = [S]
        for i in range(len(S)):
            s = S[i]
            if s.isalpha():
                new = []
                for a in ans:
                    new.append(a[:i] + s.lower() + a[i + 1:])
                    new.append(a[:i] + s.upper() + a[i + 1:])
                ans = new
        return ans


if __name__ == "__main__":
    print(Solution().letterCasePermutation("a1b2"))  # ["a1b2", "a1B2", "A1b2", "A1B2"]
    print(Solution().letterCasePermutation("3z4"))  # ["3z4", "3Z4"]
    print(Solution().letterCasePermutation("12345"))  # ["12345"]
