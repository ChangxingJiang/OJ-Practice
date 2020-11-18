class Solution:
    def minimumOperations(self, leaves: str) -> int:
        a, b, c = int(leaves[0] == "y"), float("inf"), float("inf")
        for leave in leaves[1:]:
            a, b, c = a + int(leave == "y"), min(a, b) + int(leave == "r"), min(b, c) + int(leave == "y")
        return int(c)


if __name__ == "__main__":
    print(Solution().minimumOperations("rrryyyrryyyrr"))  # 2
    print(Solution().minimumOperations("ryr"))  # 0
