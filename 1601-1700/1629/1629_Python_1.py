from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        ans = None
        ans_val = 0
        last = 0
        for i in range(len(releaseTimes)):
            if releaseTimes[i] - last > ans_val:
                ans = keysPressed[i]
                ans_val = releaseTimes[i] - last
            elif releaseTimes[i] - last == ans_val and keysPressed[i] > ans:
                ans = keysPressed[i]

            last = releaseTimes[i]

        return ans


if __name__ == "__main__":
    print(Solution().slowestKey(releaseTimes=[9, 29, 49, 50], keysPressed="cbcd"))  # c
    print(Solution().slowestKey(releaseTimes=[12, 23, 36, 46, 62], keysPressed="spuda"))  # a
