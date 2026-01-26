#region imports
import tkinter
import tkinter.ttk
import sys
import pandastable
import pandas
import numpy
import tksheet
from   decimal import Decimal
import decimal
import webcolors
import openpyxl.utils
sys.path.append('../..')
from    PythonClasses.Datawindow      import  Datawindow
from    PythonClasses.Frame           import  Frame
from    PythonClasses.Window          import  Window
from    PythonClasses.Notebook        import  Notebook
from    PythonClasses.Label           import  Label
from    PythonClasses.Config          import  Config
from    PythonClasses.Git             import  Git
#endregion imports

class   Application():
        """     
        ---------------------------------------------------------------------------------------------------------------------------
        class:                          Application
        inherits from:                  None
        ---------------------------------------------------------------------------------------------------------------------------
        repo:                           https://github.com/brucemalicoat/git_tools
        license:                        MIT
        created:                        2026-01-20 Bruce Malicoat 
        description:                    framework for GUI application
        ---------------------------------------------------------------------------------------------------------------------------
        modified:
        description:
        ---------------------------------------------------------------------------------------------------------------------------
        """
        ivar_title      : str           = "Application"
        ivar_Config     : Config        = None
        ivar_Git        : Git           = None

        def status_clicked( self ):
            try:
                        lstr_git_status = self.ivar_Git.status()
                        self.w_main.ivar_output_label['text']=lstr_git_status
            except Exception as GitCommandError:
                        self.w_main.ivar_output_label['text']=str(GitCommandError)


        def commit_clicked( self ):
            try:
                        # commit any pending git changes after add . 
                        lstr_git_status = self.ivar_Git.git.execute("git status")
                        if lstr_git_status.split("\n")[1] == "nothing to commit, working tree clean": 
                                self.w_main.ivar_output_label['text']=lstr_git_status.split("\n")[1]
                                return()
                        lstr_commit_message = tkinter.simpledialog.askstring("Commit Message","Please enter a commit message:")
                        
                        if lstr_commit_message == None:
                                self.w_main.ivar_output_label['text']="You must enter a commit message to do a commit operation." 
                                return()
                        lstr_result  = "git add ." + "\n"         
                        lstr_result += self.ivar_Git.add() + "\n"
                        lstr_result += "-------------------------------\n"
                        lstr_result += 'git commit -m "' + lstr_commit_message + '"\n'      
                        lstr_result += self.ivar_Git.commit( arg_commit_message=lstr_commit_message )+ "\n"
                        lstr_result += "-------------------------------\n"
                        lstr_result += 'git push origin/' + self.ivar_Git.active_branch.name + "\n"   
                        lstr_result += self.ivar_Git.push() + "\n"

                        self.w_main.ivar_output_label['text']=lstr_result

            except Exception as GitCommandError:
                        self.w_main.ivar_output_label['text']=str(GitCommandError)

       # constructor - extend super().__init__
        # -------------------------------------
        def     __init__(       self,
                                arg_title : str):

                        self.ivar_title = arg_title

                        self.w_main = Window(title=self.ivar_title)

                        # main window properties
                        # ----------------------
                        self.w_main.StandardWindow1( tabcount = 2, framecount = 2, tabnames=['Git','Data'] )

                        self.w_main.ivar_output_label.set_background_color( color="White")
                        self.w_main.ivar_output_label.loadfile( "helpfile.txt" )
                        self.w_main.frame_1.button_status = tkinter.Button( self.w_main.frame_1, text="Status", command=self.status_clicked )
                        self.w_main.frame_1.button_status.grid(row=0,column=0)
                        self.w_main.frame_1.button_status = tkinter.Button( self.w_main.frame_1, text="Commit", command=self.commit_clicked )
                        self.w_main.frame_1.button_status.grid(row=1,column=0) 

        def     readConig(      self,
                                arg_config_filename : str ):

                        # configuration values
                        # --------------------
                        self.ivarConfig = Config(arg_config_filename)

                        for idx in range(len(self.ivarConfig.ivar_key_values)):
                                if idx > 5: break
                                self.w_main.ivar_config_label[idx]['text'] += str(list(self.ivarConfig.ivar_key_values.keys())[idx]).ljust(40,' ') + ': ' + list(self.ivarConfig.ivar_key_values.values())[idx]

        def     setGit(         self ):

                        self.ivar_Git = Git( self.ivarConfig.ivar_key_values[('git','repo_directory')])
                        self.w_main.ivar_config_label[len(list(self.ivarConfig.ivar_key_values.keys()))]['text'] += 'current branch'.ljust(40,' ') + ': ' + self.ivar_Git.active_branch.name
                        self.w_main.ivar_config_label[len(list(self.ivarConfig.ivar_key_values.keys()))+1]['text'] += 'git version'.ljust(40,' ') + ': ' + str(self.ivar_Git.git.version_info)


        def     run(            self ):
                        self.w_main.mainloop()