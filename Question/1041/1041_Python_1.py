class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, d = 0, 0, 0
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for ch in instructions * 4:
            if ch == "L":
                d = (d - 1) % 4
            elif ch == "R":
                d = (d + 1) % 4
            else:
                x += direction[d][0]
                y += direction[d][1]

        return x == 0 and y == 0


if __name__ == "__main__":
    print(Solution().isRobotBounded("GGLLGG"))  # True
    print(Solution().isRobotBounded("GG"))  # False
    print(Solution().isRobotBounded("GL"))  # True
