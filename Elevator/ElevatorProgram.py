import ElevatorObject
import ElevatorCalls

''' 
    Evevator Program:
        Features not added: 
            That was not added was an event class to handle dynamically added buttons and calls to the lists
            while the elevator is running. 
            I did not add this, because I'm less familiar with python events, however, this is something I would
            like to build on and learn more about.

        Assumptions:
            That the user will know the states of the elevator before calling changeElevatorState ( idle, up, down )

'''

def main():
    ElevatorCallList = ElevatorCalls.ElevatorCalls()
    Elevator1 = ElevatorObject.Elevator(ElevatorCallList)

    ElevatorCallList.addElevatorCall(4)
    Elevator1.buttons.addElevatorButton(3)
    ElevatorCallList.addElevatorCall(1)
    Elevator1.buttons.addElevatorButton(2)
    Elevator1.runElevator()

if __name__ == "__main__":
    main()