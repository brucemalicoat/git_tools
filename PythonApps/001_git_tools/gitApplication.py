#region imports
import  sys
import  tkinter
import  pandas
sys.path.append('../..')
from    PythonClasses.Datawindow      import  Datawindow
from    PythonClasses.Frame           import  Frame
from    PythonClasses.Window          import  Window
from    PythonClasses.Notebook        import  Notebook
from    PythonClasses.Label           import  Label
from    PythonClasses.Config          import  Config
from    PythonClasses.Git             import  Git
from    PythonClasses.Button          import  Button
from    PythonClasses.Application     import  Application
#endregion imports

class   gitApplication(Application):
        """     
        ---------------------------------------------------------------------------------------------------------------------------
        class:                          gitApplication
        inherits from:                  Application
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
        def btn_status_clicked( self ):
            try:
                        self.w_main.ivar_framelist[1].ivar_notebooklist[0].select(0)
                        lstr_git_status = self.ivar_Git.status()
                        self.w_main.ivar_output_label['text']=lstr_git_status

            except Exception as GitCommandError:
                        self.w_main.ivar_output_label['text']=str(GitCommandError)

        def btn_log_clicked( self ):
            try:
                        self.w_main.ivar_framelist[1].ivar_notebooklist[0].select(2)
                        lvar_log = self.ivar_Git.log().split('\n')
                        lvar_df  = pandas.DataFrame()
                        lvar_df["Commit"]=lvar_log
                        #print( lvar_log )
                        self.w_main.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[2].ivar_datatable.setDF(lvar_df)
                        self.w_main.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[2].ivar_datatable.columnwidths['Commit'] = 1000

            except Exception as GitCommandError:
                        self.w_main.ivar_output_label['text']=str(GitCommandError)


        def btn_commit_clicked( self ):
            try:
                        self.w_main.ivar_framelist[1].ivar_notebooklist[0].select(0)

                        # commit any pending git changes after add . 
                        lstr_git_status = self.ivar_Git.git.execute("git status")
                        if lstr_git_status.split("\n")[1] == "nothing to commit, working tree clean": 
                                self.w_main.ivar_output_label['text']=lstr_git_status.split("\n")[1]
                                return()
                        lstr_commit_message = tkinter.simpledialog.askstring("Commit Message","Please enter a commit message:")
                        
                        if lstr_commit_message == None:
                                self.w_main.ivar_output_label['text']="You must enter a commit message to do a commit operation." 
                                return()

                        self.w_main.ivar_output_label['text']="please wait..."

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

                        super().__init__( arg_title )

                        # main window properties
                        # ----------------------
                        self.w_main.StandardWindow1( tabnames=['Status','Git Info','Log','Modified'] )

                        self.w_main.ivar_output_label.set_background_color( color="White")
                        self.w_main.ivar_output_label.loadfile( "helpfile.txt" )

                        self.w_main.ivar_framelist[0].button_status       =       Button( self.w_main.ivar_framelist[0], text="Status", command=self.btn_status_clicked )
                        self.w_main.ivar_framelist[0].button_status.grid(         row=0,column=0,sticky='EW')

                        self.w_main.ivar_framelist[0].button_commit       =       Button( self.w_main.ivar_framelist[0], text="Commit/Push", command=self.btn_commit_clicked )
                        self.w_main.ivar_framelist[0].button_commit.grid(         row=1,column=0,sticky='EW') 

                        self.w_main.ivar_framelist[0].button_log          =       Button( self.w_main.ivar_framelist[0], text="History", command=self.btn_log_clicked )
                        self.w_main.ivar_framelist[0].button_log.grid(            row=2,column=0,sticky='EW') 

        def     readConig(      self,
                                arg_config_filename : str ):

                        # configuration values
                        # --------------------
                        self.ivarConfig = Config(arg_config_filename)
                        llist_section = []
                        llist_key = []
                        llist_value = []
                        for section in self.ivarConfig.sections():
                                for     key_value_pair in self.ivarConfig.items( section ):
                                        llist_section.append(   section )
                                        llist_key.append(       key_value_pair[0] )
                                        llist_value.append(     key_value_pair[1] )
                                        # print( "section:" + section + "   key:" + key_value_pair[0] + "   value:" + key_value_pair[1] )


                        self.w_main.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[1].ivar_datatable.setDF( pandas.DataFrame({ 'Section'       :llist_section, 
                                                                                                        'Key'           :llist_key,
                                                                                                        'Value'         :llist_value } )
                                                                                   )
                        for index in range(len(llist_section)):                        
                                        self.w_main.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[1].ivar_datatable.set_cell_background_color( 0, index, "Yellow" )


        def     setGit(         self ):

                        self.ivar_Git = Git( self.ivarConfig.ivar_key_values[('git','repo_directory')])
                        df_length = len( self.w_main.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[1].ivar_datatable.model.df )

                        self.w_main.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[1].ivar_datatable.model.df.loc[ df_length ]         = ['git','current branch',              self.ivar_Git.active_branch.name        ]
                        self.w_main.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[1].ivar_datatable.model.df.loc[ df_length + 1 ]     = ['git','git version',                 str(self.ivar_Git.git.version_info)     ]

                        self.w_main.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[1].ivar_datatable.redrawDF()
                        for index in range(df_length+2):                        
                                        self.w_main.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[1].ivar_datatable.set_cell_background_color( 0, index, "Yellow" )
                                        self.w_main.ivar_framelist[1].ivar_notebooklist[0].ivar_framelist[1].ivar_datatable.set_cell_background_color( 1, index, "Yellow" )




