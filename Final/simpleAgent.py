from environment import *
class Agent:
    def clean(self,env):
       env.getCurrentRoom().Isclean=True
       env.clean+=1
       return
    def stepProgram(self,environment):
        return


class SimpleAgent(Agent):
    def stepProgram(self,environment):

        #first, if the room is dirty, clean it
        if(not environment.getCurrentRoom().Isclean):
            environment.getCurrentRoom().Isclean=True
            environment.clean+=1
            return
        #Next, if the way forward is clear, move forward
        if(not environment.detectWall()):
            print(not environment.detectWall())
            environment.advance()
            return
        #If the way is blocked, turn right
        environment.turnRight()
    
 
