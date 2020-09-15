from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # 计算距离列表
        connects = []
        for i in range(len(points)):
            line = []
            p1 = points[i]
            for j in range(len(points)):
                p2 = points[j]
                distance = abs(p2[0] - p1[0]) + abs(p2[1] - p1[1])
                line.append(distance)
            connects.append(line)

        print(connects)

        ans = 0
        visited = {0}
        for i in range(len(connects)):
            min_val = float("inf")
            min_idx = 0
            for j in range(len(connects[i])):
                print("i=" + str(i), ";", "j=" + str(j), ";",
                      connects[i][j], min_val, "->", connects[i][j] < min_val,
                      (i in visited and j not in visited),
                      (i not in visited and j in visited))
                if i != j and connects[i][j] < min_val:
                    if (i in visited and j not in visited) or (i not in visited and j in visited):  # 有一条边是老边，有一条边是新边
                        min_idx = j
                        min_val = connects[i][j]
            visited.add(i)
            visited.add(min_idx)
            ans += min_val
            print(ans, visited, min_val, connects[i])

        return ans


if __name__ == "__main__":
    print(Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))  # 20
    print(Solution().minCostConnectPoints([[0, 0], [1, 1], [1, 0], [-1, 1]]))  # 4
