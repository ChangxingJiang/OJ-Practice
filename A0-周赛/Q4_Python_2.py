from typing import List


class Solution:
    def __init__(self):
        self.jobs = []
        self.ans = 0
        self.k = 0
        self.avg = 0

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        # 处理工人比工作多的情况
        if k >= len(jobs):
            return max(jobs)

        # 处理只有一个工人的情况
        if k == 1:
            return sum(jobs)

        jobs.sort(reverse=True)

        # 处理工人比工作少1个的情况：工人至少有2个，工作至少有3个
        if k > 1 and k == len(jobs) - 1:
            return max(jobs[0], self.minimumTimeRequired(jobs[-2:], 1))

        # 处理工人比工作少2个的情况：工人至少有2个，工作至少有4个
        if k > 2 and k == len(jobs) - 2:
            return max(jobs[0], self.minimumTimeRequired(jobs[-4:], 2))

        # 处理工人比工作少3个的情况：工人至少有3个，工作至少有6个
        if k > 3 and k == len(jobs) - 3:
            return max(jobs[0], self.minimumTimeRequired(jobs[-6:], 3))

        # 处理工人比工作少4个的情况：工人至少有4个，工作至少有8个
        if k > 4 and k == len(jobs) - 4:
            return max(jobs[0], self.minimumTimeRequired(jobs[-8:], 4))

        # 处理工人比工作少5个的情况：工人至少有5个，工作至少有10个
        if k > 5 and k == len(jobs) - 5:
            return max(jobs[0], self.minimumTimeRequired(jobs[-10:], 5))

        self.jobs = jobs
        self.ans = sum(jobs)
        self.k = k
        self.avg = sum(jobs) // k

        self.dfs(idx=0, people=[0] * k, max_val=0)

        return self.ans

    def dfs(self, idx, people, max_val):
        # 处理递归完成的情况
        if idx == len(self.jobs):
            self.ans = min(self.ans, max_val)
            return

        # 剪枝条件1:处理已经不会有更优解的情况
        if max_val >= self.ans:
            return

        for i in range(self.k):
            # 剪枝条件2:处理当前位置已经超出平均值，不适合继续放置的情况
            if people[i] <= self.avg:
                people[i] += self.jobs[idx]
                self.dfs(idx + 1, people, max(max_val, people[i]))
                people[i] -= self.jobs[idx]


if __name__ == "__main__":
    # 3
    print(Solution().minimumTimeRequired(jobs=[3, 2, 3], k=3))

    # 11
    print(Solution().minimumTimeRequired(jobs=[1, 2, 4, 7, 8], k=2))

    # 13
    print(Solution().minimumTimeRequired(jobs=[3, 4, 5, 6, 7], k=2))

    # 26
    print(Solution().minimumTimeRequired(jobs=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], k=3))

    # 20
    print(Solution().minimumTimeRequired(jobs=[11, 2, 20, 18, 2, 1, 7, 11, 7, 10], k=9))

    # 504
    print(Solution().minimumTimeRequired(jobs=[254, 256, 256, 254, 251, 256, 254, 253, 255, 251, 251, 255], k=10))

    # 504
    print(Solution().minimumTimeRequired(jobs=[256, 250, 255, 250, 254, 255, 260, 260, 250, 252, 257, 253], k=9))
