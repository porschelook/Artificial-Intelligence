from board import *
import time
if __name__ == "__main__":
     
    b = state()
    b.scramble(50)


    for m in  [10,20,30,40,50]:
        totalTime=0
        totalLength=0
        
        totalTime_aStar=0
        heuristicTime_aStar=0
        totalExpand_aStar=0
        totalLength_aStar=0
        for i in range(10):
            b=state()
            b.scramble(m)
            #print("shuffle borad \n", b.board)
            tic=time.perf_counter() 
            initial_node = Node(b, 0, b.manh_dist())

            goal_node, _ = rbfs(initial_node, np.inf)
            p=goal_node
            while p.state != b:
                totalLength+=1
                p=p.parent
        
        
            toc=time.perf_counter()
            totalTime+=toc-tic
            
            tic_aStar=time.perf_counter() 
            g,expanded,heurist=aStar(b,"Other")
            p=g
            while p.state != b:
                totalLength_aStar+=1
                p=p.parent
                
            toc_aStar=time.perf_counter()
            totalTime_aStar+=toc_aStar-tic_aStar
            totalExpand_aStar+=expanded
            heuristicTime_aStar+=heurist
        print("Average time to solve with A-star: " + str(totalTime_aStar/10))
        print("Average time to solve heuristic with A-star: " + str(heuristicTime_aStar/10))
        print("Average nodes to solve with A-star: " + str(totalExpand_aStar/10))
        print("Average length of A-star solution: " + str(totalLength_aStar/10))
        print("Average time to solve with RBFS: " + str(totalTime/10))
        print("Average length of RBFS solution: " + str(totalLength/10))
        print("------------------------------------")
    #print(g.state.board)
    
