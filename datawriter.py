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
    #content: "Username; Identifier;"


    
@dataclass
class Csv(Converter):
    keys: str

    def set_keys(self)->None:
        self.content = self.content.partition('\n')
        self.keys = self.content[0].split(';')

    def check_int(self, value: str)->int:
            val=value
            try:
                val = int(value)
            except:
                pass
            return val

    def convert_to_json(self)->None:
        with open('{}.json'.format(self.file_name), 'w') as writer:
            writer.write("[\n")
            layers = self.content[2].split('\n')
            for layer in range(len(layers)):
                sub_layers = layers[layer].split(';')
                writer.write(" {\n")
                for sub_layer in range(len(sub_layers)):
                    if sub_layer == len(sub_layers) - 1:
                        if isinstance(self.check_int(sub_layers[sub_layer]), int):
                            writer.write('   "'+self.keys[sub_layer].strip(" ")+'"'+": "+sub_layers[sub_layer]+",\n")
                        else:
                            writer.write('   "'+self.keys[sub_layer].strip(" ")+'"'+": "+'"'+sub_layers[sub_layer]+'"'+"\n")
                    else:
                        if isinstance(self.check_int(sub_layers[sub_layer]), int):
                            writer.write('   "'+self.keys[sub_layer].strip(" ")+'"'+": "+sub_layers[sub_layer]+",\n")
                        else:
                            writer.write('   "'+self.keys[sub_layer].strip(" ")+'"'+": "+'"'+sub_layers[sub_layer]+'"'+","+"\n")
                         
                if layer == len(layers) - 1:
                    writer.write(" }")
                else:
                    writer.write(" },\n\n")
            writer.write("\n]")

    def convert_to_xml(self):
        pass


class Json(Converter):
    def get_keys(self):
        pass
    def convert_to_json(self):
        pass
    def convert_to_xml(self):
        pass
    
class Xml(Converter):
    pass



#For test purposes only
"""
if __name__ == '__main__':
    csv = Csv("klk", ".csv", ".json", None, None)
    csv.content = '''Username; Identifier;One-time password;Recovery code;First name;Last name;Department;Location
booker12;9012;12se74;rb9012;Rachel;Booker;Sales;Manchester
grey07;2070;04ap67;lg2070;Laura;Grey;Depot;London
johnson81;4081;30no86;cj4081;Craig;Johnson;Depot;London
jenkins46;9346;14ju73;mj9346;Mary;Jenkins;Engineering;Manchester
smith79;5079;09ja61;js5079;Jamie;Smith;Engineering;Manchester'''
csv.set_keys()
csv.convert_to_json()
"""