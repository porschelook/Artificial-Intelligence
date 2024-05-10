class board:
    def __init__(self):
        self.cells = [[{1, 2, 3, 4, 5, 6, 7, 8, 9} for col in range(9)] for row in range(9)]

    def fillCell(self, row, col, value):
        if value not in self.cells[row][col]:
            print("Attempt at invalid move of value "+ str(value))
            return  # decide how to handle this case later

     

        # eliminate the value from other applicable cells

        # eliminate from each element in same row
        for itercol in range(9):
            self.cells[row][itercol].discard(value)

        # eliminate from each element in same column
        for iterrow in range(9):
            self.cells[iterrow][col].discard(value)

        # eliminate the value from each element in the box
        rowoffset = row // 3
        coloffset = col // 3
        for rowiter in range(3):
            for coliter in range(3):
                self.cells[rowoffset * 3 + rowiter][coloffset * 3 + coliter].discard(value)

        self.cells[row][col] = {value}  # make the assignment last, so it can be removed earlier just fine

    #Do a forward error check and see if any cell has no valid values, False means that the current board is inconsistent
    def forwardCheck(self):
        for col in self.cells:
            for value in col:
                if len(value)==0:
                    return False
        return True
    #build the starting conditions from the textfile examples. Will require copy-pasting in some way to manage the fact that lots of them are in the same file. This takes in the name of a file to read in, and expects the file to just contain the board it is to build
    def buildBoard(self,instring):
        f=open(instring)
        for i in range(9):
            row=f.readline().replace(" ", "")
            for j in range(9):
                value=int(row[j])
                if value==0:
                    continue
                #print("placing value " +str(value))
                self.fillCell(i,j,value)
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
    def copy(self):
        output = board()
        output.cells = [[moveset for moveset in col] for col in self.cells]
        return output
