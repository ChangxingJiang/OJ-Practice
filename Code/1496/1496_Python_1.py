class Solution:
    def isPathCrossing(self, path: str) -> bool:
        orient = {
            "N": (0, 1),
            "S": (0, -1),
            "E": (1, 0),
            "W": (-1, 0),
        }

        x, y = 0, 0
        already = {(0, 0)}

        for p in path:
            o = orient[p]
            x += o[0]
            y += o[1]
            if (x, y) in already:
                return True
            already.add((x,y))
        else:
            return False


if __name__ == "__main__":
    print(Solution().isPathCrossing(path="NES"))  # False
    print(Solution().isPathCrossing(path="NESWW"))  # True
