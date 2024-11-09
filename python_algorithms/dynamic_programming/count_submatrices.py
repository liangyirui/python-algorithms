"""
Given a 2D character matrix grid, where grid[i][j] is either 'X', 'Y', or '.', return the number of submatrices that contains:
1. grid[0][0]
2. an equal frequency of 'X' and 'Y'
3. at least one 'X'
"""


def number_of_submatrices(grid: list[list[str]]) -> int:
    m, n = len(grid), len(grid[0])
    dp = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j][0] = (
                dp[i - 1][j][0]
                + dp[i][j - 1][0]
                - dp[i - 1][j - 1][0]
                + (grid[i - 1][j - 1] == "X")
            )
            dp[i][j][1] = (
                dp[i - 1][j][1]
                + dp[i][j - 1][1]
                - dp[i - 1][j - 1][1]
                + (grid[i - 1][j - 1] == "Y")
            )
    count = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            x_count, y_count = dp[i][j]
            if x_count > 0 and x_count == y_count:
                count += 1
    return count


if __name__ == "__main__":
    grid = [["X", "Y", "."], ["Y", ".", "."]]
    print(number_of_submatrices(grid))
