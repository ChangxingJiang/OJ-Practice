from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().compress(["a", "a", "b", "b", "c", "c", "c"]))  # 6
    print(Solution().compress(["a"]))  # 1
    print(Solution().compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))  # 4
