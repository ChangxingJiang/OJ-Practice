import string


class Solution:
    def removeDuplicates(self, S: str) -> str:
        duplicates = {2 * ch for ch in string.ascii_lowercase}

        last_length = -1
        while len(S) != last_length:
            last_length = len(S)
            for d in duplicates:
                S = S.replace(d, "")

        return S


if __name__ == "__main__":
    print(Solution().removeDuplicates("abbaca"))  # ca
