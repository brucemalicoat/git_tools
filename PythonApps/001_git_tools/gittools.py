project_directory = """c:/git/github/git_tools/PythonApps/001_git_tools"""
#region imports
import  os
os.chdir(project_directory)
import sys
import tkinter
import pandastable
sys.path.append('../..')
from    PythonClasses.Application     import  Application
#endregion imports

myApp = Application(    arg_title               =       "gittools v1.0.0")
myApp.readConig(        arg_config_filename     =       "gittools.ini")
myApp.setGit()
myApp.run()                                






