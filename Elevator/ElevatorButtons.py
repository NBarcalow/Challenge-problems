import time

''' 
    Evevator button class:
        initialization of the class
        addElevatorButton: add additional buttons to the list
        removeElevatorButton: removes a button from the list and for my benfit to see when stopped on a floor
        EvelvatorButtonList: return all buttons still within the list
'''

class ElevatorButtons:

    def __init__(self):
        self.buttonList = []
        
    def addElevatorButton(self, floor):
        if not (floor in self.buttonList):
            self.buttonList.append(floor)
            self.buttonList.sort()
            
    def removeElevatorButton(self, floor):
            self.buttonList.remove(floor)
            print('button stop on floor ', floor)
            ''' therortical wait time for passangers to disembark'''
            time.sleep(1)

    def elevatorButtonList(self):
        return self.buttonList
