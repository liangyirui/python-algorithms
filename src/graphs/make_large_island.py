"""
You are given an m * n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.
"""

def largest_island(grid: list[list[int]]) -> int:
    m, n = len(grid), len(grid[0])
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    areas = {}
    curr_color = 2
    max_area = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] != 1:
                continue
            areas[curr_color] = dfs(grid, r, c, curr_color, dirs)
            max_area = max(max_area, areas[curr_color])
            curr_color += 1
    
    for r in range(m):
        for c in range(n):
            if grid[r][c] != 0:
                continue
            colors = set()
            for dir in dirs:
                nr, nc = r + dir[0], c + dir[1]
                if not in_range(grid, nr, nc):
                    continue
                colors.add(grid[nr][nc])
            size = 1
            for color in colors:
                size += areas[color]
            max_area = max(max_area, size)
    
    return max_area



def dfs(grid: list[list[int]], row: int, col: int, color: int, dirs: list[int]) -> int:
    if not in_range(grid, row, col) or grid[row][col] != 1:
        return 0
    grid[row][col] = color
    area = 1
    for dir in dirs:
        area += dfs(grid, row + dir[0], col + dir[1], color, dirs)
    return area


def in_range(grid: list[list[int]], row: int, col: int):
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])



if __name__ == "__main__":
    grid1 = [[1, 0], [0, 1]]
    print(f"{grid1} The area of the largest island we can get by changing one 0 to 1 is {largest_island(grid1)}")
    grid2 = [[1, 1], [1, 0]]
    print(f"{grid2} The area of the largest island we can get by changing one 0 to 1 is {largest_island(grid2)}")
    grid3 = [[1, 1], [1, 1]]
    print(f"{grid3} The area of the largest island we can get by changing one 0 to 1 is {largest_island(grid3)}")