import bisect


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        lst = [int(ch) for ch in str(n)]
        now = []
        for i in range(len(lst) - 1, -1, -1):
            n = lst[i]
            if not now or now[-1] <= n:
                bisect.insort_left(now, n)
            else:
                this = now.pop(bisect.bisect_right(now, n))
                bisect.insort_left(now, n)
                ans = lst[:i] + [this] + now
                ans = int("".join([str(v) for v in ans]))
                return ans if ans < 2 ** 31 else -1
        return -1


if __name__ == "__main__":
    print(Solution().nextGreaterElement(12))  # 21
    print(Solution().nextGreaterElement(21))  # -1
    print(Solution().nextGreaterElement(230241))  # 230412
    print(Solution().nextGreaterElement(12443322))  # 13222344
    print(Solution().nextGreaterElement(12222333))  # 12223233
