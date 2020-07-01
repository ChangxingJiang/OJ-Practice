class Solution:
    def toLowerCase(self, str: str) -> str:
        return str.lower()


if __name__ == "__main__":
    print(Solution().toLowerCase("Hello"))  # hello
    print(Solution().toLowerCase("here"))  # here
    print(Solution().toLowerCase("LOVELY"))  # lovely
