from typing import List


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        t = False
        for i in range(len(bits) - 1):
            if t:
                t = False
            else:
                if bits[i] == 1:
                    t = True
        return not t


if __name__ == "__main__":
    print(Solution().isOneBitCharacter([1, 0, 0]))  # True
    print(Solution().isOneBitCharacter([1, 1, 1, 0]))  # False
