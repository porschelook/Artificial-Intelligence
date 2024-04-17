from environment import *


class threeBitAgent (Agent):
    def __init__(self):
        self.turnStep=0
        self.turnLeftFlag=0#0 for turn right 1 for turn left
        #turn step takes three values and turn direction takes 2 values indepndently. This requires six states which can be stored in three bits. 
    def stepProgram(self,environment):
        print(f"turn step {self.turnStep}")
        #if on a dirty square, clean
        if( not environment.getCurrentRoom().Isclean):
            environment.getCurrentRoom().Isclean=True
            environment.clean+=1
            return
        elif(self.turnStep==1 and self.turnLeftFlag==0):#turning after advancing happens regardless of if there is a wall ahead, so don't get stuck in the wrong mode by checking for a wall too early. 
            environment.turnRight()
            self.turnLeftFlag=1
            self.turnStep=0
            return      
        elif(self.turnStep==1 and self.turnLeftFlag==1):
            environment.turnLeft()
            self.turnLeftFlag=0
            self.turnStep=0
            return
        elif(environment.detectWall()):#when it arives at a wall, start a tragectory to move over a rank and turn around
            self.turnStep=2
            if self.turnLeftFlag==0:
                environment.turnRight()
            else:
                environment.turnLeft()
            return
        elif(self.turnStep==2):
            environment.advance()
            self.turnStep=1
            return        

        else:
            environment.advance()
        

         
    
 
