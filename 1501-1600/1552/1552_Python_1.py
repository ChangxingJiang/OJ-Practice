from typing import List


class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # 处理特殊情况
        if m == 2:
            return max(position) - min(position)

        # 计算距离列表
        position.sort()
        distances = []
        for i in range(len(position) - 1):
            distances.append(position[i + 1] - position[i])

        # 计算需要切割的次数
        cut = m - 2

        # 计算可以合并的次数
        merge = len(distances) - 1 - cut
        print("合并次数:", merge, distances)

        # 每次将最小值和旁边的更小的值合并
        while merge:
            min_distance = min(distances)

            new_distances = []

            i = 0
            while merge and i < len(distances):
                if distances[i] == min_distance:
                    if 0 < i < len(distances) - 1:
                        if distances[i - 1] < distances[i + 1]:
                            new_distances[-1] += distances[i]
                            merge -= 1
                        else:
                            new_distances.append(distances[i] + distances[i + 1])
                            i += 1
                            merge -= 1
                    elif i > 0:
                        new_distances[-1] += distances[i]
                        merge -= 1
                    elif i < len(distances) - 1:
                        new_distances.append(distances[i] + distances[i + 1])
                        i += 1
                        merge -= 1
                else:
                    new_distances.append(distances[i])

                i += 1

            distances = new_distances

            print("合并结果:", distances)

        return min(distances)


if __name__ == "__main__":
    print(Solution().maxDistance(position=[1, 2, 3, 4, 7], m=3))  # 3
    print(Solution().maxDistance(position=[5, 4, 3, 2, 1, 1000000000], m=2))  # 999999999
    print(Solution().maxDistance(position=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], m=4))  # 999999999
