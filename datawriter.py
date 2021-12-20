from typing import Text
from dataclasses import dataclass

#first lets work on converting csv to json

@dataclass
class Converter:
    file_name: str
    format: str
    convert_to: str
    content: Text

    #for example
    #file name: "username-password-recovery-code"
    #format: ".csv"
    #convert_to: ".json"

class Csv(Converter):
    def get_keys(self)->None:
        pass

    def convert_to_json(self):
        pass
    def convert_to_xml(self):
        pass
    def convert_to_sql(self):
        pass
    

class Json(Converter):
    def get_keys(self):
        pass
    def convert_to_json(self):
        pass
    def convert_to_xml(self):
        pass
    def convert_to_sql(self):
        pass

class Xml(Converter):
    pass

class Sql(Converter):
    pass