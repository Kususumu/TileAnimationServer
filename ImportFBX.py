#A Function use to import fbx or .mb to maya

import MessageDoc
#import maya.cmds as cmds

#Use in Maya Inside
#import maya.cmds as cmds
#importPath = 'E:/mayaStore/model/ModelWeUse/scenes/sit.mb'
#message = cmds.file(importPath,i=True);

# Because of the texture error
# We don't use the FBX Now
"""
def importFBX():
    setImportPath = 'E:/mayaStore/model/ModelWeUse/scenes/sit.fbx'
    # or X:/Path_To_File.fbx
    message = 'python("cmds.file(importPath,i=True);")'
    return message
"""

# The importPath is the Absolute Path in PC
def importMB(importPath):
    # Test importPath = 'E:/mayaStore/model/ModelWeUse/scenes/sit.mb'
    # The message must use as follows:
    return MessageDoc.importMbByMessage(importPath)


#setImport()