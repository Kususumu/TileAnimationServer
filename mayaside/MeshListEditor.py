# Use to edit the transform group of the object

meshList = cmds.ls('_Mesh*',sl = False , mat = False)
print('meshList::',meshList)


for obj in meshList:
    #to Filter the Shape Obj
    if(cmds.nodeType(obj)== 'transform'):
        print(obj)
        #the x,y must be -
        cmds.scale(-0.1,-0.1,0.1,obj)

#cmds.scale(0.1,0.1,0.1,str(mesh))