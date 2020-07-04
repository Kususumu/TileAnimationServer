# The Class TimeSolver is the main class of the Server Side Render

import math
import MotionType
import Debugger

class TimeSolver:
    # First 4 TimeLine Value
    timeLineName = [0,0,0]
    timeLineDirection = [0,0,0]
    timeLineCoordinate = [0,0,0]
    timeLineTotalFrame = [0,0,0]
    timeLineEachFrame = [0,0,0]

    xLength = 400.0
    zLength = 400.0
    xNum = 6
    zNum = 6

    # floorCenterX = 30
    floorCenterX = 0.0
    floorCenterZ = 0.0
    initialX = 0.0
    initialZ = 0.0

    # Initial a motiontype for use to recognize the type of Motion
    motionType = MotionType.MovingType()

    def __init__(self):
        self.timeLineName.clear()
        self.timeLineDirection.clear()
        self.timeLineCoordinate.clear()
        self.timeLineTotalFrame.clear()
        self.timeLineEachFrame.clear()

    def sendTimeLine(self):
        return 0

    '''Get the Time Line direction use the input of the ClickIndex&ClickMotion'''
    '''Return the Solved Time Line'''
    def getTimeLine(self,cIndex,cMotion):
        # Initial the Value

        self.initialTimeLine(cIndex,cMotion)

        # After Init we detect turning
        #self.detectTurning(self.timeLineDirection)

        #Debugger.showList(cMotion, "cMotion")
        #Debugger.showList(cIndex, "CIndex")


        # A function to add the end Time
        self.addEndTime(cIndex,cMotion)

        Debugger.showList(self.timeLineName, "TimeLineName")
        # Debugger.showList(self.timeLineTotalFrame, "TimeLineTotalFrame")
        Debugger.showList(self.timeLineEachFrame, "TimeLineEachFrame")
        Debugger.showList(self.timeLineCoordinate, "TimeLineCoordinate")
        Debugger.showList(self.timeLineDirection, "TimeLineDirection")
        # Adjust Direction

        # set the Final Timeline
        #self.finalTimeLine()

        solvedTimeLine = [self.timeLineName, self.timeLineCoordinate
            , self.timeLineDirection, self.timeLineEachFrame]

        return solvedTimeLine

    """Init the time line before detect Direction Turning"""
    def initialTimeLine(self,cIndex,cMotion):
        print("Init the TimeLine")
        # remember to use len() function
        # len(cIndex) - 1 because we have a end Motion
        for i in range(len(cIndex)-1):
            # Solve the Initial Name
            self.timeLineName.insert(i, cMotion[i])
            #print(i, " Name ", self.timeLineName[i])
            # Solve Initial Name done

            # Solve the Initial Coordinate
            self.timeLineCoordinate.insert(i,self.getFloorCoordinate(cIndex[i]))
            #print(i, " Coord ",self.timeLineCoordinate[i])
            # Solve Initial Coord done

            # Solve the Initial Direction
            # Every direction is solve by the first & second index
            if(i != len(cIndex)- 1):
                norDirection = self.getCharactor2dDirection(cIndex[i], cIndex[i+1])
                angle = self.getAngleOfCircleCoordinate(norDirection)
                # Adjust the time here
                self.timeLineDirection.insert(i,angle + self.motionType.getAdjustByName(cMotion[i]))
                #print(i," Direction ",self.timeLineDirection[i])
            #if(i == len(cIndex)- 1 -1):
            #    self.timeLineDirection.insert(i, self.timeLineDirection[i-1])
                #print(i," Direction ", self.timeLineDirection[i])
            # Solve Initial angle done

            # Solve the Initial Frame
            # Total Frame
            self.timeLineTotalFrame.insert(i,self.motionType.getFrameByName(cMotion[i]))
            # Each Frame
            self.timeLineEachFrame.insert(i, self.motionType.getFrameByName(cMotion[i]))
            #print(i," Frame ",self.timeLineTotalFrame[i])
            # Solve Initial Frame done

        # Initial For End

    """the Input of the function is Direction"""
    """When the direction is different between 1-2&2-3 frame"""
    """We need to add a frame to turn the charactor to the next frame direction"""
    def detectTurning(self,cDirection):
        print("Detecting The Turning")
        #print("length of cDirection:",len(cDirection))
        # We do not need to detect the last direction
        for i in range(len(cDirection)-1):
            # if the direction one != direction 2, its the turning
            if (cDirection[i] != cDirection[i+1]) & (self.timeLineName[i] != 'turn'):
                #print("Direction I",cDirection[i])
                #print("Direction I+1", cDirection[i+1])

                # We insert 4:name,Coordinate,direction,Frame

                # The Name of the Turning is turn
                self.motionType.setTurn()
                self.timeLineName.insert(i+1, self.motionType.motionName)
                #print(i+1, " Name ", self.timeLineName[i+1])

                # We assume that the turning frame count is 24
                # Total Frame
                self.timeLineTotalFrame.insert(i+1, self.motionType.frameNum)
                # Each Frame
                self.timeLineEachFrame.insert(i + 1, self.motionType.frameNum)
                #print(i+1, " Frame ", self.timeLineTotalFrame[i+1])

                # We do not change the coord of the Motion
                self.timeLineCoordinate.insert(i+1, self.timeLineCoordinate[i+1])
                #print(i+1, " Coord ", self.timeLineCoordinate[i+1])

                # The direction is the next step direction
                self.timeLineDirection.insert(i+1, self.timeLineDirection[i+1])
                #print(i+1, " Direction ", self.timeLineDirection[i+1])

    """We need to adjust the direction of every motion"""
    """so it will point to the x+"""
    def adjustDirection(self):

        return

    """Use to add end time to Timeline"""
    def addEndTime(self,cIndex,cMotion):
        # The last not point the coordinate but the direciton
        lenTimeLine = len(self.timeLineName)
        lenMotion = len(cMotion)
        #print('lenCo', lenCo)
        #print(cIndex[7])

        #This place need to be change
        self.timeLineCoordinate.insert(lenTimeLine+1,self.timeLineCoordinate[lenTimeLine-1])

        #Calculate Direction
        norDirection = self.getCharactor2dDirection(cIndex[lenMotion-2], cIndex[lenMotion-1])
        #We adjust the angle here
        angle = self.getAngleOfCircleCoordinate(norDirection) + self.motionType.getAdjustByName(cMotion[lenMotion-2])
        self.timeLineDirection.insert(lenTimeLine+1, angle)
        # This direction is diffcult to judge


    """Use to get the add up Timeline"""
    def finalTimeLine(self):
        print("Final Time Line")
        #Debugger.showList(self.timeLineTotalFrame, "TimeLineTotalFrame")
        for i in range(len(self.timeLineTotalFrame)):
            addUp = 0
            for j in range(len(self.timeLineTotalFrame) - i - 1):
                addUp = addUp + self.timeLineTotalFrame[j]
            self.timeLineTotalFrame[len(self.timeLineTotalFrame)-i-1] = addUp

        #Debugger.showList(self.timeLineTotalFrame,"TimeLineTotalFrame")

    """Use to init the floor"""
    def setFloorData(self):
        self.initialX = self.floorCenterX + self.xLength/2
        self.initialZ = self.floorCenterZ - self.zLength/2

        # Need to be assignment by the Detect Server
        #xNum = ..
        #zNum = ..
        #xLength = ..
        return 0

    """Use RedDATA to get actual data of the coordinate"""
    def getFloorCoordinate(self,index):
        #Zero is X max and z min
        #i,j start from 0 end on Num-1

        jIndex = index % self.zNum
        iIndex = (index - jIndex) / self.xNum
        eachX = self.xLength/self.xNum
        eachXp2 = eachX/2
        eachZ = self.zLength/self.zNum
        eachZp2 = eachZ/2
        #print("eachX",eachX)
        tX = self.initialX - eachXp2 - (iIndex) * eachX
        tZ = self.initialZ + eachZp2 + (jIndex) * eachZ

        coordinateGet = [tX,tZ]
        return coordinateGet

    """Get the Direction of the Charactor between step"""
    def getCharactor2dDirection(self,indexFirst,indexSecond):
        coFirst = self.getFloorCoordinate(indexFirst)
        coSecond = self.getFloorCoordinate(indexSecond)
        deltaX = coSecond[0] - coFirst[0]
        deltaY = coSecond[1] - coFirst[1]
        delta = [deltaX,deltaY]
        return self.Normalize2d(delta)

    """Get the Normalize of a Number"""
    def Normalize2d(self,delta):
        # The last motion 'end' cannt collide with last-1 motion,else false
        d = ((delta[0]*delta[0])+(delta[1]*delta[1])) ** 0.5
        t = [0,0]
        t[0] = delta[0]/d
        t[1] = delta[1]/d
        return t

    """Get the Angle of the Circle Coordinate"""
    """Thats mean you can get the Y rotate of Maya Render"""
    def getAngleOfCircleCoordinate(self,delta):
        if(delta[0]>=0):
            if(delta[1]>=0):
                radian = math.asin(-delta[1])
                #print("radian",radian)
                angle = math.degrees(radian)

            else:
                #no plus 2pi is -45
                radian = math.asin(-delta[1])
                #print("radian",2*math.pi+radian)
                angle = math.degrees(2*math.pi+radian)

        else:
            if(delta[1]>=0):
                radian = math.asin(-delta[1])
                #print("radian",math.pi - radian)
                angle = math.degrees(math.pi - radian)

            else:
                radian = math.asin(-delta[1])
                #print("radian",math.pi - radian)
                angle = math.degrees(math.pi - radian)

        if(angle<0):
            angle += 360
        if(angle>360):
            angle -= 360

        return angle

#Test Information
#x.setInitialData()
#index = 12
#print("floorCoordinate",str(index)," :",x.getFloorCoordinate(index))
#nor = x.getCharactor2dDirection(7,12)
#print(x.getAngleOfCircleCoordinate(nor))
#x= TimeSolver()
#x.setFloorData()
#print(x.getFloorCoordinate())