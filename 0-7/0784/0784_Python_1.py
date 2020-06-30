from typing import List


class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        pass


if __name__ == "__main__":
    print(Solution().letterCasePermutation("a1b2"))  # ["a1b2", "a1B2", "A1b2", "A1B2"]
    print(Solution().letterCasePermutation("3z4"))  # ["3z4", "3Z4"]
    print(Solution().letterCasePermutation("12345"))  # ["12345"]
