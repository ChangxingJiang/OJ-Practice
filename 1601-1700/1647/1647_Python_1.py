import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        count = collections.Counter(s)
        num_list = list(sorted(count.values(), reverse=True))

        ans = 0

        now = num_list[0]
        for i in range(1, len(num_list)):
            if num_list[i] >= now:
                if now > 0:
                    ans += (num_list[i] - (now - 1))
                    now -= 1
                else:
                    ans += num_list[i]
            else:
                now = num_list[i]

        return ans


if __name__ == "__main__":
    print(Solution().minDeletions("aab"))  # 0
    print(Solution().minDeletions("aaabbbcc"))  # 2
    print(Solution().minDeletions("ceabaacb"))  # 2
