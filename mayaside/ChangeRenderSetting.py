#ChangeRenderSetting.py
##This only use in the maya software render , not in arnold
#Three main Node of Maya Render:
#   ->defaultRenderGlobals, defaultRenderQuality and defaultResolution
#   ->those are separate nodes in maya
'''


import maya.cmds as cmds

#Function : getRenderGlobals()
#Usage : get the Value of Render Globals and print it
def getRenderGlobals() : 
    render_glob = "defaultRenderGlobals"
    list_Attr = cmds.listAttr(render_glob,r = True,s = True)
    #loop the list
    print 'defaultRenderSetting As follows :'
    for attr in list_Attr:
        get_attr_name = "%s.%s"%(render_glob, attr)
        print "setAttr %s %s"%(get_attr_name, cmds.getAttr(get_attr_name))
    

#Function : getRenderResolution()
#Usage : get the Value of Render Resolution and print it
def getRenderResolution() :
    resolu_list = "defaultResolution"
    list_Attr = cmds.listAttr(resolu_list,r = True , s = True)
    print 'defaultResolution As follows :'
    for attr in list_Attr:
        get_attr_name = "%s.%s"%(resolu_list, attr)
        print "setAttr %s %s"%(get_attr_name, cmds.getAttr(get_attr_name))

    
#defaultRenderGlobals.startFrame = 2.0
#Function : startEndFrame
#Usage : to change the Global value(startFrame,endFrame) of the Render
#use for set the render startFrame,endFrame,byframe
#Example : startEndFrame(3.0,7.0)
def startEndFrame(startTime,endTime) :
    cmds.setAttr("defaultRenderGlobals.startFrame",startTime)
    cmds.setAttr("defaultRenderGlobals.endFrame",endTime)

#Function : setWidthAndHeight
#Usage : to change the Resolution value(width,height) of the Render
#Example : setWidthAndHeight(960,540)
def setWidthAndHeight(width,height) :
    cmds.setAttr("defaultResolution.width",width)
    cmds.setAttr("defaultResolution.height",height)
    

'''