class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 将版本号转换为数字列表
        version1 = [int(s) for s in version1.split(".")]
        version2 = [int(s) for s in version2.split(".")]

        # 移除版本号末尾多余的0
        while version1 and version1[-1] == 0:
            version1.pop()
        while version2 and version2[-1] == 0:
            version2.pop()

        # 比较版本号
        while version1 or version2:
            if not version1:
                return -1
            if not version2:
                return 1
            v1 = version1.pop(0)
            v2 = version2.pop(0)
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0


if __name__ == "__main__":
    print(Solution().compareVersion(version1="0.1", version2="1.1"))  # -1
    print(Solution().compareVersion(version1="1.0.1", version2="1"))  # 1
    print(Solution().compareVersion(version1="7.5.2.4", version2="7.5.3"))  # -1
    print(Solution().compareVersion(version1="1.01", version2="1.001"))  # 0
    print(Solution().compareVersion(version1="1.0", version2="1.0.0"))  # 0
