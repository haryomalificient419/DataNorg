from dataclasses import dataclass



import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

import os

from typing import Text


class Start(Screen):
    _popup: object
    _format_from: str
    _format_to: str
    
    
    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)
        self._popup = None
        self._format_from = None
        self._format_to = None

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

    def set_format_from(self, format:str) -> None:
        self._format_from = format

    def set_format_to(self, format:str) -> None:
        self._format_to = format
        
    
    def load(self, path, filename):
        try:
            with open(os.path.join(path, filename[0])) as stream:
                certified_files = ('.csv', '.xml', '.json', '.sql')
                try:
                    for certified_file in certified_files:
                        if self.is_valid_filename(filename, certified_file):
                            content = PresentFile(text_input = stream.read())
                            self.set_format_from(certified_file)
                            self.add_widget(content)
                except:
                    pass
        except:
            pass


        self.dismiss_popup()
    
    def is_valid_filename(self, file:Text, file_type:Text) -> bool:
        return file[0].endswith(file_type)
        


class DataEntry(Screen):
    def __init__(self, **kwargs):
        super(DataEntry, self).__init__(**kwargs)

class WarningMessage(Popup):
   pass

class OpenFile(Popup):
    load = ObjectProperty(None)

class PresentFile(FloatLayout):
    text_input = ObjectProperty(None)




