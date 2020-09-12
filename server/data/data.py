class DataGenerator(object):
    """Generate Data to map to a response object"""
    def __init__(self):
        data = self._get_current_data() # returns a timestamp
        self.name = data["name"]
        self.time = data["time"]

    def _get_current_data(self): # generate self.data
        """generates the correct data shape and timestamp to return to the client"""
        return {
            "name": "Data",
            "time": 100
        }

