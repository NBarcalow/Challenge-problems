import ElevatorButtons
import heapq

''' 
    Evevator object class:
        initialization of the class: needs a call list
        runElevator: * First checks if lists are still populated and loops through them
                     * Then checks elevator state idle, up, down
                     * Idle - finds nearest floor to move towards.
                     * Up - cycles through the lists increasingly making stops on all floors called/buttons
                     * Down - cycles through the lists decreasingly making stops on all floors called/buttons
                     * when the lists are empty is places the elevator back into idle
        elevatorDownCycle: loops through the lists and checks that anything in the lists below the current floor are stopped at while moving down
        elevatorUpCycle: loops through the lists and checks that anything in the lists above the current floor are stopped at while moving up
        elevatorUp: moves the elevator floor up one
        elevatorDown: moves the elevator floor down one
        changeElevatorState: changes the elevators state to idle, up, down
'''

class Elevator:
    def __init__(self, callList):
        self.floor = 0
        self.buttons = ElevatorButtons.ElevatorButtons()
        self.state = 'idle'
        self.callList = callList
    
    def runElevator(self):
        while (self.buttons.elevatorButtonList() or self.callList.elevatorCallList()):
            if (self.state == 'idle'):
                    if(self.callList.elevatorCallList()):
                        targetFloor = heapq.nsmallest(1, self.callList.elevatorCallList(), key=lambda x: abs(x-self.floor))[0]

                    else:
                        targetFloor = heapq.nsmallest(1, self.buttons.elevatorButtonList(), key=lambda x: abs(x-self.floor))[0]

                    if(targetFloor >= self.floor):
                        self.changeElevatorState('up')
                        self.elevatorUpCycle()
                        

                    else:
                        self.changeElevatorState('down')
                        self.elevatorDownCycle()
                        

            elif(self.state == 'up' and (self.buttons.elevatorButtonList() or self.callList.elevatorCallList())):
                if((self.floor > any(self.buttons.elevatorButtonList())) or (self.floor > any(self.callList.elevatorCallList()))):
                    while(self.buttons.elevatorButtonList() or self.callList.elevatorCallList()):
                        if(self.floor > self.buttons.elevatorButtonList()[len(self.buttons.elevatorButtonList()) - 1] 
                           or self.floor > self.callList.elevatorCallList()[len(self.callList.elevatorCallList()) - 1]):
                            self.changeElevatorState('down')
                            self.elevatorDownCycle()
                        else:
                            self.elevatorUpCycle()
                else:
                    self.changeElevatorState('down')

            elif(self.state == 'down' and (self.buttons.elevatorButtonList() or self.callList.elevatorCallList())):
                if(self.floor < any(self.buttons.elevatorButtonList()) or self.floor < any(self.callList.elevatorCallList())):
                    while(self.buttons.elevatorButtonList() or self.callList.elevatorCallList()):
                        if(self.floor < any(self.buttons.elevatorButtonList()) or self.floor < any(self.callList.elevatorCallList())):
                            self.changeElevatorState('up')
                            self.elevatorUpCycle()
                        else:
                            self.elevatorDownCycle()
                else:
                    self.changeElevatorState('up')
                
        self.changeElevatorState('idle')


    def elevatorDownCycle(self):
        while((self.buttons.elevatorButtonList() and self.buttons.elevatorButtonList()[0] <= self.floor) 
              or (self.callList.elevatorCallList() and self.callList.elevatorCallList()[0] <=  self.floor)):
            if(self.floor in self.callList.elevatorCallList()):
                self.callList.removeElevatorCall(self.floor)
            if(self.floor in self.buttons.elevatorButtonList()):
                self.buttons.removeElevatorButton(self.floor)
            self.elevatorDown()

    def elevatorUpCycle(self):
        while((self.buttons.elevatorButtonList() and self.buttons.elevatorButtonList()[len(self.buttons.elevatorButtonList()) - 1] >= self.floor) 
              or (self.callList.elevatorCallList() and self.callList.elevatorCallList()[len(self.callList.elevatorCallList()) - 1] >=  self.floor)):
            if(self.floor in self.callList.elevatorCallList()):
                self.callList.removeElevatorCall(self.floor)
            if(self.floor in self.buttons.elevatorButtonList()):
                self.buttons.removeElevatorButton(self.floor)
            self.elevatorUp()

    def elevatorUp(self):
        self.floor = self.floor + 1

    def elevatorDown(self):
        self.floor = self.floor - 1
    
    '''assumption here is that all states are known to the caller ( idle, up, down )'''
    def changeElevatorState(self, state):
        self.state = state