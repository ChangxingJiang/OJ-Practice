class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        pass


if __name__ == "__main__":
    print(Solution().compareVersion(version1="0.1", version2="1.1"))  # -1
    print(Solution().compareVersion(version1="1.0.1", version2="1"))  # 1
    print(Solution().compareVersion(version1="7.5.2.4", version2="7.5.3"))  # -1
    print(Solution().compareVersion(version1="1.01", version2="1.001"))  # 0
    print(Solution().compareVersion(version1="1.0", version2="1.0.0"))  # 0
