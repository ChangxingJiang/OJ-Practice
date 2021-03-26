from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = 0
        for b in bits[-2::-1]:
            if b == 0:
                break
            else:
                n += 1
        return n % 2 == 0


if __name__ == "__main__":
    print(Solution().isOneBitCharacter([1, 0, 0]))  # True
    print(Solution().isOneBitCharacter([1, 1, 1, 0]))  # False
