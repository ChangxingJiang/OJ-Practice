from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if ord(letters[-1]) <= ord(target):
            return letters[0]
        left = 0
        right = len(letters) - 1
        while left < right:
            mid = (left + right) // 2
            if ord(letters[mid]) <= ord(target):
                left = mid + 1
            else:
                right = mid
        return letters[left]


if __name__ == "__main__":
    print(Solution().nextGreatestLetter(["c", "f", "j"], "a"))  # c
    print(Solution().nextGreatestLetter(["c", "f", "j"], "c"))  # f
    print(Solution().nextGreatestLetter(["c", "f", "j"], "d"))  # f
    print(Solution().nextGreatestLetter(["c", "f", "j"], "g"))  # j
    print(Solution().nextGreatestLetter(["c", "f", "j"], "j"))  # c
    print(Solution().nextGreatestLetter(["c", "f", "j"], "k"))  # c
