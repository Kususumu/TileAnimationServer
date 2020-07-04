# The TimeLineRender decode the TimeLine and make the final render in renderer
import Debugger
import ImportFBX
import MessageDoc
import time
import MotionType

# Cause there is many motion we want to render
# Each time we take one motion out to render
class TimeLineRender:
    motionWeRender = [0,0,0]
    mayaClientHandle = 0
    motionType = MotionType.MovingType()

    def __init__(self,mayaClient):
        self.motionWeRender.clear()
        self.mayaClientHandle = mayaClient

    # solvedTimeLine 0 : timeLineName 1 : timeLineCoordinate
    #                2 : timeLineDirection 3 : timeLineEachFrame
    def render(self,solvedTimeLine):
        # Take out the motion for render
        self.takeMotionForRender(solvedTimeLine[0])
        #Debugger.showList(self.motionWeRender,"MotionWeRender")

        self.renderMotionByMotion(self.motionWeRender,solvedTimeLine)


    # We need to take out the render motion first
    # So we can render motion Index by Index
    def takeMotionForRender(self,solvedMotion):
        self.motionWeRender.clear()
        countMotion = 0
        for i in range(len(solvedMotion)):
            if(solvedMotion[i] not in self.motionWeRender):
                self.motionWeRender.insert(countMotion,solvedMotion[i])
                countMotion += 1

    # We use this function to render motion step by step
    def renderMotionByMotion(self,typeMotion,solvedTimeLine):
        # Clear Secene before use this Function
        self.clearMotionInScene()

        #self.clearMotionInSceneSecond()
        # Read the Type Motion
        #for i in range(len(typeMotion)):
        for i in range(len(typeMotion)):
            #For Test : tempMotion = typeMotion[1]
            tempMotion = typeMotion[i]

            # Choose the motion
            print(tempMotion)

            # Clear Character Motion in 2 seconds
            self.clearMotionInScene()

            # This place need to be improved , we need a database to search the path of motion
            self.importMotion(tempMotion)

            self.renderMotionStepByStep(tempMotion,solvedTimeLine)


    # Wait 5 seconds for import motion
    def importMotion(self,motionName):
        message = ImportFBX.importMB(self.motionType.getPathByName(motionName))
        self.mayaClientHandle.send(message)
        # Import Scene in 5 seconds
        time.sleep(7)

        # Each Time we import a new motion,we need to get the main Controller
        self.getMain()

    # When we know one motion need to render
    # We need to know what time it need to be render
    def renderMotionStepByStep(self,tempMotion,solvedTimeLine):
        # We recognize every index name so we can render
        for i in range(len(solvedTimeLine[0])):


            if(solvedTimeLine[0][i] == tempMotion):
                # Debug Information
                print("render Motion " + str(tempMotion))
                self.sendOneMotionInformation(i,solvedTimeLine)

                #final Render
                self.callArnoldRenderOneMotion(i,solvedTimeLine)

        return 0

    # A Function use to get the Main Controller
    def getMain(self):
        message = MessageDoc.selectMainByMessage()
        self.mayaClientHandle.send(message)

    # Render the exactly motion
    # We call the Message doc here
    # Normal animation made in maya is z+,but we want x+ orientation
    def sendOneMotionInformation(self,i,solvedTimeLine):
        # Debug Information
        print("TimeLineRender: setOneMotionInformation,the Index " + str(i))

        # Send the X,Y,Z Value from the first frame to the last frame

        # On Template We only have Z,no Y
        # Send the translateX Value
        # in [x][x][0] 0 means x Value
        message = MessageDoc.keyFrameStartByMessage(0,'translateX',solvedTimeLine[1][i][0])
        self.mayaClientHandle.send(message)
        time.sleep(1)
        message = MessageDoc.keyFrameEndByMessage(solvedTimeLine[3][i],'translateX',solvedTimeLine[1][i+1][0])
        self.mayaClientHandle.send(message)
        time.sleep(1)

        # Z Value
        message = MessageDoc.keyFrameStartByMessage(0,'translateZ',solvedTimeLine[1][i][1])
        self.mayaClientHandle.send(message)
        time.sleep(1)
        message = MessageDoc.keyFrameEndByMessage(solvedTimeLine[3][i],'translateZ',solvedTimeLine[1][i+1][1])
        self.mayaClientHandle.send(message)
        time.sleep(1)

        # Direction
        message = MessageDoc.keyFrameStartByMessage(0, 'rotateY', solvedTimeLine[2][i])
        self.mayaClientHandle.send(message)
        time.sleep(1)
        message = MessageDoc.keyFrameEndByMessage(solvedTimeLine[3][i], 'rotateY', solvedTimeLine[2][i + 1])
        self.mayaClientHandle.send(message)
        time.sleep(1)

    def callArnoldRenderOneMotion(self,i,solvedTimeLine,startFrame = 0):
        message = MessageDoc.renderArnoldByMessage(startFrame,solvedTimeLine[3][i],i)
        self.mayaClientHandle.send(message)
        #We wait 30 second for 24 frame
        time.sleep(120)

    # Clear the Motion In the Scene when we start render or render the next motion
    def clearMotionInScene(self):
        message = MessageDoc.deleteObjectFrontByMessage('tx2')
        self.mayaClientHandle.send(message)

        message = MessageDoc.deleteObjectFrontByMessage('Set')
        self.mayaClientHandle.send(message)

        # Give System 1 Second to receive the second message
        time.sleep(2)