import time

''' 
    Evevator call class:
        initialization of the class
        addElevatorCall: add additional call to the list
        removeElevatorCall: removes a call from the list and for my benfit to see when stopped on a floor
        EvelvatorCallList: return all calls still within the list
'''
''' 
    Call class is separate from the elevator object because
    there could be more than one elevator and all would need
    access to the same list
'''
class ElevatorCalls:
    
    def __init__(self):
        self.callList = []

    def addElevatorCall(self, floor):
        self.callList.append(floor)
        self.callList.sort()


    def removeElevatorCall(self, floor):
        self.callList.remove(floor)
        print('call stop on floor ', floor)
        ''' therortical wait time for passangers to disembark'''
        time.sleep(1)
                
    def elevatorCallList(self):
        return self.callList
