List = cmds.ls('sit_tx2')
print(List)

#Use main to translate the model position
Main = cmds.ls('Main')
print(Main)
result = Main[0]
cmds.setKeyframe(Main[0],time = 0,attribute='translateX',value=0 )

#Each Frame is from 0 to MotionFrameNum
def keyFrameForCharacter(character,endFrame,motion):
    #colorObject
    cmds.setKeyframe(character,time = 0,attribute='translateX',value=0 )
    cmds.setKeyframe(character,time = endFrame,attribute='translateX',value=2)
