# MessageDoc tell you how to send message to Maya Server
# The MessageDoc only can call the function preBuild in the maya
# Sending Message has ""
# message = 'python("importPath = \\"wwwsss\\" ")'
# notice \\"

def renderArnoldByMessage(startFrame,endFrame,motionIndex):
    #{0}:startFrame,{1}:endFrame,{2}:frameNum(use to create the folder)
    message = 'python("RenderScript.renderSequenceWithArnold({0}, {1}, {2})")'\
        .format(startFrame,endFrame,motionIndex).encode('utf-8')
    return message

# Main is the controller of the character
def selectMainByMessage():
    # Main = cmds.ls('Main')
    message = 'python("Main = cmds.ls(\\"Main\\")")'.encode('utf-8')
    return message

# We use this to send keyFrame to motion
# trans # is the value you want to change like : translateX
# we assume that the start time is 0
# We set keyFrame to Main which we get on the upper function
#cmds.setKeyframe(Main[0], time = 0 , attribute='rotateY',value = 90)
def keyFrameStartByMessage(time,trans,value):
    # Start Frame
    message = 'python("cmds.setKeyframe(Main[0],time = {0},attribute=\\"{1}\\",value={2});")'\
        .format(time,trans,value).encode('utf-8')
    return message

def keyFrameEndByMessage(time,trans,value):
    # End Frame
    message = 'python("cmds.setKeyframe(Main[0],time = {0},attribute=\\"{1}\\",value={2});")'\
        .format(time,trans,value).encode('utf-8')
    return message

def deleteObjectFrontByMessage(info):
    message = 'python("DeleteObject.frontDelete(\\"{0}\\")")'.format(info).encode('utf-8')
    return message

def deleteObjectEndByMessage(info):
    message = 'python("DeleteObject.endDelete(\\"{0}\\")")'.format(info).encode('utf-8')
    return message

def importMbByMessage(importPath):
    message = 'python("importPath = \\"{0}\\";cmds.file(importPath,i=True) ")' \
        .format(importPath).encode('utf-8')
    #print(message)
    return message

# Hello World
def createCubeByMessage():
    # In This Place you can send the Message you want
    # the command from external editor to maya
    cmd = 'mc.polyCube();'
    message = 'python("import maya.cmds as mc;{0}")'.format(cmd).encode('utf-8')
    return message

# Render the Scene , Call the function prebuild in maya
def renderByMessage(startFrame , endFrame , frameIndex):
    message = 'python("renderSequence({0}, {1},{2});")'.format(startFrame,endFrame,frameIndex).encode('utf-8')
    return message

