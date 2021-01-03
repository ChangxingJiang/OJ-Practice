from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        cuboids = [list(sorted(cuboid, reverse=True)) for cuboid in cuboids]
        cuboids.sort(reverse=True)

        # print(cuboids)

        size = len(cuboids)

        dp = [cuboids[i][0] for i in range(size)]

        for i in range(size):
            x1, y1, z1 = cuboids[i]
            for j in range(i):
                x2, y2, z2 = cuboids[j]
                if x1 <= x2 and y1 <= y2 and z1 <= z2:
                    dp[i] = max(dp[i], dp[j] + x1)

        return max(dp)


if __name__ == "__main__":
    print(Solution().maxHeight(cuboids=[[50, 45, 20], [95, 37, 53], [45, 23, 12]]))  # 190
    print(Solution().maxHeight(cuboids=[[38, 25, 45], [76, 35, 3]]))  # 76
    print(Solution().maxHeight(
        cuboids=[[7, 11, 17], [7, 17, 11], [11, 7, 17], [11, 17, 7], [17, 7, 11], [17, 11, 7]]))  # 102

    # 301
    print(Solution().maxHeight(
        [[74, 7, 80], [7, 52, 61], [62, 41, 37], [91, 58, 26], [88, 98, 5], [72, 93, 23], [56, 58, 94], [88, 8, 64],
         [32, 55, 5]]))
