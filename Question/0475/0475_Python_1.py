from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        # 标注供暖器位置
        distance = [-1] * max(houses + heaters)
        for i in heaters:
            distance[i - 1] = 0

        # 双向遍历
        for i in range(len(distance)):
            if i > 0 and distance[i] == -1 and distance[i - 1] != -1:
                distance[i] = distance[i - 1] + 1

        for i in range(len(distance) - 1, - 1, -1):
            if i < len(distance) - 1 and distance[i + 1] != -1:
                if distance[i] == -1 or distance[i] > distance[i + 1] + 1:
                    distance[i] = distance[i + 1] + 1

        # 计算最大值
        maximum = 0
        for i in houses:
            if distance[i - 1] > maximum:
                maximum = distance[i - 1]
        return maximum


if __name__ == "__main__":
    print(Solution().findRadius([1, 2, 3], [2]))  # 1
    print(Solution().findRadius([1, 5], [2]))  # 3
    print(Solution().findRadius([1, 2, 3, 4], [1, 4]))  # 1
    print(Solution().findRadius([1, 5], [10]))  # 9
