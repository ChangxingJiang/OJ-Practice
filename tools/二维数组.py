m, n = len(grid), len(grid[0])


def _is_valid(x, y):
    return 0 <= x < m and 0 <= y < n


def _get_neighbors(x1, y1):
    return [(x2, y2) for (x2, y2) in [(x1 - 1, y1), (x1 + 1, y1), (x1, y1 - 1), (x1, y1 + 1)]
            if _is_valid(x2, y2)]
