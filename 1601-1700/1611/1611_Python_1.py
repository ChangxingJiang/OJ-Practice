class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # if n == 0:
        #     return 0

        nums = bin(n)[2:]
        # print("当前位情况:", nums)

        # 想降位必须形如1100...的形式
        # 想进位必须形式1000...的形式

        # 0
        # 1
        # 11 10
        # 110 111 101 100
        # 1100 1101 111 1110 1010 1011 1001 1000
        # 上一位是0的时候，下一位的顺序就是1->0；上一位是1的时候，下一位的顺序就是0->1
        # 每一位的0和1的顺序不断调换

        ans = 0
        N = len(nums)
        stat = 0  # 当前的情况
        # 0 还没有出现1
        # 1 出现了一个1（奇数个1）
        # 2 出现了两个1（偶数个1）
        for i, ch in enumerate(nums):
            n = 2 ** (N - i - 1)
            if stat == 0:
                if ch == "1":
                    ans += n
                    stat = 1
            elif stat == 1:
                if ch == "0":
                    ans += n
                else:
                    stat = 2
            elif stat == 2:
                if ch == "1":
                    ans += n
                    stat = 1

        return ans


if __name__ == "__main__":
    print(Solution().minimumOneBitOperations(0))  # 0
    print(Solution().minimumOneBitOperations(3))  # 2
    print(Solution().minimumOneBitOperations(6))  # 4
    print(Solution().minimumOneBitOperations(9))  # 14
    print(Solution().minimumOneBitOperations(333))  # 393
