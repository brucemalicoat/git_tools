#region imports
from git import Repo # pip install GitPython
#endregion imports

class   Git(Repo):
        """     
        ---------------------------------------------------------------------------------------------------------------------------
        class:                          Git
        inherits from:                  git.Repo
        ---------------------------------------------------------------------------------------------------------------------------
        repo:                           https://github.com/brucemalicoat/git_tools
        license:                        MIT
        created:                        2026-01-20 Bruce Malicoat - no Jira ticket #
        description:                    interact with a git library
        ---------------------------------------------------------------------------------------------------------------------------
        modified:
        description:
        ---------------------------------------------------------------------------------------------------------------------------
        """
        ivar_error : str = ""
        ivar_last_commit_id : str = ""
        
        # constructor - extend super().__init__
        # -------------------------------------
        def     __init__(       self,
                                *args,
                                **kargs):

                super().__init__(*args,**kargs)

        def     status(         self )->str:
                try:
                        return( self.git.execute("git status") )

                except Exception as GitCommandError:
                        self.ivar_error = str(GitCommandError)
                        print( "git error: " + self.ivar_error )
                        raise GitCommandError

        def     add(         self )->str:
                try:
                        return( self.git.execute("git add .") )

                except Exception as GitCommandError:
                        self.ivar_error = str(GitCommandError)
                        print( "git error: " + self.ivar_error )
                        raise GitCommandError

        def     commit(         self,
                                arg_commit_message : str 
                        )->str:

                try:
                        return( self.git.execute('git commit -m "' + arg_commit_message.replace('"',"'") + '"') )

                except Exception as GitCommandError:
                        self.ivar_error = str(GitCommandError)
                        print( "git error: " + self.ivar_error )
                        raise GitCommandError

        def     push(         self
                        )->str:

                try:
                        str(self.git.execute('git push origin "' + self.active_branch.name + '"',with_extended_output=True))  

                        # compare local last branch commit id vs remote commit id (maybe parnoid but)
                        self.ivar_last_commit_id        = self.git.execute('git rev-parse HEAD').replace('"','')
                        self.git.execute('git fetch --quiet --all')
                        self.ivar_last_remote_commit_id = self.git.execute('git rev-parse origin/'+self.active_branch.name)

                        if (self.ivar_last_commit_id == self.ivar_last_remote_commit_id):
                                return(self.ivar_last_commit_id + ' has been pushed to origin/'+self.active_branch.name)
                        else:
                                return("mismatch between local commit:" + self.ivar_last_commit_id + " and remote commit:" + self.ivar_last_remote_commit_id)

                except Exception as GitCommandError:
                        self.ivar_error = str(GitCommandError)
                        print( "git error: " + self.ivar_error )
                        raise GitCommandError
