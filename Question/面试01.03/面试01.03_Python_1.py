class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        return S[:length].replace(" ", "%20")


if __name__ == "__main__":
    print(Solution().replaceSpaces("Mr John Smith    ", 13))  # "Mr%20John%20Smith"
    print(Solution().replaceSpaces("               ", 5))  # "%20%20%20%20%20"
