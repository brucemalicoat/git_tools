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

        def     push(         self,
                                arg_commit_message : str 
                        )->str:

                try:
                        return( str(self.git.execute('git push origin "' + self.active_branch.name + '"',with_extended_output=True))  )

                except Exception as GitCommandError:
                        self.ivar_error = str(GitCommandError)
                        print( "git error: " + self.ivar_error )
                        raise GitCommandError
