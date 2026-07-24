class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for row in range(9):
            for col in range(9):

                if board[row][col] == ".":
                    empty.append((row, col))
                
                else:
                    ch = board[row][col]

                    rows[row].add(ch)
                    cols[col].add(ch)

                    box = (row // 3) * 3 + (col // 3)
                    boxes[box].add(ch)

        def solve(index):

            if index == len(empty):
                return True

            row, col = empty[index]
            box = (row // 3) * 3 + (col // 3)

            for num in range(1,10):

                ch = str(num)

                if (
                    ch not in rows[row] and
                    ch not in cols[col] and
                    ch not in boxes[box]
                ):
                    board[row][col] = ch

                    rows[row].add(ch)
                    cols[col].add(ch)
                    boxes[box].add(ch)

                    if solve(index + 1):
                        return True

                    board[row][col] = "."

                    rows[row].remove(ch)
                    cols[col].remove(ch)
                    boxes[box].remove(ch)
                
            return False
        return solve(0)