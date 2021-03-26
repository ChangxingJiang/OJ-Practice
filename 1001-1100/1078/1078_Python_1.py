from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        text = text.split(" ")
        ans = []
        for i in range(len(text) - 2):
            if text[i] == first and text[i + 1] == second:
                ans.append(text[i + 2])
        return ans


if __name__ == "__main__":
    print(Solution().findOcurrences(text="alice is a good girl she is a good student", first="a",
                                    second="good"))  # ["girl","student"]
    print(Solution().findOcurrences(text="we will we will rock you", first="we", second="will"))  # ["we","rock"]
