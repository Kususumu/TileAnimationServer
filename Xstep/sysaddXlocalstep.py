# Import the plugin path in the pc
import sys
sys.path.append('E:\mayaStore\pythonServerWorkplace\mayaside')

# Import the function what we need to use
# We don't need to take care of the error in pycharm ,because we use it in maya editor
#If you want to use Render,use this
import RenderScript
reload(RenderScript)

#Use to Clear the Scene
import DeleteObject
reload(DeleteObject)


# Local step up
# Use in maya to start the port of the socket server
# Use in maya port version render
import maya.cmds as cmds
if not cmds.commandPort(':54321', q=True):
   cmds.commandPort(n=':54321')