from board import *
import time
if __name__ == "__main__":
     
    b = state()
    b.scramble(50)


    for m in  [10,20,30,40,50]:
        totalTime=0
        totalTime_aStar=0
        for i in range(50):
            b=state()
            b.scramble(m)
            #print("shuffle borad \n", b.board)
            tic=time.perf_counter() 
            initial_node = Node(b, 0, b.manh_dist())

            goal_node, _ = rbfs(initial_node, np.inf)

            #g=aStar(b)
            toc=time.perf_counter()
            totalTime+=toc-tic
            
            tic_aStar=time.perf_counter() 
            g=aStar(b)
            toc_aStar=time.perf_counter()
            totalTime_aStar+=toc_aStar-tic_aStar

        print("Average time to solve with A-star: " + str(totalTime_aStar/10))
        print("Average time to solve with RBFS: " + str(totalTime/10))
        print("------------------------------------")
    #print(g.state.board)
    
