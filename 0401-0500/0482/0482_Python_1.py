class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        S = S.upper()
        ans = []
        now = ""
        for s in S[::-1]:
            if s.isalnum():
                now += s
                if len(now) == K:
                    ans.append(now[::-1])
                    now = ""
        else:
            if len(now) > 0:
                ans.append(now[::-1])
        return "-".join(ans[::-1])


if __name__ == "__main__":
    print(Solution().licenseKeyFormatting("5F3Z-2e-9-w", 4))  # 5F3Z-2E9W
    print(Solution().licenseKeyFormatting("2-5g-3-J", 2))  # 2-5G-3J
