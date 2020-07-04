#Need to prebuild in maya first
#RenderScript.py
#MayaPythonScript : RenderScript
#A script that can use python to automativly render the scene

import maya.cmds as cmds
import maya.cmds as mc
import maya.app.general.createImageFormats as createImageFormats
from mtoa.cmds.arnoldRender import arnoldRender

#Function : getCameraCharacter()
#Usage : use to get the Camera of the Character
#There is only one Camera in the Scene:
    #    ->characterCamera
#Return : the Camera Get
def getCameraCharacter() : 
    #Define the list Camera Class
    cmds.listCameras()
    #get the listCamera
    listCamera = cmds.listCameras()
    #debug information print
    #debug information for list of Cameras
    #print 'listCamera : ' + str(listCamera)
    cameraWant = listCamera[0]
    return cameraWant;

#Function : renderSequence    
#Usage : frome the startFrame to the endFrame , we render it with a advanced setting
#use the render to render the camera want
#cmds.render(cameraWant)
#Input : renderfn(The render Tool) . renderfn_args(The flag use to render)
#the parameter frameNum is look like 00,01,02 to record the Index
def renderSequenceWithMayaSoft(startFrame , endFrame , frameNum ,renderfn = mc.render, renderfn_args = None):
    
    #save the state
    now = mc.currentTime(q = True)
    
    for x in range(startFrame, endFrame):
        #for render information debug
        #print 'RenderScript : Do Render :' + str( x )
        mc.currentTime(x)
        
        #Launch render process
        renderfn(renderfn_args)

        # Save the Picture in RenderView
        savePicInRenderView(frameNum, x)
        
    #restore state
    mc.currentTime(now)

# How to use : RenderScript.renderSequenceWithArnold(0,2,12)
# The function is the same as mayaSoftRender , but it use the arnold
def renderSequenceWithArnold(startFrame, endFrame, frameNum
                             , renderfn = arnoldRender
                             , renderfn_args= [695, 449, True, True,'camera1', ' -layer defaultRenderLayer']):
    # save the state
    now = mc.currentTime(q=True)

    #renderfn_args = [960, 720, True, True,'camera1', ' -layer defaultRenderLayer']

    for x in range(startFrame, endFrame):
        # for render information debug
        # print 'RenderScript : Do Render :' + str( x )
        mc.currentTime(x)

        # Launch render process
        renderfn(renderfn_args[0],renderfn_args[1],renderfn_args[2],renderfn_args[3],renderfn_args[4],renderfn_args[5])
        #renderfn(960, 720, True, True,'camera1', ' -layer defaultRenderLayer')

        # Save the Picture in RenderView
        savePicInRenderView(frameNum,x)

    # restore state
    mc.currentTime(now)

# The function use to save the RenderView frame when being render
def savePicInRenderView(frameIndex,x):
    # save the image to a exist folder
    editor = 'renderView'
    formatManager = createImageFormats.ImageFormats()
    formatManager.pushRenderGlobalsForDesc("PNG")
    # The name of the Image is CharacterImage'+str(x)+.jpg ,example CharacterImage1.jpg\
    cmds.renderWindowEditor(editor, e=True, writeImage='E:/mayaStore/images/imageSequence/CharacterImage_'
                                                       + str(frameIndex).zfill(2) + '_' + str(x).zfill(2) + '.png')
    formatManager.popRenderGlobals()

#Test Function
#renderSequence(0,24,renderfn_args = getCameraCharacter())