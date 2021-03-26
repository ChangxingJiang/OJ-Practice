class Solution:
    def reachNumber(self, target: int) -> int:
        # 1 : [1]
        # 2 : [1,3]
        # 3 : [2,4,6]
        # 4 : [4,6,8,10]
        # 5 : [1,3,5,7,9,11,13,15]
        target = abs(target)
        now = 1
        ans = 0
        while target > 0:
            target -= now
            now += 1
            ans += 1
        if target % 2 == 0:  # 存在于比最大值小的同一步中
            return ans
        else:
            return ans + 1 + ans % 2  # 如果在奇数步，需要走两步；如果在偶数步，需要走一步


if __name__ == "__main__":
    print(Solution().reachNumber(-1))  # 1
    print(Solution().reachNumber(2))  # 3
    print(Solution().reachNumber(3))  # 2
    print(Solution().reachNumber(4))  # 3
    print(Solution().reachNumber(7))  # 5
    print(Solution().reachNumber(8))  # 4
