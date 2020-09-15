from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        visited_group = []
        for edge in edges:
            group0, group1 = None, None
            for group in visited_group:
                if edge[0] in group:
                    group0 = group
                if edge[1] in group:
                    group1 = group
            if group0 and group1:
                if group0 == group1:
                    return edge
                else:
                    visited_group.remove(group0)
                    visited_group.remove(group1)
                    visited_group.append(group0 | group1)
            elif group0:
                group0.add(edge[1])
            elif group1:
                group1.add(edge[0])
            else:
                visited_group.append({edge[0], edge[1]})


if __name__ == "__main__":
    print(Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # [2,3]
    print(Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))  # [1,4]
    print(Solution().findRedundantConnection([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]))  # [2,5]
