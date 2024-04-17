from environment import *
NO_WALL = 0
WALL = 1

class Agent:
    def stepProgram(self,environment):
        return


class lowmemoryAgent (Agent):
    alreadyClean_x = []
    alreadyClean_y = []
        

    def stepProgram(self,environment):
        if environment.Iswall == WALL:

            
            #first, if the room is dirty, clean it
            if(not environment.getCurrentRoom().Isclean):
                environment.getCurrentRoom().Isclean=True
                self.alreadyClean_x.append(environment.current_x)
                self.alreadyClean_y.append(environment.current_y)
                print(self.alreadyClean_x)
                print(self.alreadyClean_y)
                return
            
            if not environment.detectNextClean_mem() :
                environment.turnRight()
                return
            #Next, if the way forward is clear, move forward
            if(not environment.detectWall()):
                environment.advance()
                return
            
            #If the way is blocked, turn right
            environment.turnRight()


         
    
 