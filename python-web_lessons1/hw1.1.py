from abc import *
import json
import pickle


class SerializationInterface(ABC):

    @property
    @abstractmethod
    def some_data(self):
        return some_data
    
            
class SerializationJson(SerializationInterface):

    some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}

    def create_json_file(self): 
        with open("data_file.json", "w") as file:
            json.dump(self.some_data, file)

    
class SerializationBin(SerializationInterface):
    
    some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}

    def create_bin_file(self):
        with open("data_file.bin", "wb") as file:
            pickle.dump(self.some_data, file)
           

dser_json = SerializationJson()
dser_json.create_json_file()

dser_bin = SerializationBin()
dser_bin.create_bin_file()





