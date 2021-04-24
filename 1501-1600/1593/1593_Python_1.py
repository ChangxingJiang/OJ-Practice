class Solution:
    def __init__(self):
        self.max = 0

    def maxUniqueSplit(self, s: str) -> int:

        # @functools.lru_cache
        def recursor(ss: str, val, now):
            # print(ss, val, now)

            if not ss:
                self.max = max(self.max, val)
                return

            if ss not in now:
                self.max = max(self.max, val + 1)

            for i in range(1, len(ss)):
                if ss[:i] not in now:
                    now.add(ss[:i])
                    recursor(ss[i:], val + 1, now.copy())
                    now._remove(ss[:i])

        recursor(s, 0, set())

        return self.max


if __name__ == "__main__":
    print(Solution().maxUniqueSplit("ababccc"))  # 5
    print(Solution().maxUniqueSplit("acbabc"))  # 4
    print(Solution().maxUniqueSplit("aba"))  # 2
    print(Solution().maxUniqueSplit("aa"))  # 1
