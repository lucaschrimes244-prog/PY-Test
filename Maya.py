import maya.cmds as cmds

print ("Spawn a PolyCube via VSCode")
Cube = cmds.polyCube(name='myCube', width=1, height=2, depth=3, subdivisionsX=2, subdivisionsY=1, subdivisionsZ=3)


cmds.move(0, 5, 0, Cube) # Move the cube up 5 units in Y axis

x = cmds.getAttr('myCube.translateX') # Get the X position of the cube
y = cmds.getAttr('myCube.translateY') # Get the Y position of the cube
z = cmds.getAttr('myCube.translateZ') # Get the Z position of the cube

print (f"My Attributes are: x:{x}, y:{y}, z:{z}")

attribs = cmds.listAttr(Cube) # List all attributes of the cube
for attrib in attribs:
    #currentAttrib = cmds.getAttr(Cube.[attrib])
    print(attrib)
    #try:
        
        #value = cmds.getAttr(f'{Cube}.{attrib}') # Get the value of each attribute
        #print (Cube+'.'+ str(attrib) , ' : ', str(value)) # Print the attribute and its value
    #except RuntimeError:
    #    pass # Some attributes cananot be read, so we skip those
    #except ValueError:
    #    pass # Some attributes cannot be read, so we skip those
