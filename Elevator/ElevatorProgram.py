import ElevatorObject
import ElevatorCalls



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
