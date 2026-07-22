class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]

        cols = set()
        diag1 = set()
        diag2 = set()

        ans = []
        
        def solve(row):

            if row == n:
                temp = ["".join(r) for r in board]
                ans.append(temp)
                return

            for col in range(n):

                if (
                    col in cols or
                    row - col in diag1 or
                    row + col in diag2
                ):
                    continue
                
                board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                solve(row + 1)

                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
        solve(0)

        return ans