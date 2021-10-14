elevatorID = 1
floorRequestButtonID = 1
callButtonID = 1

class Column:
    def __init__(self, _id, _amountOfFloors, _amountOfElevators):
        self.ID = _id
        self.status = 'online'
        self.amountOfFloors = _amountOfFloors
        self.amountOfElevators = _amountOfElevators
        self.elevatorList = []
        self.callButtonList = []

        self.createCallButtons(_amountOfFloors)
        self.createElevators(_amountOfFloors, _amountOfElevators)

    def createCallButtons(self,_amountOfFloors):
        buttonFloor = 1

        for buttonFloor in _amountOfFloors:
            if (buttonFloor < _amountOfFloors):
                callButton = CallButton(callButtonID, "off", buttonFloor, "up")
                self.callButtonList.append(callButton)
                self.callButtonID += 1
            if (buttonFloor > 1):
                callButton = CallButton(callButtonID, "off", buttonFloor, "down")
                self.callButtonList.append(callButton)
                self.callButtonID += 1
        buttonFloor += 1

    def createElevators(self ,_amountOfFloors, _amountOfElevators):
        for elevator in _amountOfElevators:
            elevator = Elevator(elevatorID, _amountOfFloors)
            self.elevatorList.append(elevator)
            self.elevatorID += 1

    def requestElevator(self, floor , direction) :
        self.elevator = self.findElevator(floor,direction)
        self.floorRequestList.append(floor)
        elevator.move()
        elevator.operateDoors()

        return elevator

    def findElevator(self, requestedFloor, requestedDirection):

        # bestElevatorInformations = {
        # bestElevator: null,
        # bestScore: 5,
        # referenceGap: 10000000
        

        self.elevatorList.forEach(elevator

            if (requestedFloor == elevator.currentFloor && elevator.status == "stopped" && requestedDirection == elevator.direction)
                bestElevatorInformations = self.checkIfElevatorIsBetter(1, elevator, bestElevatorInformations, requestedFloor)

            elif (requestedFloor > elevator.currentFloor && elevator.direction == "up" && requestedDirection == elevator.direction) 
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)

            elif (requestedFloor < elevator.currentFloor && elevator.direction == "down" && requestedDirection == elevator.direction) 
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)

            elif (elevator.status == "idle")
                bestElevatorInformations = self.checkIfElevatorIsBetter(3, elevator, bestElevatorInformations, requestedFloor)

            else 
                bestElevatorInformations = self.checkIfElevatorIsBetter(4, elevator, bestElevatorInformations, requestedFloor)
            
        
        return bestElevatorInformations.bestElevator 
    


class Elevator:
    def __init__(self, _id, _amountOfFloors):


class CallButton:
    def __init__(self, _id, _floor, _direction):


class FloorRequestButton:
    def __init__(self, _id, _floor):


class Door:
    def __init__(self, _id):
