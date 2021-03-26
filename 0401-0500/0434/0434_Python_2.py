class Solution:
    def countSegments(self, s: str) -> int:
        not_space = False
        ans = 0
        for c in s:
            if c != " ":
                not_space = True
            else:
                if not_space:
                    ans += 1
                    not_space = False
        ans += not_space
        return ans


if __name__ == "__main__":
    print(Solution().countSegments("Hello, my name is John"))  # 5
    print(Solution().countSegments("Of all the gin joints in all the towns in all the world,   "))  # 13
