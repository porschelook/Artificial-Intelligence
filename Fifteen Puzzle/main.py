from board import *
import time
if __name__ == "__main__":
    initial_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 0, 14, 15]] #
    b = state()
    b.scramble(50)
    print( b.board)

    print("main ", b.emptyLoc)

    for m in  [10,20,30,40,50]:
        totalTime=0
        for i in range(10):
            b=state()
            b.scramble(m)
            tic=time.perf_counter() 
            g=aStar(b)
            toc=time.perf_counter()
            totalTime+=toc-tic
        print("Average time to solve with A-star: " + str(totalTime/10))
   
    print(g.state.board)
    
