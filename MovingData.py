# The Class MovingData use to Collect Data from the fore-End
# The Test floor width and height is 100* Scale(4) = 400
import TimeSolver


class MovingData:

    """redInt Test Data"""

    """Constructor"""
    def __init__(self):
        # Walk from left to center then up
        #self.clickData = [12,13,14,15,21,27,33]
        #self.clickMotion = ['walk','walk','walk','walk','walk','walk','walk']
        self.clickIndex = [0]
        self.clickMotion = ['None']

    def setClickData(self,cIndex,cMotion):
        self.clickIndex = cIndex
        self.clickMotion = cMotion
        # This place can also provide the camera position by frame if slam
        # self.cameraPosition = [x,x,x]

#For test

#norDirection = ts.getCharactor2dDirection(15, 21)
#print(ts.getAngleOfCircleCoordinate(norDirection))
#print(ts.timeLineDirection)
#print(x.clickIndex)
#print(x.clickMotion)