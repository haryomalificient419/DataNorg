from dataclasses import dataclass
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.properties import ObjectProperty

import os

from typing import Text


class Start(Screen):
    _popup: object
    
    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)
        self._popup = None

    def set_popup(self, obj: object) -> None:
        self._popup = None
        self._popup = obj

    def dismiss_popup(self) -> None:
        self._popup.dismiss()
        
    def open_warning_message(self) -> object:
        self.set_popup(WarningMessage())
        self._popup.open()

    def open_file(self) -> object:
        self.set_popup(OpenFile(load=self.load))
        self._popup.open()

    def load(self, path, filename):
        with open(os.path.join(path, filename[0])) as stream:
            #self.text_input.text = stream.read()
            print(stream.read())

        self.dismiss_popup()


class DataEntry(Screen):
    def __init__(self, **kwargs):
        super(DataEntry, self).__init__(**kwargs)

class WarningMessage(Popup):
   pass

class OpenFile(Popup):
    load = ObjectProperty(None)


class DataNorg(App):
    def build(self) -> object:
        self.icon = 'datanorg.png'
        screen_manager = ScreenManager()
        start_screen = Start(name="start")
        data_entry_screen = DataEntry(name="dataentry")
        screen_manager.add_widget(start_screen)
        screen_manager.add_widget(data_entry_screen)
        
        return screen_manager


