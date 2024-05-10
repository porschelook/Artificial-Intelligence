class board:
    def __init__(self):
        self.cells=[[{1 ,2,3,4,5,6,7,8,9} for col in range(9)] for row in range(9)]

    def fillCell(self, row,col,value):
        if value not in self.cells[row][col]:
            print("attempt at invalid move")
            return#decide how to handles this case later
        
        self.cells[row][col]={value} #make the assignment
        #eliminate the value from other applicapble cells

        #eliminate from each element in same row
        for itercol in range(9):
            if itercol == col:
                continue
            self.cells[row][itercol].discard(value )

        #eliminate from each element in same column
        for iterrow in range(9):
            if iterrow == row:
                continue
            self.cells[iterrow][col].discard(value)

        #eliminate the value from each element in the box
        rowoffset=row//3
        coloffset=col//3
        for rowiter in range(3):
            for coliter in range(3):
                self.cells[rowoffset+rowiter][coloffset+coliter].discard(value)
    def printBoard(self):
        for i in range(9):
            print(self.cells[i]," ",end="")
            print()
             
 

    
