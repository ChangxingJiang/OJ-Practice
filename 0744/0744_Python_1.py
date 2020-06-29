from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        pass


if __name__ == "__main__":
    print(Solution().nextGreatestLetter(["c", "f", "j"], "a"))  # c
    print(Solution().nextGreatestLetter(["c", "f", "j"], "c"))  # f
    print(Solution().nextGreatestLetter(["c", "f", "j"], "d"))  # f
    print(Solution().nextGreatestLetter(["c", "f", "j"], "g"))  # j
    print(Solution().nextGreatestLetter(["c", "f", "j"], "f"))  # c
    print(Solution().nextGreatestLetter(["c", "f", "j"], "k"))  # c
