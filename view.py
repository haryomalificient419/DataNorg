from dataclasses import dataclass
import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

from typing import Text


class Start(Screen):
    _popup: object
    
    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)
        self._popup = PopupWarningMessage()
        
    def open_warning_message(self) -> object:
        self._popup.open()

class DataEntry(Screen):
    def __init__(self, **kwargs):
        super(DataEntry, self).__init__(**kwargs)

class PopupWarningMessage(Popup):
   pass 

class DataNorg(App):
    def build(self) -> object:
        self.icon = 'datanorg.png'
        screen_manager = ScreenManager()
        start_screen = Start(name="start")
        data_entry_screen = DataEntry(name="dataentry")
        screen_manager.add_widget(start_screen)
        screen_manager.add_widget(data_entry_screen)
        
        return screen_manager


