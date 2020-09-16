from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        c = int(pow(area, 0.5))
        while area % c != 0:
            c -= 1
        else:
            return [area // c, c]


if __name__ == "__main__":
    print(Solution().constructRectangle(4))  # [2,2]
