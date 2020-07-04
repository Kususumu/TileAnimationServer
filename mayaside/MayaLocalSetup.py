# Use in maya to start the port of the socket server
# Use in maya port version render
import maya.cmds as cmds
if not cmds.commandPort(':54321', q=True):
   cmds.commandPort(n=':54321')