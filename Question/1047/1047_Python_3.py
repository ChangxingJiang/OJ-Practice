import re


class Solution:
    def removeDuplicates(self, S: str) -> str:
        last_length = -1
        while len(S) != last_length:
            last_length = len(S)
            S = re.sub(r"(.)\1", "", S)
        return S


if __name__ == "__main__":
    print(Solution().removeDuplicates("abbaca"))  # ca
