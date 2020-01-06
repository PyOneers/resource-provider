'''
    resource_provider.py
    ~~~~~~
    
    Created By : PyOneers
'''

class ResourceProvider():

    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def get_resource(key:str):
        """ Static access method to fetch resource. """
        if ResourceProvider.__instance == None:
            raise Exception("ResourceProvider configuration is not defined. Initialize ResourceProvider first.")
        return ResourceProvider.__instance.data[key]

    @staticmethod
    def get_all_resources():
        """ Static access method to fetch all resources. """
        if ResourceProvider.__instance == None:
            raise Exception("ResourceProvider configuration is not defined. Initialize ResourceProvider first.")
        return ResourceProvider.__instance.data

    def __init__(self, **kwargs):
        """
        ** kwargs: Single Instance of Resource needed in Application
        """
        if ResourceProvider.__instance != None:
            raise Exception("ResourceProvider already initialized")
        else:
            self.data = kwargs
        ResourceProvider.__instance = self
