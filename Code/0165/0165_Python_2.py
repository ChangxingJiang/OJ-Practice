class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 将版本号转换为数字列表
        version1 = [int(s) for s in version1.split(".")]
        version2 = [int(s) for s in version2.split(".")]
        N1, N2 = len(version1), len(version2)

        # 比较版本号
        for i in range(max(N1, N2)):
            i1 = version1[i] if i < N1 else 0
            i2 = version2[i] if i < N2 else 0
            if i1 > i2:
                return 1
            elif i1 < i2:
                return -1
        return 0


if __name__ == "__main__":
    print(Solution().compareVersion(version1="0.1", version2="1.1"))  # -1
    print(Solution().compareVersion(version1="1.0.1", version2="1"))  # 1
    print(Solution().compareVersion(version1="7.5.2.4", version2="7.5.3"))  # -1
    print(Solution().compareVersion(version1="1.01", version2="1.001"))  # 0
    print(Solution().compareVersion(version1="1.0", version2="1.0.0"))  # 0
