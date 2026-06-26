class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)
        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                if value in rows[i] or value in columns[j] or value in boxes[(i // 3, j // 3)]:
                    return False

                columns[j].add(value)
                rows[i].add(value)
                boxes[(i // 3, j // 3)].add(value)
        return True
