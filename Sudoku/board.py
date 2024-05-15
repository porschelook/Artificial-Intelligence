import copy
class board:
    def __init__(self):
        self.cells = [[{1, 2, 3, 4, 5, 6, 7, 8, 9} for col in range(9)] for row in range(9)]
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
    
        try:
            self.emptyCells.remove((row,col))
        except:
            print("already assigned this element")
            return -1

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
        print("-------------------------------------")
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
        print("-------------------------------------")

    def copy(self):
        output = board()
        output.cells = copy.deepcopy(self.cells)
        
        output.emptyCells=copy.deepcopy(self.emptyCells)
        return output
    
    def mostConstrainedVariable(self):
        if len(self.emptyCells)==0:
            print("stopping")
            return 1,1
        min_domain_size = float('inf')
        for cell in self.emptyCells:
                cell_row, cell_col = cell
                domain_size = len(self.cells[cell_row][cell_col])
                if domain_size < min_domain_size:
                    min_domain_size = domain_size
                    row, col = cell
        return row, col
    def doNakedSingles(self): #yes I see the unfortunate wording
        #iterate through "empty" cells looking for those who have only one possible action left, then fill those in with the fill cell
        numberOfHits=0
        for row,col in self.emptyCells:
            values=self.cells[row][col]
            if len(values)==1:
                self.fillCell(row,col,list(values)[0])
                numberOfHits+=1
        return numberOfHits
    def doHiddenSingles(self):
        #iterate through "empty" cells looking for those who have unique actions
        numberOfHits=0
        for row,col in self.emptyCells:
            values=self.cells[row][col]

            #remove values present in the row
            for colIter in range(9):
                if colIter==col:
                        continue
                removeVals=self.cells[row][colIter]
                #actually do the removing
                for v in removeVals:
                    values.discard(v)
            
            #remove values present in the col
            for rowIter in range(9):
                if rowIter==row:
                    continue
                removeVals=self.cells[rowIter][col]
                #actually do the removing
                for v in removeVals:
                    values.discard(v)
            #remove from the box
            rowoffset = row // 3
            coloffset = col // 3
            for rowiter in range(3):
                for coliter in range(3):
                    rowtemp=rowoffset * 3 + rowiter
                    coltemp=coloffset * 3 + coliter
                    if rowtemp==row and coltemp==col:
                        continue
                
                    removeVals=self.cells[rowtemp][coltemp]
                    for v in removeVals:
                        values.discard(v)
            if len(values)==1:
                numberOfHits+=1
                self.fillCell(row,col,list(values)[0])
        return numberOfHits
    #TEST
    def backtrackSearch(self):
        if len(self.emptyCells) == 0:  # If the board is filled, we've found a solution
            return True
        #this does most constrained variable
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
        hits =self.doNakedSingles()
        if hits>0:
            return
        hits=self.doHiddenSingles()
        if hits>0:
            self.propogateConstraints()
            return
        #put the rest of the rules

# if __name__ == "__main__":
#     my_board = board()
#     print("forwardCheck ", my_board.forwardCheck())
#     my_board.buildBoard("testExample.txt")
#     my_board.printBoard()
#     # Fill your board with initial values (using buildBoard method)
#     # Then initiate the backtracking search from the first empty cell
#     solution_found = my_board.backtrackSearch()
#     if solution_found:
#         print("Solution found:")
#         my_board.printBoard()
#     else:
#         print("No solution found.")
