from typing import List


class Solution:
    def guardCastle(self, grid: List[str]) -> int:
        pass


if __name__ == "__main__":
    # 3
    print(Solution().guardCastle(grid=["S.C.P#P.", ".....#.S"]))

    # -1
    print(Solution().guardCastle(grid=["SP#P..P#PC#.S", "..#P..P####.#"]))

    # 0
    print(Solution().guardCastle(grid=["SP#.C.#PS", "P.#...#.P"]))

    # 4
    print(Solution().guardCastle(grid=["CP.#.P.", "...S..S"]))
