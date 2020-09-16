def isBadVersion(version):
    return version >= 4


class Solution:
    def firstBadVersion(self, n):
        left, right = 0, n
        while (right - left) > 1:
            binery = left + (right - left) // 2
            binery_ans = isBadVersion(binery)
            if binery_ans:
                right = binery
            else:
                left = binery
        return right


if __name__ == "__main__":
    print(Solution().firstBadVersion(5))  # 4
