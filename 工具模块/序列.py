# 组合
from scipy.special import comb

comb(3, 2)  # C23


# 枚举所有可能的组合
def enumeration(nums):
    size = len(nums)
    ans = [0 for _ in range(1 << size)]  # 2**n种可能
    for i in range(size):
        for j in range(1 << i):
            ans[(1 << i) + j] = nums[i] + ans[j]
    return ans


# ---------- 生成所有不同的全排列(0047题) ----------
def permuteUnique(nums):
    visited = set()
    ans = []
    now = []

    n = len(nums)

    def track_back():
        if len(now) == n:
            ans.append(now[:])
        tmp_set = set()
        for i in range(n):
            if i not in visited:
                if nums[i] in tmp_set:
                    continue
                tmp_set.add(nums[i])

                visited.add(i)
                now.append(nums[i])
                track_back()
                now.pop()
                visited.remove(i)

    track_back()

    return ans
