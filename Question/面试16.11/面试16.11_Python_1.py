from typing import List


class Solution:
    def divingBoard(self, shorter: int, longer: int, k: int) -> List[int]:
        if k == 0:
            return []

        if shorter == longer:
            return [shorter * k]

        ans = []
        for i in range(k + 1):
            ans.append(longer * i + shorter * (k - i))
        return ans


if __name__ == "__main__":
    print(Solution().divingBoard(1, 1, 0))  # []
    print(Solution().divingBoard(1, 2, 3))  # [3,4,5,6]
