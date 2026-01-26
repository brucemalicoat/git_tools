project_directory = """c:/git/github/git_tools/PythonApps/001_git_tools"""
import  os
os.chdir(project_directory)
import sys
sys.path.append('../..')
from    PythonClasses.Application     import  Application


myApp = Application(    arg_title               =       "gittools v1.0.0")
myApp.readConig(        arg_config_filename     =       "gittools.ini")
myApp.setGit()
myApp.run()                                






