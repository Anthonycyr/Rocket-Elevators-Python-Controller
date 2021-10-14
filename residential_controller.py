# from test_residential_controller import FloorRequestButton


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

        for i in range(1,_amountOfFloors):
            if (i < _amountOfFloors):
                callButton = CallButton(callButtonID, "off", buttonFloor, "up")
                self.callButtonList.append(callButton)
                self.callButtonID += 1
            if (i > 1):
                callButton = CallButton(callButtonID, "off", buttonFloor, "down")
                self.callButtonList.append(callButton)
                self.callButtonID += 1
        buttonFloor += 1

    def createElevators(self ,_amountOfFloors, _amountOfElevators):
        for i in range(1, _amountOfElevators):
            elevator = Elevator(i, _amountOfFloors)
            self.elevatorList.append(elevator)
            self.elevatorID += 1

    def requestElevator(self, floor , direction) :
        self.elevator = self.findElevator(floor,direction)
        self.floorRequestList.append(floor)
        elevator.move()
        elevator.operateDoors()

        return elevator

    def findElevator(self, requestedFloor, requestedDirection):

        bestElevator: None
        bestScore: 5
        referenceGap: 10000000

        bestElevatorInformations = [bestElevator, bestScore, referenceGap]
        

        
        for elevator in self.elevatorList:

            if requestedFloor == elevator.currentFloor and elevator.status == "stopped" and requestedDirection == elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(1, elevator, bestElevatorInformations, requestedFloor)

            elif requestedFloor > elevator.currentFloor and elevator.direction == "up" and requestedDirection == elevator.direction: 
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)

            elif requestedFloor < elevator.currentFloor and elevator.direction == "down" and requestedDirection == elevator.direction: 
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator, bestElevatorInformations, requestedFloor)

            elif elevator.status == "idle":
                bestElevatorInformations = self.checkIfElevatorIsBetter(3, elevator, bestElevatorInformations, requestedFloor)

            else: 
                bestElevatorInformations = self.checkIfElevatorIsBetter(4, elevator, bestElevatorInformations, requestedFloor)
            
        
        return bestElevatorInformations.bestElevator 
    
    def checkIfElevatorIsBetter(self ,scoreToCheck, newElevator, bestElevatorInformations, requestedFloor) :   
        if scoreToCheck < bestElevatorInformations.bestScore : 
            bestElevatorInformations.bestScore = scoreToCheck
            bestElevatorInformations.bestElevator = newElevator
            bestElevatorInformations.referenceGap = abs(newElevator.currentFloor - requestedFloor)

        elif bestElevatorInformations.bestScore == scoreToCheck :
            gap = abs(newElevator.currentFloor - requestedFloor)
            if (bestElevatorInformations.referenceGap > gap) :
                bestElevatorInformations.bestScore = scoreToCheck 
                bestElevatorInformations.bestElevator = newElevator
                bestElevatorInformations.referenceGap = gap
            
        
        return bestElevatorInformations



class Elevator:
    def __init__(self, _id, _amountOfFloors):
        self.ID = _id
        self.status = 'idle'
        self.amountOfFloors = _amountOfFloors
        self.currentFloor = 1
        self.direction = None
        self.door = Door(_id, "closed")
        self.floorRequestButtonList = []
        self.floorRequestList = []

        self.createFloorRequestButtons(self.amountOfFloors)

    def createFloorRequestButtons(self,_amountOfFloors):
        buttonFloor = 1

        for x in _amountOfFloors :
            floorRequestButton = FloorRequestButton(floorRequestButtonID,"off",buttonFloor)
            self.floorRequestButtonList.append(floorRequestButton)
            buttonFloor += 1

    def requestFloor(self , floor):
        self.floorRequestList.append(floor)
        self.move()
        self.operateDoors()    

    def move(self):
        while (len(self.floorRequestList) > 0):
            destination = self.floorRequestList[0] 
            self.status = "moving"
            if (self.currentFloor < destination): 
                self.direction = "up"
                self.sortFloorList()
                while(self.currentFloor < destination): 
                    self.currentFloor += 1
                    self.screenDisplay = self.currentFloor
                
            elif (self.currentFloor > destination) :
                self.direction = "down" 
                self.sortFloorList()
                while(self.currentFloor > destination): 
                    self.currentFloor -=1
                    self.screenDisplay = self.currentFloor
                
            
            self.status = "stopped"
            self.floorRequestList.pop(0)
        
        self.status = "idself"
    def operateDoors(self):
        self.door.status = "opened"

        if(self != "overweight"):
            self.door.status = "closing"
            if(self != "obstructed"):
                self.door.status = "closed"
            else :
                self.operateDoors()
        else:
            while(self == "overweight"):
        
                self.operateDoors()

class CallButton:
    def __init__(self, _id, _floor, _direction):
        self.ID = _id
        # self.status = _status
        self.floor = _floor
        self.direction = _direction        


class FloorRequestButton:
    def __init__(self, _id, _floor):
        self.ID = _id
        self.floor = _floor


class Door:
    def __init__(self, _id):
        # self.status = _status
        self.ID = _id
