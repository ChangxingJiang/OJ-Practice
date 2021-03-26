from typing import List


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        c = pow(area, 0.5)
        l = w = int(c)  # l>w
        while l * w != area:
            if l * w < area:
                l += 1
            else:
                w -= 1
        return [l, w]


if __name__ == "__main__":
    print(Solution().constructRectangle(4))  # [2,2]
