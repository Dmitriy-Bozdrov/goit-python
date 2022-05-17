from abc import *
import json
import pickle


class SerializationInterface(ABC):
    
    @abstractmethod
    def create_json_file(self, *args, **kwargs):
        pass

    @abstractmethod
    def create_bin_file(self, *args, **kwargs):
        pass


class Serialization(SerializationInterface):
    
    def create_json_file(self, *args, **kwargs): 
        with open("data_file.json", "w") as file:
            json.dump(args, file)
            
    def create_bin_file(self, *args, **kwargs):
        with open("data_file.bin", "wb") as file:
            pickle.dump(args, file)     

    
some_data = {'key': 'value', 2: [1, 2, 3], 'tuple': (5, 6), 'a': {'key': 'value'}}

dser_json = Serialization()
dser_json.create_json_file(some_data)

