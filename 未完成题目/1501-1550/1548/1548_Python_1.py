from typing import List


class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        pass


if __name__ == "__main__":
    # [0,2,4,2]
    print(Solution().mostSimilar(n=5, roads=[[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]],
                                 names=["ATL", "PEK", "LAX", "DXB", "HND"], targetPath=["ATL", "DXB", "HND", "LAX"]))

    # [0,1,0,1,0,1,0,1]
    print(Solution().mostSimilar(n=4, roads=[[1, 0], [2, 0], [3, 0], [2, 1], [3, 1], [3, 2]],
                                 names=["ATL", "PEK", "LAX", "DXB"],
                                 targetPath=["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX"]))

    # [3,4,5,4,3,2,1]
    print(Solution().mostSimilar(n=6, roads=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],
                                 names=["ATL", "PEK", "LAX", "ATL", "DXB", "HND"],
                                 targetPath=["ATL", "DXB", "HND", "DXB", "ATL", "LAX", "PEK"]))
