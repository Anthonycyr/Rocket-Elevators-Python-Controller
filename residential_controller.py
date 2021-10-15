# from test_residential_controller import FloorRequestButton


elevatorID =  1 
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
        global callButtonID
        buttonFloor = 1

        for i in range(_amountOfFloors):
            if (i < _amountOfFloors):
                callButton = CallButton(callButtonID, buttonFloor, "up")#"up"
                self.callButtonList.append(callButton)
                callButtonID += 1
            if (i > 1):
                callButton = CallButton(callButtonID, buttonFloor, "down")#"down"
                self.callButtonList.append(callButton)
                callButtonID += 1
        buttonFloor += 1

    def createElevators(self ,_amountOfFloors, _amountOfElevators):
        global elevatorID
        for i in range( _amountOfElevators):
            elevator = Elevator(i, _amountOfFloors)
            self.elevatorList.append(elevator)
            elevatorID += 1

    def requestElevator(self, floor , direction) :
        elevator = self.findElevator(floor,direction)
        elevator.floorRequestList.append(floor)
        elevator.move()
        elevator.operateDoors()

        return elevator

    def findElevator(self, requestedFloor, requestedDirection):

        bestScore = 5
        referenceGap = 10000000
        bestElevator = None
        bestElevatorInformations = None

        
        
        for elevator in self.elevatorList:

            if requestedFloor == elevator.currentFloor and elevator.status == "stopped" and requestedDirection == elevator.direction:
                bestElevatorInformations = self.checkIfElevatorIsBetter(1, elevator,  bestElevator ,bestScore , referenceGap , requestedFloor)

            elif requestedFloor > elevator.currentFloor and elevator.direction == "up" and requestedDirection == elevator.direction: 
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator,  bestElevator ,bestScore , referenceGap , requestedFloor)

            elif requestedFloor < elevator.currentFloor and elevator.direction == "down" and requestedDirection == elevator.direction: 
                bestElevatorInformations = self.checkIfElevatorIsBetter(2, elevator,  bestElevator ,bestScore , referenceGap , requestedFloor)

            elif elevator.status == "idle":
                bestElevatorInformations = self.checkIfElevatorIsBetter(3, elevator,  bestElevator ,bestScore , referenceGap , requestedFloor)

            else: 
                bestElevatorInformations = self.checkIfElevatorIsBetter(4, elevator, bestElevator ,bestScore , referenceGap , requestedFloor)
            
        
        return bestElevatorInformations["bestElevator"]
    
    def checkIfElevatorIsBetter(self ,scoreToCheck, newElevator,  bestElevator ,bestScore , referenceGap , requestedFloor) :   
        if scoreToCheck < bestScore : 
            bestScore = scoreToCheck
            bestElevator = newElevator
            referenceGap = abs(newElevator.currentFloor - requestedFloor)

        elif bestScore == scoreToCheck :
            gap = abs(newElevator.currentFloor - requestedFloor)
            if (referenceGap > gap) :
                bestScore = scoreToCheck 
                bestElevator = newElevator
                referenceGap = gap
        
        bestElevatorInformations = {
            "bestElevator" : bestElevator ,
            "bestScore" : bestScore,
            "referenceGap" : referenceGap
            }    
        
        return bestElevatorInformations



class Elevator:
    def __init__(self, _id, _amountOfFloors):
        self.ID = _id
        self.status = 'idle'
        self.amountOfFloors = _amountOfFloors
        self.currentFloor = 1
        self.direction = None
        self.door = Door(_id)
        self.floorRequestButtonList = []
        self.floorRequestList = []

        self.createFloorRequestButtons(self.amountOfFloors)

    def createFloorRequestButtons(self,_amountOfFloors):
        global floorRequestButtonID
        buttonFloor = 1

        for i in range(_amountOfFloors):
            floorRequestButton = FloorRequestButton(floorRequestButtonID, i) #"off"
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

    def sortFloorList(self) :
        if self.status == "up" :
            self.floorRequestList.sort()
        else :
            self.floorRequestList.sort()
        

    
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
    def __init__(self, _id, _floor, _direction ):
        self.ID = _id
        #self.status = None
        self.floor = _floor
        self.direction = _direction        


class FloorRequestButton:
    def __init__(self, _id, _floor):
        self.ID = _id
        #self.status = None
        self.floor = _floor


class Door:
    def __init__(self, _id):
        self.status = None
        self.ID = _id


# def scenario1():
#     column = Column(1, "online", 10, 2)
#     column.elevatorsList[0].currentFloor = 2
#     column.elevatorsList[1].currentFloor = 6
#     elevator = column.requestElevator(3, "up")
#     elevator.requestFloor(7)