# m, n = len(grid), len(grid[0])

m, n = 0, 0


def _is_valid(x, y):
    return 0 <= x < m and 0 <= y < n


def _is_border(x, y):
    return x == 0 or x == m - 1 or y == 0 or y == n - 1


# 四个方向传递
def _get_neighbors(x1, y1):
    return [(x2, y2) for (x2, y2) in [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
            if _is_valid(x2, y2)]


# 八个方向传递
def _get_neighbors(x1, y1):
    return [(x2, y2) for (x2, y2) in [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1),
                                      (x1 - 1, y1 - 1), (x1 + 1, y1 + 1), (x1 + 1, y1 - 1), (x1 - 1, y1 + 1)]
            if _is_valid(x2, y2)]


# m, n = len(matrix), len(matrix[0])

# 计算前缀和
prefix = [[0] * (n + 1) for _ in range(m + 1)]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1] + matrix[i - 1][j - 1]


# 计算范围内的和
def count(x1, y1, x2, y2):
    return prefix[x2][y2] - prefix[x1 - 1][y2] - prefix[x2][y1 - 1] + prefix[x1 - 1][y1 - 1]


m, n = len(grid), len(grid[0])

# 对角线遍历（左上-右下）
for d in range(-m + 1, n):
    if d < 0:
        i0, j0, num = -d, 0, min(m + d, n)
    else:
        i0, j0, num = 0, d, min(n - d, m)

    lst = []
    for k in range(num):
        i1, j1 = i0 + k, j0 + k
        pass

# 对角线遍历（左下-右上）
for d in range(n + m - 1):
    if d < m:
        i0, j0, num = d, 0, min(d + 1, n)
    else:
        i0, j0, num = m - 1, d - m + 1, min(n + m - 1 - d, m)

    lst = []
    for k in range(num):
        i1, j1 = i0 - k, j0 + k
        pass
