from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        h = len(image)
        w = len(image[0])

        old_color = image[sr][sc]

        if old_color == newColor:
            return image

        def change(r, c):
            if image[r][c] == old_color:
                image[r][c] = newColor
                if r > 0:
                    change(r - 1, c)
                if c > 0:
                    change(r, c - 1)
                if r < h - 1:
                    change(r + 1, c)
                if c < w - 1:
                    change(r, c + 1)

        change(sr, sc)

        return image


if __name__ == "__main__":
    # [[2,2,2],[2,2,0],[2,0,1]]
    print(Solution().floodFill(image=[[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2))
