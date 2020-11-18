# O(N) O(N)
# 哈希表

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        n1, n2 = 0, 0
        visited = {(n1, n2)}

        for ch in path:
            if ch == "N":
                n1 += 1
            elif ch == "S":
                n1 -= 1
            elif ch == "W":
                n2 -= 1
            elif ch == "E":
                n2 += 1

            if (n1, n2) not in visited:
                visited.add((n1, n2))
            else:
                return True

        return False


if __name__ == "__main__":
    print(Solution().isPathCrossing(path="NES"))  # False
    print(Solution().isPathCrossing(path="NESWW"))  # True
