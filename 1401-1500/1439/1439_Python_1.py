import heapq
from typing import List


class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        # k不大于200，但是所有可能的组合有m^n种，所以用堆可能更合适
        size1, size2 = len(mat), len(mat[0])

        heap = []
        visited = {(0,) * size1}
        heapq.heappush(heap, (sum(m[0] for m in mat), (0,) * size1))

        for _ in range(k - 1):
            val, lst = heapq.heappop(heap)
            for k in range(size1):
                if lst[k] + 1 < size2:
                    new_lst = lst[:k] + (lst[k] + 1,) + lst[k + 1:]
                    if new_lst not in visited:
                        visited.add(new_lst)
                        heapq.heappush(heap, (val + mat[k][lst[k] + 1] - mat[k][lst[k]], tuple(new_lst)))

        return heapq.heappop(heap)[0]


if __name__ == "__main__":
    # 7
    print(Solution().kthSmallest(mat=[[1, 3, 11],
                                      [2, 4, 6]],
                                 k=5))

    # 17
    print(Solution().kthSmallest(mat=[[1, 3, 11],
                                      [2, 4, 6]],
                                 k=9))

    # 9
    print(Solution().kthSmallest(mat=[[1, 10, 10],
                                      [1, 4, 5],
                                      [2, 3, 6]],
                                 k=7))

    # 12
    print(Solution().kthSmallest(mat=[[1, 1, 10],
                                      [2, 2, 9]],
                                 k=7))
