class Solution:
    def beautySum(self, s: str) -> int:
        ans = 0

        size = len(s)
        for i in range(size):
            fre_list = [0] * 26
            for j in range(i, size):
                idx = ord(s[j]) - 97
                fre_list[idx] += 1
                ans += max(fre_list) - min(fre for fre in fre_list if fre > 0)

        return ans


if __name__ == "__main__":
    print(Solution().beautySum("aabcb"))  # 5
    print(Solution().beautySum("aabcbaa"))  # 17
