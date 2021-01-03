from typing import List


class Solution:
    def boxDelivering(self, boxes: List[List[int]], portsCount: int, maxBoxes: int, maxWeight: int) -> int:
        pass


if __name__ == "__main__":
    print(Solution().boxDelivering(boxes=[[1, 1], [2, 1], [1, 1]], portsCount=2, maxBoxes=3, maxWeight=3))  # 4
    print(Solution().boxDelivering(boxes=[[1, 2], [3, 3], [3, 1], [3, 1], [2, 4]], portsCount=3, maxBoxes=3,
                                   maxWeight=6))  # 6
    print(Solution().boxDelivering(boxes=[[1, 4], [1, 2], [2, 1], [2, 1], [3, 2], [3, 4]], portsCount=3, maxBoxes=6,
                                   maxWeight=7))  # 6
    print(Solution().boxDelivering(boxes=[[2, 4], [2, 5], [3, 1], [3, 2], [3, 7], [3, 1], [4, 4], [1, 3], [5, 2]],
                                   portsCount=5, maxBoxes=5, maxWeight=7))  # 14
