from typing import List


class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        d1 = []  # 松果到树的往返的距离
        d2 = []  # 松果到松鼠+松果到树的距离的距离
        for i1, i2 in nuts:
            if 0 <= i1 < height and 0 <= i2 < width:
                d1.append((abs(i1 - tree[0]) + abs(i2 - tree[1])) * 2)
                d2.append(abs(i1 - tree[0]) + abs(i2 - tree[1]) + abs(i1 - squirrel[0]) + abs(i2 - squirrel[1]))

        ans = 0
        more = float("inf")  # 第一个捡的松果的距离变化量
        for i in range(len(d1)):
            ans += d1[i]
            more = min(more, d2[i] - d1[i])

        return ans + more


if __name__ == "__main__":
    # 12
    print(Solution().minDistance(
        height=5,
        width=7,
        tree=[2, 2],
        squirrel=[4, 4],
        nuts=[[3, 0], [2, 5]]
    ))
