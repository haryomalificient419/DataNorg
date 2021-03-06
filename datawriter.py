from typing import Text
from dataclasses import dataclass
import os

#first lets work on converting csv to json




@dataclass
class Converter:
    file_name: str
    format: str
    convert_to: str
    content: Text
    keys: str

    #for example
    #file name: "username-password-recovery-code"
    #format: ".csv"
    #convert_to: ".json"
    #content: "Username; Identifier;"

    def set_keys(self)->None:
        self.content = self.content.partition('\n')
        self.keys = self.content[0].split(';')

@dataclass
class Csv(Converter):
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

    def convert_to_xml(self)->None:
        with open('{}.xml'.format(self.file_name), 'w') as writer:
            writer.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            layers = self.content[2].split('\n')
            writer.write("<root>\n")
            for layer in range(len(layers)):
                sub_layers = layers[layer].split(';')
                for sub_layer in range(len(sub_layers)):
                    if sub_layer == 0:
                        writer.write(" <row>\n")
                    writer.write(" "*2+"<"+self.keys[sub_layer].strip(" ")+">"+sub_layers[sub_layer]+\
                        "</"+self.keys[sub_layer].strip(" ")+">""\n")
                    if sub_layer == len(sub_layers) - 1:
                        writer.write(" </row>\n")
            writer.write("</root>\n")
                        
                   
                


class Json(Converter):

    def set_keys(self)->None:
        self.content = self.content.partition('\n')
        layers = self.content[2].split('\n')
        self.keys = []
        
        for layer in range(len(layers)):
            key_layers = layers[layer].split(":")[0]
            if not self.is_parenthesis(key_layers) and\
                not (key_layers.isspace() or "\n" in key_layers or len(key_layers)==0):
                if self.keys is not None and\
                     key_layers not in self.keys:
                     self.keys.append(key_layers)

    def is_parenthesis(self, value:str)->bool:
        lst_parenthesis = ["{", "}", "[", "]", ",", "},"]
        for parenthesis in lst_parenthesis:
            if parenthesis in value:
                return True
        return False

    def convert_to_csv(self):
        with open('{}.csv'.format(self.file_name), 'w') as writer:
            for key_layers in range(len(self.keys)):
                if key_layers != len(self.keys):
                    writer.write(self.keys[key_layers].lstrip(" ").strip('"')+";")
                else:
                    writer.write(self.keys[key_layers].lstrip(" ").strip('"'))
                    writer.write("\n")
            layer = self.content[2].split('\n')
            writer.write("\n")
            for layers in range(len(layer)):
                if len(layer[layers].split(":"))>1:
                    sub_layer = layer[layers].split(":")[1].strip(",")
                    if len(sub_layer.strip('" "')) != 0:
                        if self.keys[len(self.keys)-1] not in\
                            layer[layers].split(":")[0]:
                            writer.write(sub_layer.strip('" "')+";")
                        else:
                            writer.write(sub_layer.strip('" "'))
                if "}" in layer[layers].split(":")[0]:
                    writer.write("\n")
    


    def convert_to_xml(self):
        self.convert_to_csv()
        with open('{}.csv'.format(self.file_name), 'r') as reader:
            content = reader.read()
            csv = Csv(self.file_name, self.format, ".xml", content, None)
            csv.set_keys()
            csv.convert_to_xml()
        os.remove(self.file_name+".csv")

        
    
