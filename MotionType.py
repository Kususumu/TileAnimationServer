# MovingType is type of class that contain the motion database
# usage: use it to search the key information for motion and store the outer motion


class MovingType:
    motionName = 'motionType'
    posDirection = [0, 0, -1]
    distance = 1
    frameNum = 0
    texture = 0
    path = 0
    adjustDirection = 0

    def __init__(self):
        self.motionName = 'None'

    def setWalk(self):
        self.motionName = 'walk'
        self.posDirection = [0,0,+1]
        self.distance = 1
        self.frameNum = 24
        self.adjustDirection = 90
        self.path = 'E:/mayaStore/model/ModelWeUse/scenes/walk0024.mb'

    def setTurn(self):
        self.motionName = 'turn'
        self.posDirection = [0,0,+1]
        self.distance = 1
        self.frameNum = 24
        self.adjustDirection = 90
        self.path = 'E:/mayaStore/model/ModelWeUse/scenes/walk0024.mb'

    def setSit(self):
        self.motionName = 'sit'
        self.posDirection = [0,0,+1]
        self.distance = 1
        self.frameNum = 24
        self.adjustDirection = 90
        self.path = 'E:/mayaStore/model/ModelWeUse/scenes/sit0024.mb'

    def getFrameByName(self,typeName):
        # This place go in dataBase to search
        if typeName == 'walk':
            self.setWalk()
            return self.frameNum
        if typeName == 'sit':
            self.setSit()
            return self.frameNum
        if typeName == 'turn' :
            self.setTurn()
            return self.frameNum

    def getPathByName(self,typeName):
        #This place go in dataBase to search
        if typeName == 'walk':
            self.setWalk()
            return self.path
        if typeName == 'sit':
            self.setSit()
            return self.path
        if typeName == 'turn' :
            self.setTurn()
            return self.path

    def getAdjustByName(self,typeName):
        # This place go in dataBase to search
        if typeName == 'walk':
            self.setWalk()
            return self.adjustDirection
        if typeName == 'sit':
            self.setSit()
            return self.adjustDirection
        if typeName == 'turn':
            self.setTurn()
            return self.adjustDirection
