from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        pass


if __name__ == "__main__":
    print(Solution().findOcurrences(text="alice is a good girl she is a good student", first="a",
                                    second="good"))  # ["girl","student"]
    print(Solution().findOcurrences(text="we will we will rock you", first="we", second="will"))  # ["we","rock"]
