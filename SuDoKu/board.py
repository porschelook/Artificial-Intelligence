class board:
    def __init__(self):
        self.cells = [[{1, 2, 3, 4, 5, 6, 7, 8, 9} for col in range(9)] for row in range(9)]

    def fillCell(self, row, col, value):
        if value not in self.cells[row][col]:
            print("Attempt at invalid move")
            return  # decide how to handle this case later

        self.cells[row][col] = {value}  # make the assignment

        # eliminate the value from other applicable cells

        # eliminate from each element in same row
        for itercol in range(9):
            if itercol == col:
                continue
            self.cells[row][itercol].discard(value)

        # eliminate from each element in same column
        for iterrow in range(9):
            if iterrow == row:
                continue
            self.cells[iterrow][col].discard(value)

        # eliminate the value from each element in the box
        rowoffset = row // 3
        coloffset = col // 3
        for rowiter in range(3):
            for coliter in range(3):
                self.cells[rowoffset * 3 + rowiter][coloffset * 3 + coliter].discard(value)

    def printBoard(self):
        for row in range(9):
            if row % 3 == 0 and row != 0:
                print("-" * 21)
            for col in range(9):
                if col % 3 == 0 and col != 0:
                    print("|", end=" ")
                value = self.cells[row][col]
                if len(value) == 1:
                    print(list(value)[0], end=" ")
                else:
                    print(".", end=" ")
            print()
