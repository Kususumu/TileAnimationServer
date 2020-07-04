#CharacterAdaptionPreious.py
#Introdaction
#An python C script that can
#0.load a scene with the furniture 
#    ->and the character
#1.import a Character & import obj
#2.move & rotate it to where you want  
#3.duplicate one Charactor and make it a white model
#4.let the White Charactor do 
#    ->what the Color Charactor do
#5.do an animation
#6.render an animation to special folder

#start from move a cube and duplicate it
#to make an animation

#first create and copy the object named colorCharacter
#delete the name whos name is "Color********"
#In the newestModel.mb every step is 75 in the grid
#Function : keyFrameForTwoCharacter
#Usage : Input the animation Character and List of what they do
#    ->would happen on the object
#    ->To make the Two Character do the same animation in one step
#

#The True Editer is main
#meshList = cmds.ls('Main',sl = False , mat = False)
#result = meshList[0]
#print(result)
#cmds.move(0,0,0,result)
def keyFrameForTwoCharacter(colorName,whiteName,listToDo):
    #colorObject
    cmds.setKeyframe(colorName,time=startTime,attribute='translateX',value=0 )
    cmds.setKeyframe(colorName,time=endTime,attribute='translateX',value=2)

    #White Object
    cmds.setKeyframe(whiteName,time=startTime,attribute='translateY',value=0 )
    cmds.setKeyframe(whiteName,time=endTime,attribute='translateY',value=2)
    return;
    
#Function : shapeWhiteCharacter
#Usage : When get a copy of the Original Character
#     ->We need to change the copy on to white Character
#
def shapeWhiteCharacter(whiteCharacter):
    
    return; 
    
#Function : renderProcess
#Usage : Use to render the final scene
#
def renderProcess():
    
    return;
    
cubeList = cmds.ls('Color*')
if len(cubeList) > 0:
    cmds.delete(cubeList )
    
cubeList = cmds.ls('White*')
if len(cubeList) > 0:
    cmds.delete(cubeList )

#create a cube that is 3,3,3
result = cmds.polyCube(w=3,h=3,d=3,name = 'ColorCharacter')

#print the result
print 'result:'  + str( result )

#get the Name of the Model from result
transformName = result[0]

duplicateResult = cmds.duplicate(transformName , name='WhiteCharacter')
print 'duplicateResult: ' + str( duplicateResult )
duplicateName = duplicateResult[0]


#start giving an animation
startTime = cmds.playbackOptions(query=True , minTime=True)
endTime = cmds.playbackOptions(query=True , maxTime=True)

#Delete the Key of one Animation
cmds.cutKey(transformName,time=(startTime,endTime),attribute='translateX')

#set KeyFrame must be a function choose by the user
#Set Key Frame
keyFrameForTwoCharacter(transformName,duplicateName,startTime);




