import copy
class board:
    def __init__(self):
        self.cells = [[{1, 2, 3, 4, 5, 6, 7, 8, 9} for col in range(9)] for row in range(9)]
        self.toFill=81
        self.emptyCells=[(row,col) for col in range(9) for row in range(9)]
        #self.cells = [[{0} for col in range(9)] for row in range(9)]
    def fillCell(self, row, col, value):
        if value not in self.cells[row][col]:
            print("Attempt at invalid move of value "+ str(value))
            return -1 # decide how to handle this case later

     

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
        self.toFill-=1
        self.emptyCells.remove((row,col))

    #Do a forward error check and see if any cell has no valid values, False means that the current board is inconsistent
    def forwardCheck(self):
        for row in range(len(self.cells)):
            for col in range(len(self.cells[0])):
                value=self.cells[row][col]
                if len(value)==0:
                    print("forward check fails for cell "+ str(row) + "," +str(col))
                    return False
        return True
    #build the starting conditions from the textfile examples. Will require copy-pasting in some way to manage the fact that lots of them are in the same file. This takes in the name of a file to read in, and expects the file to just contain the board it is to build
    def buildBoard(self,instring):
        f=open(instring)
        numFilled=0
        for i in range(9):
            row=f.readline().replace(" ", "")
            for j in range(9):
                value=int(row[j])
                if value==0:
                    continue
                #print("placing value " +str(value))
                self.fillCell(i,j,value)
                numFilled+=1
        return numFilled
    
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
        output.cells = copy.deepcopy(self.cells)
        output.toFill=self.toFill
        output.emptyCells=copy.deepcopy(self.emptyCells)
        return output
    
    #TEST
    def backtrackSearch(self):
        if self.toFill == 0:  # If the board is filled, we've found a solution
            return True

        row, col = self.emptyCells[0]

        if self.emptyCells and self.toFill > 1:
            min_domain_size = float('inf')
            for cell in self.emptyCells:
                cell_row, cell_col = cell
                domain_size = len(self.cells[cell_row][cell_col])
                if domain_size < min_domain_size:
                    min_domain_size = domain_size
                    row, col = cell

        for value in self.cells[row][col]:
            new_board = self.copy()

            print()
            self.printBoard()
            

            new_board.fillCell(row, col, value)
            new_board.propagateConstraints()
            if new_board.forwardCheck():
                if new_board.backtrackSearch():
                    self.cells = new_board.cells
                    return True

        return False

    def propagateConstraints(self):
        # Perform constraint propagation through domain-specific inference rules
        # Implement the inference rules here
        pass

if __name__ == "__main__":
    my_board = board()
    print("forwardCheck ", my_board.forwardCheck())
    my_board.buildBoard("testExample.txt")
    my_board.printBoard()
    # Fill your board with initial values (using buildBoard method)
    # Then initiate the backtracking search from the first empty cell
    solution_found = my_board.backtrackSearch()
    if solution_found:
        print("Solution found:")
        my_board.printBoard()
    else:
        print("No solution found.")
