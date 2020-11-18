from typing import List


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        lst = [[False, False] for _ in range(n)]
        ans = 0
        for edge in edges:
            t, p1, p2 = edge[0], edge[1] - 1, edge[2] - 1
            if t == 1:
                if lst[p1][0] and lst[p2][0]:
                    ans += 1
                else:
                    lst[p1][0] = True
                    lst[p2][0] = True
            elif t == 2:
                if lst[p1][1] and lst[p2][1]:
                    ans += 1
                else:
                    lst[p1][1] = True
                    lst[p2][1] = True
            else:
                if lst[p1][0] and lst[p2][0] and lst[p1][1] and lst[p2][1]:
                    ans += 1
                else:
                    lst[p1][0] = True
                    lst[p2][0] = True
                    lst[p1][1] = True
                    lst[p2][1] = True
        if all([all(elem) for elem in lst]):
            return ans
        else:
            return -1


if __name__ == "__main__":
    print(Solution().maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 3], [1, 2, 4], [1, 1, 2], [2, 3, 4]]))  # 2
    print(Solution().maxNumEdgesToRemove(n=4, edges=[[3, 1, 2], [3, 2, 3], [1, 1, 4], [2, 1, 4]]))  # 0
    print(Solution().maxNumEdgesToRemove(n=4, edges=[[3, 2, 3], [1, 1, 2], [2, 3, 4]]))  # -1
    print(Solution().maxNumEdgesToRemove(n=2, edges=[[1, 1, 2], [2, 1, 2], [3, 1, 2]]))  # 2
