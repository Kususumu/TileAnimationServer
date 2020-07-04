# DeleteObject use to delete things in the maya render
# It has front delete and end delete


import maya.cmds as cmds

# Usage:DeleteObject.frontDelete('Set')
# Usage:DeleteObject.frontDelete('tx2')
def frontDelete(info):
    #SetList = cmds.ls('*Set')
    SetList = cmds.ls('*'+str(info))
    if len(SetList) > 0:
        cmds.delete(SetList)
        #print(cubeList)

# Usage:DeleteObject.endDelete('walk')
def endDelete(info):
    typeList = cmds.ls(str(info)+'*')
    if len(typeList) > 0:
        cmds.delete(typeList)
        #print(cubeList)
