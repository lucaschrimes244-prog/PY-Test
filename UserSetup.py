#For Vscode to maya
print ("Loading userSetup Script")

import maya.cmds as cmds

cmds.commandPort(name="localhost:5678", stp="python")
cmds.commandPort(name="localhost:7001", stp="mel")

#Code to start my tool
print ("Loading Smart Sheet Tool")

def ToolStartup():
    print ("Tool Was Started Successfully!")

ToolStartup()
