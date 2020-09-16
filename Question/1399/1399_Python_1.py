class Solution:
    def countLargestGroup(self, n: int) -> int:
        def helper(k):
            a = 0
            while k:
                a += k % 10
                k = k // 10
            return a

        hashmap = {}
        for i in range(1, n + 1):
            m = helper(i)
            if m in hashmap:
                hashmap[m] += 1
            else:
                hashmap[m] = 1

        maximum = max(hashmap.values())
        ans = 0
        for key, values in hashmap.items():
            if values == maximum:
                ans += 1
        return ans


if __name__ == "__main__":
    print(Solution().countLargestGroup(13))  # 4
    print(Solution().countLargestGroup(2))  # 2
    print(Solution().countLargestGroup(15))  # 6
    print(Solution().countLargestGroup(24))  # 5
