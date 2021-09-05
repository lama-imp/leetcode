"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.
You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].
To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.
Return the modified image after performing the flood fill.
"""


def floodFill(image, sr, sc, newColor):
    """
    :type image: List[List[int]]
    :type sr: int
    :type sc: int
    :type newColor: int
    :rtype: List[List[int]]
    """
    m = len(image) - 1
    n = len(image[0]) - 1

    def check_index(c1, c2, m, n):
        if c1 < 0 or c2 < 0:
            return False
        elif c1 > m or c2 > n:
            return False
        else:
            return True

    color = image[sr][sc]

    if color == newColor:
        return image

    def foo(r, c, color, newColor):
        image[r][c] = newColor
        if check_index(r - 1, c, m, n) and image[r - 1][c] == color:
            foo(r - 1, c, color, newColor)
        if check_index(r + 1, c, m, n) and image[r + 1][c] == color:
            foo(r + 1, c, color, newColor)
        if check_index(r, c - 1, m, n) and image[r][c - 1] == color:
            foo(r, c - 1, color, newColor)
        if check_index(r, c + 1, m, n) and image[r][c + 1] == color:
            foo(r, c + 1, color, newColor)

    foo(sr, sc, color, newColor)
    return image
