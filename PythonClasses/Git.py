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
        
        # constructor - extend super().__init__
        # -------------------------------------
        def     __init__(       self,
                                *args,
                                **kargs):

                super().__init__(*args,**kargs)
