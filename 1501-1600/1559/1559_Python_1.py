import collections
from typing import List


# O(M×N)
# 图 广度优先搜索 哈希表


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        n, m = len(grid), len(grid[0])

        # 寻找所有需要检查的字符
        visited = collections.defaultdict(set)  # 需要检查的字符
        for i in range(n):
            for j in range(m):
                value = grid[i][j]

                # 判断当前位置是否已被查询过，如果已被查询过则跳过
                if (i, j) in visited[value]:
                    continue

                # 如果没被查询过则检查是否存在环
                new_visited = set()
                positions = collections.deque([(None, (i, j))])

                while positions:
                    from_position, now_position = positions.popleft()

                    if now_position not in new_visited:
                        new_visited.add(now_position)
                    else:
                        # 如果检查出环则直接返回结果
                        return True

                    i, j = now_position
                    if i > 0 and grid[i - 1][j] == value and from_position != (i - 1, j):
                        positions.append(((i, j), (i - 1, j)))
                    if i < n - 1 and grid[i + 1][j] == value and from_position != (i + 1, j):
                        positions.append(((i, j), (i + 1, j)))
                    if j > 0 and grid[i][j - 1] == value and from_position != (i, j - 1):
                        positions.append(((i, j), (i, j - 1)))
                    if j < m - 1 and grid[i][j + 1] == value and from_position != (i, j + 1):
                        positions.append(((i, j), (i, j + 1)))

                # 如果没有检查出环在，则记录检查过的点
                visited[value] |= new_visited

        return False


if __name__ == "__main__":
    # True
    print(Solution().containsCycle(
        grid=[["a", "a", "a", "a"], ["a", "b", "b", "a"], ["a", "b", "b", "a"], ["a", "a", "a", "a"]]))

    # True
    print(Solution().containsCycle(
        grid=[["c", "c", "c", "a"], ["c", "d", "c", "c"], ["c", "c", "e", "c"], ["f", "c", "c", "c"]]))

    # False
    print(Solution().containsCycle(grid=[["a", "b", "b"], ["b", "z", "b"], ["b", "b", "a"]]))

    # False
    print(Solution().containsCycle(grid=[["a", "a", "b"]]))

    # True
    print(Solution().containsCycle(grid=[["f", "c", "b", "d", "f", "a", "e", "e", "a", "c", "e"],
                                         ["d", "f", "f", "c", "c", "a", "b", "b", "a", "c", "f"],
                                         ["e", "d", "d", "a", "d", "d", "d", "c", "f", "b", "e"],
                                         ["e", "a", "d", "d", "a", "e", "e", "a", "c", "f", "b"],
                                         ["d", "c", "f", "a", "b", "c", "c", "d", "e", "c", "b"],
                                         ["d", "a", "e", "d", "a", "a", "a", "e", "f", "a", "b"],
                                         ["d", "f", "e", "a", "f", "b", "c", "b", "d", "a", "e"],
                                         ["c", "f", "d", "c", "d", "a", "e", "e", "a", "a", "e"],
                                         ["f", "b", "c", "e", "e", "b", "e", "b", "a", "a", "a"],
                                         ["d", "d", "b", "c", "b", "f", "a", "c", "b", "c", "d"],
                                         ["e", "e", "c", "c", "e", "b", "e", "f", "b", "c", "d"]]))
