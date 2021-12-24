from dataclasses import dataclass



import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

from datawriter import*

import os

from typing import Text


class Start(Screen):
    _popup: object
    _format_from: str
    _format_to: str
    _file_name: str
    _content: Text
    
    
    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)
        self._popup = None
        self._format_from = None
        self._format_to = None
        self._file_name = None
        self._content = None

    def set_popup(self, obj: object) -> None:
        self._popup = None
        self._popup = obj

    def dismiss_popup(self) -> None:
        self._popup.dismiss()
        
    def open_warning_message(self) -> None:
        self.set_popup(WarningMessage())
        self._popup.open()

    def open_file(self) -> None:
        self.set_popup(OpenFile(load=self.load))
        self._popup.open()

    def set_file_name(self, filename) -> None:
        self._file_name = filename

    def set_content(self, content) -> None:
        self._content = content

    def set_format_from(self, format:str) -> None:
        self._format_from = format

    def set_format_to(self, format:str) -> None:
        self._format_to = format
        if self._format_from == ".csv":
            csv = Csv(self._file_name, self._format_from, self._format_to, None, None)
            csv.content = self._content
            if self._format_to == ".json":
                csv.set_keys()
                csv.convert_to_json()
            if self._format_to == ".xml":
                csv.set_keys()
                csv.convert_to_xml()
        
        
    
    def load(self, path, filename):
        try:
            with open(os.path.join(path, filename[0])) as stream:
                certified_files = ('.csv', '.xml', '.json')
                try:
                    for certified_file in certified_files:
                        if self.is_valid_filename(filename, certified_file):
                            text_content = stream.read()
                            content = PresentFile(text_input = text_content)
                            self.add_widget(content)
                            self.set_content(text_content[:])
                            self.set_format_from(certified_file)
                            file_ind_start = len(filename[0]) - filename[0][::-1].find("\\")
                            compl_filename = filename[0][file_ind_start:]
                            new_filename = compl_filename[:compl_filename.find(".")]
                            self.set_file_name(new_filename)
                            
                except:
                    pass
        except:
            pass


        self.dismiss_popup()
    
    def is_valid_filename(self, file:Text, file_type:Text) -> bool:
        return file[0].endswith(file_type)
        




class WarningMessage(Popup):
   pass

class OpenFile(Popup):
    load = ObjectProperty(None)

class PresentFile(FloatLayout):
    text_input = ObjectProperty(None)




