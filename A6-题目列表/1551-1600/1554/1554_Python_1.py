from typing import List


class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().differByOne(dict=["abcd", "acbd", "aacd"]))  # True
    print(Solution().differByOne(dict=["ab", "cd", "yz"]))  # False
    print(Solution().differByOne(dict=["abcd", "cccc", "abyd", "abab"]))  # True
