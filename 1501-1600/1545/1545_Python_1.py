class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        count = 0
        for i in [2 ** i for i in range(20, 0, -1)]:
            if k > i:
                k = 2 * i - k
                count += 1
            elif k == i:
                return "1" if count % 2 == 0 else "0"
        return "0" if count % 2 == 0 else "1"


if __name__ == "__main__":
    print(Solution().findKthBit(n=3, k=1))  # 0
    print(Solution().findKthBit(n=4, k=11))  # 1
    print(Solution().findKthBit(n=1, k=1))  # 0
    print(Solution().findKthBit(n=2, k=3))  # 1
    print(Solution().findKthBit(n=3, k=5))  # 0
    print(Solution().findKthBit(n=4, k=12))  # 0
