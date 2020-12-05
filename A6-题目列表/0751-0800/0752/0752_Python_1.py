from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        pass


if __name__ == "__main__":
    # 6
    print(Solution().openLock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202"))

    # 1
    print(Solution().openLock(deadends=["8888"], target="0009"))  # 1

    # -1
    print(Solution().openLock(deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
                              target="8888"))  # 1

    # -1
    print(Solution().openLock(deadends=["0000"], target="8888"))  # 1
