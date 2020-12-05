from typing import List


class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        pass


if __name__ == "__main__":
    # 2
    print(Solution().regionsBySlashes([
        " /",
        "/ "
    ]))

    # 1
    print(Solution().regionsBySlashes([
        " /",
        "  "
    ]))

    # 4
    print(Solution().regionsBySlashes([
        "\\/",
        "/\\"
    ]))

    # 5
    print(Solution().regionsBySlashes([
        "/\\",
        "\\/"
    ]))

    # 3
    print(Solution().regionsBySlashes([
        "//",
        "/ "
    ]))
