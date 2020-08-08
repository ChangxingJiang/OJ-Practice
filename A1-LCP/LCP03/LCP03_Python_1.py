from typing import List


class Solution:
    def robot(self, command: str, obstacles: List[List[int]], x: int, y: int) -> bool:
        pass


if __name__ == "__main__":
    print(Solution().robot(command="URR", obstacles=[], x=3, y=2))  # True
    print(Solution().robot(command="URR", obstacles=[[2, 2]], x=3, y=2))  # False
    print(Solution().robot(command="URR", obstacles=[[4, 2]], x=3, y=2))  # True
