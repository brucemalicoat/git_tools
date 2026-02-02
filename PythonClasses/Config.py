#region imports
import configparser
#endregion imports

class   Config(configparser.ConfigParser):
        """     
        ---------------------------------------------------------------------------------------------------------------------------
        class:                          Config
        inherits from:                  configparser.ConfigParser
        ---------------------------------------------------------------------------------------------------------------------------
        repo:                           https://github.com/brucemalicoat/git_tools
        license:                        MIT
        created:                        2026-01-20 Bruce Malicoat - no Jira ticket #
        description:                    parse a config ini file for the application in a consistent way
        ---------------------------------------------------------------------------------------------------------------------------
        modified:
        description:
        ---------------------------------------------------------------------------------------------------------------------------
        """
        ivar_key_values : list = {}

        # constructor - extend super().__init__
        # -------------------------------------
        def     __init__(   self,
                            arg_filename : str ):

                super().__init__()
                self.read( arg_filename )

                for     section_name, section_proxy in self.items():
                        for     key, value in section_proxy.items():

                                dict_value_to_add={ (section_name, key): value }
                                self.ivar_key_values.update(dict_value_to_add)