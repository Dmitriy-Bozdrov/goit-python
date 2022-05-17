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



