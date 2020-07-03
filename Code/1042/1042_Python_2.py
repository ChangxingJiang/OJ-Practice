from typing import List


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        hashmap = [[] for _ in range(N + 1)]
        for path in paths:
            if path[0] > path[1]:
                hashmap[path[0]].append(path[1])
            else:
                hashmap[path[1]].append(path[0])

        color = [0 for _ in range(N + 1)]
        for i in range(1, N + 1):
            apt = [1, 2, 3, 4]
            for near in hashmap[i]:
                if color[near] != 0 and color[near] in apt:
                    apt.remove(color[near])
            color[i] = apt[0]

        return color[1:]


if __name__ == "__main__":
    print(Solution().gardenNoAdj(N=3, paths=[[1, 2], [2, 3], [3, 1]]))  # [1,2,3]
    print(Solution().gardenNoAdj(N=4, paths=[[1, 2], [3, 4]]))  # [1,2,1,2]
    print(Solution().gardenNoAdj(N=4, paths=[[1, 2], [2, 3], [3, 4], [4, 1], [1, 3], [2, 4]]))  # [1,2,3,4]
    print(Solution().gardenNoAdj(N=1, paths=[]))  # [1]
