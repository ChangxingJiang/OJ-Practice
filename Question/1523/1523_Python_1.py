class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (high - low) % 2 == 1:
            return (high - low) // 2 + 1
        else:
            ans = (high - low) // 2
            ans += 1 if high % 2 == 1 and low % 2 == 1 else 0
            return ans



if __name__ == "__main__":
    print(Solution().countOdds(3, 7))  # 3
    print(Solution().countOdds(8, 10))  # 1
    print(Solution().countOdds(21, 22))  # 1
