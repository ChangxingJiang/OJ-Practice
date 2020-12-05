class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().shortestWay(source="abc", target="abcbc"))  # 2
    print(Solution().shortestWay(source="abc", target="acdbc"))  # -1
    print(Solution().shortestWay(source="xyz", target="xzyxz"))  # 3
