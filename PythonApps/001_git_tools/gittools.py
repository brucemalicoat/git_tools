import  os
os.chdir("c:/git/github/git_tools/PythonApps/001_git_tools")
#region imports
import sys
import tkinter
import pandastable
sys.path.append('../..')
from    PythonClasses.Window          import  Window
from    PythonClasses.Config          import  Config
from    PythonClasses.Git             import  Git
from    PythonClasses.Button          import  Button
#endregion imports

w_main = Window(title="gittools v1.0.0")

# main window properties
# ----------------------
w_main.StandardWindow1( tabcount = 2, framecount = 2, tabnames=['Git','Data'] )

w_main.ivar_datatable.set_cell_background_color(x=3,y=3,color="red")

w_main.ivar_output_label.set_background_color( color="White")
w_main.ivar_output_label.loadfile( "helpfile.txt" )

# configuration values
# --------------------
config_values = Config("gittools.ini")

for idx in range(len(config_values.ivar_key_values)):
    if idx > 5: break
    w_main.ivar_config_label[idx]['text'] += str(list(config_values.ivar_key_values.keys())[idx]).ljust(40,' ') + ': ' + list(config_values.ivar_key_values.values())[idx]

myGit = Git( config_values.ivar_key_values[('git','repo_directory')])
w_main.ivar_config_label[idx+1]['text'] += 'current branch'.ljust(40,' ') + ': ' + myGit.active_branch.name
w_main.ivar_config_label[idx+2]['text'] += 'git version'.ljust(40,' ') + ': ' + str(myGit.git.version_info)

def status_clicked():
    try:
            lstr_git_status = myGit.git.execute("git status")
            w_main.ivar_output_label['text']=lstr_git_status
    except Exception as GitCommandError:
            w_main.ivar_output_label['text']=str(GitCommandError)

w_main.frame_1.button_status = tkinter.Button( w_main.frame_1, text="Status", command=status_clicked )
w_main.frame_1.button_status.grid(row=0,column=0)

def commit_clicked():
    try:
            lstr_1 = "git add ." + "\n" + myGit.git.execute("git add .") + "\n"
            lstr_2 = "git commit " + "\n" + myGit.git.execute('git commit -m "commit"') + "\n"
            lstr_3 = 'git push origin "' + myGit.active_branch.name + '"\n' + str(myGit.git.execute('git push origin "' + myGit.active_branch.name + '"',with_extended_output=True)) + "\n"
            print( lstr_3 )
            w_main.ivar_output_label['text']=lstr_1+lstr_2+lstr_3
    except Exception as GitCommandError:
            w_main.ivar_output_label['text']=str(GitCommandError)

w_main.frame_1.button_status = tkinter.Button( w_main.frame_1, text="Commit", command=commit_clicked )
w_main.frame_1.button_status.grid(row=1,column=0)


w_main.mainloop()
