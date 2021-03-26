from typing import List


class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        ans = 0

        stat = [0] * len(light)  # 当前亮灯状态
        now = 0  # 当前全亮的最右侧位置

        for i in range(len(light)):
            stat[light[i] - 1] = 1

            while now < len(light) and stat[now]:
                now += 1

            if now == i + 1:
                ans += 1

        return ans


if __name__ == "__main__":
    print(Solution().numTimesAllBlue([2, 1, 3, 5, 4]))  # 3
    print(Solution().numTimesAllBlue([3, 2, 4, 1, 5]))  # 2
    print(Solution().numTimesAllBlue([4, 1, 2, 3]))  # 1
    print(Solution().numTimesAllBlue([2, 1, 4, 3, 6, 5]))  # 3
    print(Solution().numTimesAllBlue([1, 2, 3, 4, 5, 6]))  # 6
