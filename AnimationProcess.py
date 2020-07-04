import socket
import MovingData
import TimeSolver
import TimeLineRender
import Pic2video

import Debugger

# Use the socket to connect the Maya Render Server
localHostIp = '127.0.0.1'
localPort = 54321
localAddr = (localHostIp, localPort)

mayaClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mayaClient.connect(localAddr)

# Receive motion data first
# Receiving
clickDataFromPhone = [2,8,14,20,21,22,23,29]
clickMotionFromPhone = ['walk', 'walk', 'walk', 'walk', 'walk', 'walk', 'sit','end']

# Create a class of Moving data
movingData = MovingData.MovingData()
movingData.setClickData(clickDataFromPhone,clickMotionFromPhone)

#Debugger.showList(movingData.clickIndex,'MovingData Index')
#Debugger.showList(movingData.clickMotion,'MovingData Motion')

# Create TimeSolver to solve the data
timeSolver = TimeSolver.TimeSolver()
timeSolver.setFloorData()
# Get the SolvedTimeLine
solvedTimeLine = timeSolver.getTimeLine(movingData.clickIndex,movingData.clickMotion)

# Create TimeLine Render , Render the raw picture sequence
timeLineRender = TimeLineRender.TimeLineRender(mayaClient)
timeLineRender.render(solvedTimeLine)
#
print("RenderPicDone")

# From the raw pic sequence to the final video
videoMaker = Pic2video.pic2Video()
videoMaker.rawPicSequence2FinalVideo(solvedTimeLine)
# Final we made it

#Test the Import
#message = ImportFBX.importMB('E:/mayaStore/model/ModelWeUse/scenes/walk0024.mb').encode('utf-8')

# Remember to use the encode() function to translate the information
#MyMessage = MessageDoc.renderByMessage(0,24,10).encode('utf-8')
#mayaClient.send(message)

# receive the result info
data = mayaClient.recv(1024)
print('The Result is %s' % data)

mayaClient.close()
print('Maya Client Close')